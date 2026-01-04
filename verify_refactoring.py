import requests
import sys

BASE_URL = "http://localhost:8000/api"

def check_endpoint(name, url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"✅ {name}: OK - {response.json()}")
        else:
            print(f"❌ {name}: Failed - {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ {name}: Error - {e}")

if __name__ == "__main__":
    print("Verifying AEGIS Backend Refactoring...")
    check_endpoint("Dashboard", f"{BASE_URL}/dashboard/overview")
    check_endpoint("Traffic", f"{BASE_URL}/traffic/flows")
    check_endpoint("Entities", f"{BASE_URL}/entities")
    check_endpoint("Alerts", f"{BASE_URL}/alerts")
