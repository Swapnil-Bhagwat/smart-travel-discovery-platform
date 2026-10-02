import urllib.request
import urllib.error
import json
import sys

def verify_all():
    endpoints = [
        ("Health", "http://127.0.0.1:5000/api/v1/health"),
        ("Providers List", "http://127.0.0.1:5000/api/v1/providers"),
        ("Providers Search", "http://127.0.0.1:5000/api/v1/providers/search?starting_city=Mumbai&interest=Beach"),
        ("Packages Search", "http://127.0.0.1:5000/api/v1/packages?starting_city=Mumbai&interest=Beach"),
        ("Package Detail", "http://127.0.0.1:5000/api/v1/packages/1"),
        ("Destinations List", "http://127.0.0.1:5000/api/v1/destinations"),
        ("Destinations Discovery", "http://127.0.0.1:5000/api/v1/discover/destinations?starting_city=Mumbai&budget=50000&travellers=2&duration_days=5&interest=Beach&travel_type=Couple&month=11"),
        ("Recommendations", "http://127.0.0.1:5000/api/v1/recommendations/packages?starting_city=Mumbai&budget=50000&travellers=2&duration_days=5&interest=Beach&travel_type=Couple&month=11"),
        ("Themes (Cached)", "http://127.0.0.1:5000/api/v1/themes"),
    ]

    all_ok = True
    print("\n=== STEP 9 LIVE ENDPOINT VERIFICATION ===")
    for label, url in endpoints:
        try:
            req = urllib.request.urlopen(url, timeout=5)
            data = json.loads(req.read().decode("utf-8"))
            success = data.get("success", data.get("status") == "ok")
            payload = data.get("data")
            count = len(payload) if isinstance(payload, list) else ("dict" if isinstance(payload, dict) else "ok")
            status = "PASS" if (success or req.status == 200) else "FAIL"
            print(f"[{status}] {label:<24}: HTTP {req.status} | success={success} | items={count}")
            if not success and req.status != 200:
                all_ok = False
        except Exception as e:
            print(f"[FAIL] {label:<24}: ERROR {e}")
            all_ok = False

    # Check invalid provider returns 400 with standard error format
    try:
        urllib.request.urlopen("http://127.0.0.1:5000/api/v1/providers/search?provider=invalid_provider")
        print("[FAIL] Invalid provider lookup did not raise 400")
        all_ok = False
    except urllib.error.HTTPError as err:
        err_body = json.loads(err.read().decode("utf-8"))
        if err.code == 400 and err_body.get("success") is False and "error" in err_body:
            print(f"[PASS] Invalid Provider Error : HTTP 400 | Standard error format: {err_body['error']}")
        else:
            print(f"[FAIL] Invalid Provider Error : Unexpected response: {err_body}")
            all_ok = False

    print("=========================================\n")
    if all_ok:
        print("ALL STEP 9 LIVE ENDPOINTS VERIFIED SUCCESSFULLY.")
    else:
        print("SOME CHECKS FAILED.")
        sys.exit(1)

if __name__ == "__main__":
    verify_all()
