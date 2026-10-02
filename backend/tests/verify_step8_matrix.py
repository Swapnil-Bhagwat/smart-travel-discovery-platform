"""
Step 8 Quality Verification Script: Search, Discovery, Recommendation, and Comparison.
"""

import sys
import os
import urllib.parse

# Ensure stdout handles UTF-8 (Rupee symbol, etc.) on Windows console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BACKEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from app import create_app

app = create_app()
client = app.test_client()

def test_search_matrix():
    print("=" * 75)
    print("1. SEARCH QUALITY TEST MATRIX (A through H)")
    print("=" * 75)

    matrix = [
        ('A', 'Mumbai', 'Beach'),
        ('B', 'Delhi', 'Adventure'),
        ('C', 'Pune', 'Nature'),
        ('D', 'Bangalore', 'Wildlife'),
        ('E', 'Hyderabad', 'Heritage'),
        ('F', 'Mumbai', 'Culture'),
        ('G', 'Delhi', 'Beach'),
        ('H', 'Pune', 'Adventure'),
    ]

    all_passed = True
    for code, city, interest in matrix:
        params = {
            'starting_city': city,
            'interest': interest,
            'budget': 100000,
            'travellers': 1,
        }
        qs = urllib.parse.urlencode(params)
        url = f"/api/v1/packages?{qs}"
        res = client.get(url)
        if res.status_code != 200:
            print(f"[{code}] {city} + {interest} FAILED: HTTP {res.status_code}")
            all_passed = False
            continue

        data = res.get_json().get('data', [])
        print(f"[{code}] {city} + {interest} -> {len(data)} matching package(s):")
        
        query_passed = True
        for p in data:
            if p['starting_city'].lower() != city.lower():
                print(f"   FAIL: Package {p['id']} starting city is {p['starting_city']}, expected {city}")
                query_passed = False
            if not p.get('is_active', True):
                print(f"   FAIL: Package {p['id']} is inactive!")
                query_passed = False
            p_themes = [t['slug'].lower() for t in p.get('themes', [])]
            if interest.lower() not in p_themes:
                print(f"   FAIL: Package {p['id']} themes {p_themes} missing {interest.lower()}")
                query_passed = False

        if not query_passed:
            all_passed = False
        else:
            for p in data[:3]:
                print(f"   * ID {p['id']}: '{p['name']}' ({p['destination']['name']}) | INR {p['price_per_person']} | {p['duration_days']}d")
            if len(data) > 3:
                print(f"   ... and {len(data) - 3} more")

    print("-" * 75)
    print("SEARCH TEST RESULT:", "PASSED" if all_passed else "FAILED")
    return all_passed


def test_discovery_matrix():
    print("\n" + "=" * 75)
    print("2. DISCOVERY QUALITY MATRIX")
    print("=" * 75)

    discovery_cases = [
        ('Mumbai', 'Beach'),
        ('Delhi', 'Adventure'),
        ('Pune', 'Nature'),
        ('Bangalore', 'Wildlife'),
        ('Hyderabad', 'Culture'),
    ]

    all_passed = True
    for city, interest in discovery_cases:
        params = {
            'starting_city': city,
            'interest': interest,
            'budget': 100000,
            'travellers': 1,
            'duration_days': 5,
            'travel_type': 'Couple',
            'month': 12,
        }
        qs = urllib.parse.urlencode(params)
        url = f"/api/v1/discover/destinations?{qs}"
        res = client.get(url)
        if res.status_code != 200:
            print(f"{city} + {interest} DISCOVERY FAILED: HTTP {res.status_code} - {res.get_json()}")
            all_passed = False
            continue

        dests = res.get_json().get('data', [])
        print(f"{city} + {interest} -> {len(dests)} destination(s) discovered:")

        disc_passed = True
        for d in dests:
            # Check destination integrity
            dest_name = d.get('destination_name')
            pkg_cnt = d.get('matching_package_count', 0)
            lowest = d.get('lowest_price_per_person')
            best = d.get('best_matching_package_name')
            reasons = d.get('match_reasons', [])
            mismatches = d.get('mismatches', [])
            print(f"   * {dest_name}: {pkg_cnt} matching package(s) | Lowest INR {lowest} | Best: '{best}'")
            if reasons:
                print(f"     Reasons: {reasons[:2]}")
            if mismatches:
                print(f"     Mismatches: {mismatches[:2]}")

            if pkg_cnt <= 0:
                print(f"   FAIL: Destination {dest_name} returned with 0 matching packages")
                disc_passed = False

            # Verify that non-beach destinations like Manali/Jaipur don't appear for Beach
            if interest.lower() == 'beach' and dest_name in ['Manali', 'Jaipur', 'Leh', 'Varanasi', 'Amritsar', 'Jim Corbett']:
                print(f"   FAIL: Non-beach destination {dest_name} appeared for Beach search!")
                disc_passed = False

        if not disc_passed:
            all_passed = False

    print("-" * 75)
    print("DISCOVERY TEST RESULT:", "PASSED" if all_passed else "FAILED")
    return all_passed


def test_recommendations_and_comparison():
    print("\n" + "=" * 75)
    print("3. RECOMMENDATION & COMPARISON QUALITY")
    print("=" * 75)

    params = {
        'starting_city': 'Mumbai',
        'interest': 'Beach',
        'budget': 60000,
        'travellers': 2,
        'duration_days': 4,
        'travel_type': 'Couple',
        'month': 11,
    }
    qs = urllib.parse.urlencode(params)
    url = f"/api/v1/recommendations/packages?{qs}"
    res = client.get(url)
    all_passed = True
    if res.status_code != 200:
        print(f"Recommendations FAILED: HTTP {res.status_code} - {res.get_json()}")
        all_passed = False
    else:
        items = res.get_json().get('data', [])
        print(f"Recommendations returned {len(items)} package(s):")
        for it in items[:4]:
            name = it.get('name')
            score = it.get('match_score')
            city = it.get('starting_city')
            reasons = it.get('match_reasons', [])
            mismatches = it.get('mismatches', [])
            print(f"   * {name} | Score: {score}/100 | City: {city}")
            if reasons:
                print(f"     Reasons: {reasons}")
            if mismatches:
                print(f"     Mismatches: {mismatches}")

        if len(items) >= 2:
            print(f"\nPackage Comparison Readiness: {len(items)} matching packages available for side-by-side comparison.")
        else:
            print("FAIL: Less than 2 packages returned for comparison test.")
            all_passed = False

    print("-" * 75)
    print("RECOMMENDATION TEST RESULT:", "PASSED" if all_passed else "FAILED")
    return all_passed


if __name__ == '__main__':
    s_ok = test_search_matrix()
    d_ok = test_discovery_matrix()
    r_ok = test_recommendations_and_comparison()

    if s_ok and d_ok and r_ok:
        print("\nALL STEP 8 QUALITY TESTS PASSED PERFECTLY!")
        sys.exit(0)
    else:
        print("\nSOME TESTS FAILED!")
        sys.exit(1)
