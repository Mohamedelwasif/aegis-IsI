import requests
import time
import json

BASE_URL = "http://localhost:8000/api"

def test_digital_twin():
    print("Testing Digital Twin API...")
    # Get Topology
    res = requests.get(f"{BASE_URL}/simulation/topology")
    if res.status_code == 200:
        print("✅ Get Topology: Success")
    else:
        print(f"❌ Get Topology: Failed ({res.status_code})")

    # Run Simulation
    res = requests.post(f"{BASE_URL}/simulation/simulate/avaya_compromise")
    if res.status_code == 200:
        print("✅ Run Simulation (Avaya): Success")
        data = res.json()
        if len(data.get("log", [])) > 0:
            print("✅ Simulation Log generated")
    else:
        print(f"❌ Run Simulation: Failed ({res.status_code})")

    # Reset
    res = requests.post(f"{BASE_URL}/simulation/reset")
    if res.status_code == 200:
        print("✅ Reset Simulation: Success")
    else:
        print(f"❌ Reset Simulation: Failed ({res.status_code})")

def test_cti():
    print("\nTesting CTI API...")
    # Get Feeds
    res = requests.get(f"{BASE_URL}/cti/feeds")
    if res.status_code == 200:
        print("✅ Get Feeds: Success")
    else:
        print(f"❌ Get Feeds: Failed ({res.status_code})")

    # Check IOC
    res = requests.get(f"{BASE_URL}/cti/check/185.100.1.1")
    if res.status_code == 200:
        data = res.json()
        if data.get("found"):
            print("✅ Check IOC (Found): Success")
        else:
            print("❌ Check IOC: Expected found but got not found")
    else:
        print(f"❌ Check IOC: Failed ({res.status_code})")

def test_red_team():
    print("\nTesting Red Team API...")
    # Create Campaign
    campaign = {
        "name": "Test Campaign",
        "description": "Integration Test",
        "techniques": ["T1071", "T1021"]
    }
    res = requests.post(f"{BASE_URL}/red_team/campaigns", json=campaign)
    if res.status_code == 200:
        print("✅ Create Campaign: Success")
        campaign_id = res.json()["id"]
        
        # Run Campaign
        res = requests.post(f"{BASE_URL}/red_team/campaigns/{campaign_id}/run")
        if res.status_code == 200:
            print("✅ Run Campaign: Success")
            data = res.json()
            if data["status"] == "completed":
                print("✅ Campaign Execution Completed")
        else:
            print(f"❌ Run Campaign: Failed ({res.status_code})")
    else:
        print(f"❌ Create Campaign: Failed ({res.status_code})")

if __name__ == "__main__":
    try:
        test_digital_twin()
        test_cti()
        test_red_team()
    except Exception as e:
        print(f"❌ Test Script Error: {e}")
