import requests
import json
print("Script started")

BASE_URL = "http://localhost:8000/api"

def test_compliance():
    print("Testing Compliance API...")
    try:
        res = requests.get(f"{BASE_URL}/compliance/overview")
        if res.status_code == 200:
            print("✅ Get Overview: Success")
            print(json.dumps(res.json(), indent=2))
        else:
            print(f"❌ Get Overview: Failed ({res.status_code})")

        res = requests.get(f"{BASE_URL}/compliance/controls")
        if res.status_code == 200:
            print(f"✅ Get Controls: Success ({len(res.json())} controls)")
        else:
            print(f"❌ Get Controls: Failed ({res.status_code})")
            
        res = requests.post(f"{BASE_URL}/compliance/reports/ISO 27001")
        if res.status_code == 200:
            print("✅ Generate Report: Success")
        else:
            print(f"❌ Generate Report: Failed ({res.status_code})")
            
    except Exception as e:
        print(f"❌ Compliance API Error: {e}")

def test_forensics():
    print("\nTesting Forensics API...")
    try:
        # Case Management
        res = requests.get(f"{BASE_URL}/forensics/cases")
        if res.status_code == 200:
            print(f"✅ Get Cases: Success ({len(res.json())} cases)")
            first_case_id = res.json()[0]["id"]
        else:
            print(f"❌ Get Cases: Failed ({res.status_code})")
            return

        res = requests.get(f"{BASE_URL}/forensics/cases/{first_case_id}")
        if res.status_code == 200:
            print("✅ Get Case Details: Success")
        else:
            print(f"❌ Get Case Details: Failed ({res.status_code})")

        # Create Case
        new_case = {
            "title": "Test Incident",
            "description": "Created by test script",
            "severity": "low",
            "analyst": "Tester"
        }
        res = requests.post(f"{BASE_URL}/forensics/cases", json=new_case)
        if res.status_code == 200:
            print(f"✅ Create Case: Success (ID: {res.json()['id']})")
            new_case_id = res.json()['id']
        else:
            print(f"❌ Create Case: Failed ({res.status_code})")
            return

        # Add Evidence
        evidence = {
            "name": "suspicious.log",
            "type": "log",
            "content": "malicious content here",
            "custodian": "Tester"
        }
        res = requests.post(f"{BASE_URL}/forensics/cases/{new_case_id}/evidence", json=evidence)
        if res.status_code == 200:
            print("✅ Add Evidence: Success")
        else:
            print(f"❌ Add Evidence: Failed ({res.status_code})")

    except Exception as e:
        print(f"❌ Forensics API Error: {e}")

if __name__ == "__main__":
    test_compliance()
    test_forensics()
