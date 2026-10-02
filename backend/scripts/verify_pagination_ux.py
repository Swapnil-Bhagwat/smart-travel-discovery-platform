import urllib.request
import json
import sys

def verify_pagination():
    print("\n=== VERIFYING PACKAGE RESULTS PAGINATION API ===")
    all_ok = True

    # Test 1: Page 1 without filters
    url_p1 = "http://127.0.0.1:5000/api/v1/packages?page=1&per_page=20"
    res1 = urllib.request.urlopen(url_p1)
    d1 = json.loads(res1.read().decode('utf-8'))
    p1 = d1['pagination']
    item_count1 = len(d1['data'])
    start1 = (p1['page'] - 1) * p1['per_page'] + 1
    end1 = min(p1['page'] * p1['per_page'], p1['total'])
    msg1 = f"Showing {start1}–{end1} of {p1['total']} packages"
    print(f"Test 1: Page 1 | Items: {item_count1} | {msg1} | Total pages: {p1['pages']}")
    if item_count1 == 20 and p1['page'] == 1 and p1['total'] == 103 and p1['pages'] == 6:
        print("[PASS] Test 1: Page 1 metadata and item count correct.")
    else:
        print("[FAIL] Test 1 failed.")
        all_ok = False

    # Test 2: Page 2 without filters
    url_p2 = "http://127.0.0.1:5000/api/v1/packages?page=2&per_page=20"
    res2 = urllib.request.urlopen(url_p2)
    d2 = json.loads(res2.read().decode('utf-8'))
    p2 = d2['pagination']
    item_count2 = len(d2['data'])
    start2 = (p2['page'] - 1) * p2['per_page'] + 1
    end2 = min(p2['page'] * p2['per_page'], p2['total'])
    msg2 = f"Showing {start2}–{end2} of {p2['total']} packages"
    print(f"Test 2: Page 2 | Items: {item_count2} | {msg2} | Total pages: {p2['pages']}")
    if item_count2 == 20 and p2['page'] == 2 and p2['total'] == 103:
        print("[PASS] Test 2: Page 2 metadata and item count correct.")
    else:
        print("[FAIL] Test 2 failed.")
        all_ok = False

    # Test 3: Page 6 (last page)
    url_p6 = "http://127.0.0.1:5000/api/v1/packages?page=6&per_page=20"
    res6 = urllib.request.urlopen(url_p6)
    d6 = json.loads(res6.read().decode('utf-8'))
    p6 = d6['pagination']
    item_count6 = len(d6['data'])
    start6 = (p6['page'] - 1) * p6['per_page'] + 1
    end6 = min(p6['page'] * p6['per_page'], p6['total'])
    msg6 = f"Showing {start6}–{end6} of {p6['total']} packages"
    print(f"Test 3: Page 6 | Items: {item_count6} | {msg6} | Total pages: {p6['pages']}")
    if item_count6 == 3 and p6['page'] == 6 and p6['total'] == 103:
        print("[PASS] Test 3: Last page metadata and item count correct.")
    else:
        print("[FAIL] Test 3 failed.")
        all_ok = False

    # Test 4: Filtered search (Mumbai + Beach)
    url_filtered = "http://127.0.0.1:5000/api/v1/packages?starting_city=Mumbai&interest=Beach&page=1&per_page=20"
    res_f = urllib.request.urlopen(url_filtered)
    df = json.loads(res_f.read().decode('utf-8'))
    pf = df['pagination']
    item_count_f = len(df['data'])
    start_f = (pf['page'] - 1) * pf['per_page'] + 1
    end_f = min(pf['page'] * pf['per_page'], pf['total'])
    msg_f = f"Showing {start_f}–{end_f} of {pf['total']} packages"
    print(f"Test 4: Filtered search (Mumbai + Beach) | Items: {item_count_f} | {msg_f} | Total pages: {pf['pages']}")
    if item_count_f == 6 and pf['total'] == 6 and pf['pages'] == 1:
        print("[PASS] Test 4: Filtered search correctly applies to filtered count (6 of 6).")
    else:
        print("[FAIL] Test 4 failed.")
        all_ok = False

    # Test 5: Verify page 1 and page 2 return distinct packages
    ids_p1 = {pkg['id'] for pkg in d1['data']}
    ids_p2 = {pkg['id'] for pkg in d2['data']}
    overlap = ids_p1.intersection(ids_p2)
    print(f"Test 5: Overlap between Page 1 and Page 2: {len(overlap)} items")
    if len(overlap) == 0:
        print("[PASS] Test 5: Page 1 and Page 2 return strictly distinct packages.")
    else:
        print(f"[FAIL] Test 5 failed: Overlapping IDs found: {overlap}")
        all_ok = False

    print("=================================================\n")
    if not all_ok:
        sys.exit(1)
    print("ALL PAGINATION API VERIFICATION CHECKS PASSED!")

if __name__ == '__main__':
    verify_pagination()
