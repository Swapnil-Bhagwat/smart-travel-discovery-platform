"""
Step 10 Comprehensive Platform Audit & Verification Script
Smart Travel Discovery and Comparison Platform
"""

import sys
import os
import json
import urllib.request
import urllib.error
from decimal import Decimal

BASE_URL = "http://127.0.0.1:5000/api/v1"

def check(condition, message):
    if condition:
        print(f"  [PASS] {message}")
        return True
    else:
        print(f"  [FAIL] {message}")
        return False

def http_get(endpoint):
    url = f"{BASE_URL}{endpoint}"
    req = urllib.request.Request(url, headers={"User-Agent": "Step10Audit/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status, json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8')
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, {"raw": body}
    except Exception as e:
        return 0, {"error": str(e)}

def run_audit():
    all_passed = True
    print("\n==================================================")
    print("STEP 10 — COMPREHENSIVE PLATFORM AUDIT")
    print("==================================================")

    # --------------------------------------------------
    # 1. DATABASE & INVENTORY AUDIT
    # --------------------------------------------------
    print("\n--- 1. DATABASE & INVENTORY AUDIT ---")
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from app import create_app
    from app.models import Destination, Operator, Theme, Package, PackageItinerary, PackageInclusion, PackageExclusion
    app = create_app()

    with app.app_context():
        dest_count = Destination.query.count()
        op_count = Operator.query.count()
        theme_count = Theme.query.count()
        pkg_total = Package.query.count()
        pkg_active = Package.query.filter_by(is_active=True).count()
        pkg_inactive = Package.query.filter_by(is_active=False).count()

        all_passed &= check(dest_count == 25, f"Destinations count == 25 (Found: {dest_count})")
        all_passed &= check(op_count == 10, f"Operators count == 10 (Found: {op_count})")
        all_passed &= check(theme_count == 10, f"Themes count == 10 (Found: {theme_count})")
        all_passed &= check(pkg_total == 107, f"Total packages count == 107 (Found: {pkg_total})")
        all_passed &= check(pkg_active == 103, f"Active packages count == 103 (Found: {pkg_active})")
        all_passed &= check(pkg_inactive == 4, f"Inactive packages count == 4 (Found: {pkg_inactive})")

        # Verify child records on all active packages
        active_pkgs = Package.query.filter_by(is_active=True).all()
        invalid_itinerary = [p.id for p in active_pkgs if len(p.itineraries) < p.duration_days]
        invalid_inclusions = [p.id for p in active_pkgs if len(p.inclusions) == 0]
        invalid_exclusions = [p.id for p in active_pkgs if len(p.exclusions) == 0]
        invalid_themes = [p.id for p in active_pkgs if len(p.themes) == 0]
        invalid_types = [p.id for p in active_pkgs if len(p.travel_types) == 0]
        invalid_months = [p.id for p in active_pkgs if len(p.availability_months) == 0]
        missing_dest = [p.id for p in active_pkgs if p.destination is None]
        missing_op = [p.id for p in active_pkgs if p.operator is None]

        all_passed &= check(len(invalid_itinerary) == 0, f"All active packages have complete itineraries ({len(active_pkgs)} checked)")
        all_passed &= check(len(invalid_inclusions) == 0, f"All active packages have inclusions ({len(active_pkgs)} checked)")
        all_passed &= check(len(invalid_exclusions) == 0, f"All active packages have exclusions ({len(active_pkgs)} checked)")
        all_passed &= check(len(invalid_themes) == 0, f"All active packages have themes ({len(active_pkgs)} checked)")
        all_passed &= check(len(invalid_types) == 0, f"All active packages have travel types ({len(active_pkgs)} checked)")
        all_passed &= check(len(invalid_months) == 0, f"All active packages have availability months ({len(active_pkgs)} checked)")
        all_passed &= check(len(missing_dest) == 0, "No packages have missing destination relationship")
        all_passed &= check(len(missing_op) == 0, "No packages have missing operator relationship")

    # --------------------------------------------------
    # 2. ALL 14 API ENDPOINTS AUDIT
    # --------------------------------------------------
    print("\n--- 2. ALL 14 API ENDPOINTS AUDIT ---")
    endpoints_to_test = [
        ("Health", "/health", 200, True),
        ("DB Health", "/health/db", 200, True),
        ("Destinations", "/destinations", 200, True),
        ("Destination by ID", "/destinations/1", 200, True),
        ("Operators", "/operators", 200, True),
        ("Operator by ID", "/operators/1", 200, True),
        ("Themes", "/themes", 200, True),
        ("Theme by ID", "/themes/1", 200, True),
        ("Packages List", "/packages", 200, True),
        ("Package Detail", "/packages/1", 200, True),
        ("Discover Destinations", "/discover/destinations?starting_city=Mumbai&budget=50000&travellers=2&duration_days=5&interest=Beach&travel_type=Couple&month=11", 200, True),
        ("Recommendations", "/recommendations/packages?starting_city=Mumbai&budget=50000&travellers=2&duration_days=5&interest=Beach&travel_type=Couple&month=11", 200, True),
        ("Providers List", "/providers", 200, True),
        ("Providers Search", "/providers/search?starting_city=Mumbai&interest=Beach", 200, True),
    ]

    for label, ep, exp_code, exp_success in endpoints_to_test:
        code, body = http_get(ep)
        has_success = body.get("success") == exp_success
        has_data = "data" in body or body.get("status") == "ok"
        passed = (code == exp_code) and has_success and has_data
        all_passed &= check(passed, f"{label} ({ep.split('?')[0]}): HTTP {code} | success={body.get('success')}")

    # Test Error Formats (404 and 400)
    print("\n--- Error Response Formats ---")
    code_404, body_404 = http_get("/packages/999999")
    all_passed &= check(code_404 == 404 and body_404.get("success") is False and "error" in body_404 and "message" in body_404["error"],
                        f"404 Error follows standard format: {body_404.get('error')}")

    code_400, body_400 = http_get("/packages?travellers=-5")
    all_passed &= check(code_400 == 400 and body_400.get("success") is False and "error" in body_400 and "message" in body_400["error"],
                        f"400 Error follows standard format: {body_400.get('error')}")

    # --------------------------------------------------
    # 3. SEARCH & HARD/SOFT FILTERS AUDIT
    # --------------------------------------------------
    print("\n--- 3. SEARCH & HARD/SOFT FILTERS AUDIT ---")
    # A. Hard Interest Filter: Beach -> Only Beach packages
    code_b, body_b = http_get("/packages?interest=Beach&per_page=100")
    b_pkgs = body_b.get("data", [])
    beach_all_match = all(any(t["name"].lower() == "beach" or t["slug"].lower() == "beach" for t in p["themes"]) for p in b_pkgs)
    all_passed &= check(beach_all_match and len(b_pkgs) > 0, f"Hard filter Beach returns only Beach packages ({len(b_pkgs)} packages)")

    # B. Hard Interest Filter: Adventure -> Only Adventure packages
    code_a, body_a = http_get("/packages?interest=Adventure&per_page=100")
    a_pkgs = body_a.get("data", [])
    adv_all_match = all(any(t["name"].lower() == "adventure" or t["slug"].lower() == "adventure" for t in p["themes"]) for p in a_pkgs)
    all_passed &= check(adv_all_match and len(a_pkgs) > 0, f"Hard filter Adventure returns only Adventure packages ({len(a_pkgs)} packages)")

    # C. Hard Starting City Filter: Mumbai departures only
    code_m, body_m = http_get("/packages?starting_city=Mumbai&per_page=100")
    m_pkgs = body_m.get("data", [])
    mumbai_all_match = all(p["starting_city"].lower() == "mumbai" for p in m_pkgs)
    all_passed &= check(mumbai_all_match and len(m_pkgs) > 0, f"Hard filter Starting City returns only Mumbai departures ({len(m_pkgs)} packages)")

    # D. Inactive packages excluded
    all_passed &= check(all(p["id"] not in [104, 105, 106, 107] for p in m_pkgs), "Inactive packages excluded from search results")

    # E. Over-budget exclusion (>20% over budget excluded)
    code_low_b, body_low_b = http_get("/packages?budget=5000&travellers=1")
    low_pkgs = body_low_b.get("data", [])
    all_passed &= check(all(p["price_per_person"] <= 6000 for p in low_pkgs), f"Over-budget logic respects 20% limit (budget=5000 max price <= 6000)")

    # --------------------------------------------------
    # 4. RECOMMENDATION & EXPLANATION AUDIT
    # --------------------------------------------------
    print("\n--- 4. RECOMMENDATION & EXPLANATION AUDIT ---")
    rec_url = "/recommendations/packages?starting_city=Mumbai&budget=50000&travellers=2&duration_days=5&interest=Beach&travel_type=Couple&month=11"
    code_rec, body_rec = http_get(rec_url)
    rec_pkgs = body_rec.get("data", [])
    all_passed &= check(len(rec_pkgs) > 0, f"Recommendations returned {len(rec_pkgs)} packages")
    all_passed &= check(all(0 <= p.get("match_score", 0) <= 100 for p in rec_pkgs), "All recommendation scores are between 0 and 100")
    all_passed &= check(all("match_reasons" in p for p in rec_pkgs), "All recommended packages include explainable match_reasons")

    # Check for forbidden superlative words in match reasons
    forbidden_words = ["best", "winner", "most popular", "perfect for you"]
    reasons_clean = True
    for p in rec_pkgs:
        for r in (p.get("match_reasons") or []):
            for fw in forbidden_words:
                if fw in r.lower():
                    reasons_clean = False
                    print(f"    [WARN] Forbidden term '{fw}' found in reason: '{r}'")
    all_passed &= check(reasons_clean, "No unsupported superlative claims ('best', 'winner', 'most popular', 'perfect for you') in match reasons")

    # --------------------------------------------------
    # 5. PAGINATION AUDIT
    # --------------------------------------------------
    print("\n--- 5. PAGINATION AUDIT ---")
    _, p1 = http_get("/packages?page=1&per_page=20")
    _, p2 = http_get("/packages?page=2&per_page=20")
    _, p6 = http_get("/packages?page=6&per_page=20")

    all_passed &= check(len(p1["data"]) == 20 and p1["pagination"]["page"] == 1 and p1["pagination"]["total"] == 103,
                        "Page 1 returns 20 items, total 103, page 1")
    all_passed &= check(len(p2["data"]) == 20 and p2["pagination"]["page"] == 2 and p2["pagination"]["total"] == 103,
                        "Page 2 returns 20 items, total 103, page 2")
    all_passed &= check(len(p6["data"]) == 3 and p6["pagination"]["page"] == 6 and p6["pagination"]["total"] == 103,
                        "Page 6 (last page) returns 3 items, total 103")

    p1_ids = {p["id"] for p in p1["data"]}
    p2_ids = {p["id"] for p in p2["data"]}
    all_passed &= check(len(p1_ids.intersection(p2_ids)) == 0, "Page 1 and Page 2 contain non-overlapping packages")

    # Filtered pagination with <20 results
    _, pf = http_get("/packages?starting_city=Mumbai&interest=Beach&page=1&per_page=20")
    all_passed &= check(len(pf["data"]) == 6 and pf["pagination"]["total"] == 6 and pf["pagination"]["pages"] == 1,
                        f"Filtered search correctly paginated: 6 items of 6 total, 1 page")

    # --------------------------------------------------
    # 6. PROVIDER-READY ARCHITECTURE AUDIT
    # --------------------------------------------------
    print("\n--- 6. PROVIDER-READY ARCHITECTURE AUDIT ---")
    code_prv, body_prv = http_get("/providers")
    providers = body_prv.get("data", [])
    demo_p = next((p for p in providers if p["provider"] == "demo"), None)
    viator_p = next((p for p in providers if p["provider"] == "viator"), None)
    booking_p = next((p for p in providers if p["provider"] == "booking"), None)

    all_passed &= check(demo_p is not None and demo_p["enabled"] is True and demo_p["status"] == "healthy",
                        f"Demo provider registered, enabled, and healthy ({demo_p.get('message')})")
    all_passed &= check(viator_p is not None and viator_p["enabled"] is False and viator_p["status"] == "disabled",
                        "Viator live provider adapter registered and strictly disabled")
    all_passed &= check(booking_p is not None and booking_p["enabled"] is False and booking_p["status"] == "disabled",
                        "Booking live provider adapter registered and strictly disabled")

    # --------------------------------------------------
    # 7. SECURITY & CREDENTIALS AUDIT
    # --------------------------------------------------
    print("\n--- 7. SECURITY & CREDENTIALS AUDIT ---")
    from app.config import Config
    all_passed &= check(Config.MYSQL_USER == "travel_app", f"MySQL configured with dedicated user '{Config.MYSQL_USER}', not root")
    all_passed &= check(not Config.VIATOR_ENABLED, "Live provider VIATOR_ENABLED is False")
    all_passed &= check(not Config.BOOKING_ENABLED, "Live provider BOOKING_ENABLED is False")
    all_passed &= check(Config.VIATOR_API_KEY == "", "No hardcoded VIATOR_API_KEY")
    all_passed &= check(Config.BOOKING_API_KEY == "", "No hardcoded BOOKING_API_KEY")

    # Verify .env is in .gitignore
    root_gitignore = os.path.join(os.path.dirname(__file__), '..', '..', '.gitignore')
    with open(root_gitignore, 'r') as f:
        git_content = f.read()
    all_passed &= check(".env" in git_content, ".env is protected in root .gitignore")

    print("\n==================================================")
    if all_passed:
        print("ALL STEP 10 COMPREHENSIVE AUDIT CHECKS PASSED!")
        print("==================================================")
        return 0
    else:
        print("SOME AUDIT CHECKS FAILED!")
        print("==================================================")
        return 1

if __name__ == '__main__':
    sys.exit(run_audit())
