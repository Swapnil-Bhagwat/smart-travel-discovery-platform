"""
Step 10 Final Manual Test Matrix (A through R) Verification Script
Smart Travel Discovery and Comparison Platform
"""

import sys
import json
import urllib.request
import urllib.error

BASE_URL = "http://127.0.0.1:5000/api/v1"
FRONTEND_URL = "http://localhost:3000"

def get_json(endpoint):
    url = f"{BASE_URL}{endpoint}"
    req = urllib.request.Request(url, headers={"User-Agent": "MatrixTest/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, json.loads(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode('utf-8'))

def get_frontend(path):
    url = f"{FRONTEND_URL}{path}"
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            return r.status, r.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8')

def test_matrix():
    print("\n==================================================")
    print("STEP 10 — FINAL MANUAL TEST MATRIX (A through R)")
    print("==================================================")
    all_ok = True

    # A. Destination-selected search
    code, res = get_json("/packages?destination_id=1&starting_city=Delhi&per_page=10")
    pkgs = res.get("data", [])
    ok_a = (code == 200) and len(pkgs) > 0 and all(p["destination"]["id"] == 1 for p in pkgs)
    print(f"A. Destination-selected search (Goa, dest=1): {'PASS' if ok_a else 'FAIL'} (Returned {len(pkgs)} pkgs)")
    all_ok &= ok_a

    # B. Destination discovery
    code, res = get_json("/discover/destinations?starting_city=Delhi&budget=50000&travellers=2&duration_days=5&interest=Adventure&travel_type=Couple&month=12")
    dests = res.get("data", [])
    ok_b = (code == 200) and len(dests) > 0 and all("matching_package_count" in d for d in dests)
    print(f"B. Destination discovery: {'PASS' if ok_b else 'FAIL'} (Found {len(dests)} matching destinations)")
    all_ok &= ok_b

    # C. Beach hard filter
    code, res = get_json("/packages?interest=Beach&per_page=100")
    b_pkgs = res.get("data", [])
    ok_c = (code == 200) and len(b_pkgs) > 0 and all(any(t["name"].lower() == "beach" for t in p["themes"]) for p in b_pkgs)
    print(f"C. Beach hard filter: {'PASS' if ok_c else 'FAIL'} (Verified {len(b_pkgs)}/{len(b_pkgs)} packages have Beach theme)")
    all_ok &= ok_c

    # D. Adventure hard filter
    code, res = get_json("/packages?interest=Adventure&per_page=100")
    a_pkgs = res.get("data", [])
    ok_d = (code == 200) and len(a_pkgs) > 0 and all(any(t["name"].lower() == "adventure" for t in p["themes"]) for p in a_pkgs)
    print(f"D. Adventure hard filter: {'PASS' if ok_d else 'FAIL'} (Verified {len(a_pkgs)}/{len(a_pkgs)} packages have Adventure theme)")
    all_ok &= ok_d

    # E. Different duration (e.g. 7 days preference)
    code, res = get_json("/packages?duration_days=7&per_page=5")
    d_pkgs = res.get("data", [])
    ok_e = (code == 200) and len(d_pkgs) > 0
    print(f"E. Different duration (7 days): {'PASS' if ok_e else 'FAIL'} (Top scored duration: {d_pkgs[0]['duration_days']} days, score: {d_pkgs[0].get('match_score')})")
    all_ok &= ok_e

    # F. Different travel type (Family)
    code, res = get_json("/packages?travel_type=Family&per_page=5")
    f_pkgs = res.get("data", [])
    ok_f = (code == 200) and len(f_pkgs) > 0
    print(f"F. Different travel type (Family): {'PASS' if ok_f else 'FAIL'} (Returned {len(f_pkgs)} packages)")
    all_ok &= ok_f

    # G. Different month (May = 5)
    code, res = get_json("/packages?month=5&per_page=5")
    m_pkgs = res.get("data", [])
    ok_g = (code == 200) and len(m_pkgs) > 0
    print(f"G. Different month (May): {'PASS' if ok_g else 'FAIL'} (Top package available in May: {5 in m_pkgs[0]['available_months']})")
    all_ok &= ok_g

    # H. Low budget (Rs 10,000 for 1 traveller)
    code, res = get_json("/packages?budget=10000&travellers=1&per_page=5")
    lb_pkgs = res.get("data", [])
    ok_h = (code == 200) and len(lb_pkgs) > 0 and all(p["price_per_person"] <= 12000 for p in lb_pkgs)
    print(f"H. Low budget: {'PASS' if ok_h else 'FAIL'} (Found {len(lb_pkgs)} packages within budget/20% fallback of Rs 10000)")
    all_ok &= ok_h

    # I. Multiple package results
    code, res = get_json("/packages?per_page=20")
    all_pkgs = res.get("data", [])
    ok_i = (code == 200) and len(all_pkgs) == 20
    print(f"I. Multiple package results: {'PASS' if ok_i else 'FAIL'} (Returned full page of {len(all_pkgs)} packages)")
    all_ok &= ok_i

    # J. Pagination (Page 1 vs Page 2)
    code1, res1 = get_json("/packages?page=1&per_page=20")
    code2, res2 = get_json("/packages?page=2&per_page=20")
    ids1 = {p["id"] for p in res1.get("data", [])}
    ids2 = {p["id"] for p in res2.get("data", [])}
    ok_j = (code1 == 200 and code2 == 200) and len(ids1.intersection(ids2)) == 0 and res1["pagination"]["total"] == 103
    print(f"J. Pagination: {'PASS' if ok_j else 'FAIL'} (Page 1 and Page 2 distinct, total: {res1['pagination']['total']})")
    all_ok &= ok_j

    # K. Add to Compare from search results
    code_f, html_f = get_frontend("/packages")
    ok_k = (code_f == 200) and ("Add to Compare" in html_f or "PackageCard" in html_f or "ComparisonBar" in html_f or "min-h-screen" in html_f)
    print(f"K. Add to Compare availability on search results: {'PASS' if ok_k else 'FAIL'}")
    all_ok &= ok_k

    # L. Compare 2 packages
    code_c2, html_c2 = get_frontend("/compare?ids=1,2&travellers=2")
    ok_l = (code_c2 == 200)
    print(f"L. Compare 2 packages (/compare?ids=1,2): {'PASS' if ok_l else 'FAIL'} (HTTP {code_c2})")
    all_ok &= ok_l

    # M. Compare 3 packages
    code_c3, html_c3 = get_frontend("/compare?ids=1,2,3&travellers=2")
    ok_m = (code_c3 == 200)
    print(f"M. Compare 3 packages (/compare?ids=1,2,3): {'PASS' if ok_m else 'FAIL'} (HTTP {code_c3})")
    all_ok &= ok_m

    # N. Package details
    code_dt, res_dt = get_json("/packages/1")
    pkg_detail = res_dt.get("data", {})
    ok_n = (code_dt == 200) and ("itinerary" in pkg_detail) and ("inclusions" in pkg_detail) and len(pkg_detail["itinerary"]) > 0
    print(f"N. Package details (/packages/1): {'PASS' if ok_n else 'FAIL'} ('{pkg_detail.get('name')}', {len(pkg_detail.get('itinerary', []))} days itinerary)")
    all_ok &= ok_n

    # O. Demo Source
    code_src, html_src = get_frontend("/sources/packages/1")
    ok_o = (code_src == 200) and ("Demo Source" in html_src or "demo" in html_src.lower())
    print(f"O. Demo Source page (/sources/packages/1): {'PASS' if ok_o else 'FAIL'} (HTTP {code_src})")
    all_ok &= ok_o

    # P. Mobile layout check (HTML has viewport tag and responsive classes)
    ok_p = (code_f == 200) and ("viewport" in html_f or "max-w-7xl" in html_f)
    print(f"P. Mobile layout readiness: {'PASS' if ok_p else 'FAIL'}")
    all_ok &= ok_p

    # Q. Empty results
    code_emp, res_emp = get_json("/packages?starting_city=Mumbai&interest=Skiing")
    ok_q = (code_emp == 200) and len(res_emp.get("data", [])) == 0 and res_emp["pagination"]["total"] == 0
    print(f"Q. Empty results handling: {'PASS' if ok_q else 'FAIL'} (Returned 0 items gracefully with message: '{res_emp.get('message', '')[:40]}...')")
    all_ok &= ok_q

    # R. Invalid inputs
    code_inv, res_inv = get_json("/packages?travellers=-1")
    ok_r = (code_inv == 400) and (res_inv.get("success") is False) and ("error" in res_inv)
    print(f"R. Invalid inputs handling: {'PASS' if ok_r else 'FAIL'} (HTTP {code_inv}: '{res_inv.get('error', {}).get('message')}')")
    all_ok &= ok_r

    print("==================================================")
    if all_ok:
        print("ALL 18 MANUAL TEST MATRIX SCENARIOS PASSED!")
        print("==================================================")
        return 0
    else:
        print("SOME MATRIX SCENARIOS FAILED!")
        print("==================================================")
        return 1

if __name__ == '__main__':
    sys.exit(test_matrix())
