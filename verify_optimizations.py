import requests
import time
import sys

BASE_URL = "http://localhost:8000/api"

def check_endpoint(endpoint):
    url = f"{BASE_URL}{endpoint}"
    start = time.time()
    try:
        response = requests.get(url, timeout=2)
        elapsed = (time.time() - start) * 1000
        print(f"[{response.status_code}] {endpoint} - {elapsed:.2f}ms")
        if response.status_code != 200:
            print(f"   Error: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"[FAIL] {endpoint} - {e}")
        return False

print("Verifying Optimized Endpoints...")
print("-" * 40)

# Check Settings Endpoints (Critical for Trust Matrix)
success = True
success &= check_endpoint("/settings/integrations/cards")
success &= check_endpoint("/settings/auth")
success &= check_endpoint("/settings/protocol-intelligence")

# Check Auth Endpoint (Critical for Login)
# Just a GET to /me to see if it's there (might fail 401 but that's a response)
# Actually /me requires auth, so checking 401 is success for reachability
try:
    url = f"{BASE_URL}/auth/me"
    start = time.time()
    response = requests.get(url, timeout=2)
    elapsed = (time.time() - start) * 1000
    print(f"[{response.status_code}] /auth/me - {elapsed:.2f}ms (Expected 401)")
except Exception as e:
    print(f"[FAIL] /auth/me - {e}")

print("-" * 40)
if success:
    print("Verification Passed: Endpoints are reachable and responding.")
else:
    print("Verification Failed: Some endpoints are not working.")
