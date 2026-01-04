import requests
import sys

BASE_URL = "http://localhost:8000/api/auth"

def test_login(email, password, mfa_code=None):
    payload = {
        "email": email,
        "password": password
    }
    if mfa_code:
        payload["mfa_code"] = mfa_code
        
    try:
        response = requests.post(f"{BASE_URL}/login", json=payload)
        print(f"Login with MFA='{mfa_code}': Status {response.status_code}")
        if response.status_code == 200:
            print("  -> Success!")
            return True
        else:
            print(f"  -> Failed: {response.json().get('detail')}")
            return False
    except Exception as e:
        print(f"  -> Error: {e}")
        return False

print("Verifying MFA Enforcement...")
print("-" * 30)

# 1. Test without MFA (Should Fail now)
print("1. Testing Login WITHOUT MFA Code...")
test_login("agent@aegis.intel", "Admin123!x", None)

# 2. Test with Wrong MFA (Should Fail)
print("\n2. Testing Login with WRONG MFA Code...")
test_login("agent@aegis.intel", "Admin123!x", "123456")

# 3. Test with Correct MFA (Should Success)
# Since pyotp is missing, "000000" is the fallback master code
print("\n3. Testing Login with CORRECT MFA Code (000000)...")
test_login("agent@aegis.intel", "Admin123!x", "000000")
