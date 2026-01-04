import requests
import json
import time

BASE_URL = "http://127.0.0.1:8000/api/data-offload"

def test_happy_path():
    print("\n--- Testing Happy Path ---")
    # 1. Trigger
    print("Triggering offload...")
    res = requests.post(f"{BASE_URL}/trigger")
    print(f"Trigger Response: {res.status_code}")
    data = res.json()
    print(f"Status: {data['status']}")
    
    # Wait for transfer (mock delay)
    time.sleep(2)
    
    # 2. Check Status
    res = requests.get(f"{BASE_URL}/status")
    data = res.json()
    print(f"Current Status: {data['status']}")
    
    if data['status'] == "WAITING_FOR_ACK":
        print("System is waiting for ACK. Good.")
        
        # 3. Send ACK
        print("Sending ACK...")
        res = requests.post(f"{BASE_URL}/ack", json={"signature": "valid-sig"})
        data = res.json()
        print(f"ACK Response Status: {data['status']}")
        print(f"ACK Status: {data['ack_status']}")
        print(f"Secure Wipe: {data['secure_wipe_status']}")
    else:
        print("Unexpected status.")

def test_failure_no_ack():
    print("\n--- Testing Failure Scenario: NO ACK ---")
    # 1. Simulate Failure
    res = requests.post(f"{BASE_URL}/simulate-failure", json={"scenario": "NO_ACK"})
    data = res.json()
    print(f"Status: {data['status']}")
    # In simulation, it might jump to FAILED immediately or wait. 
    # My simulate_failure_scenario implementation for NO_ACK sets it to WAITING_FOR_ACK then FAILED.
    # Let's check the logs.
    logs = data.get('logs', [])
    if logs:
        print(f"Last Log: {logs[-1]['message']}")

if __name__ == "__main__":
    try:
        test_happy_path()
        test_failure_no_ack()
    except Exception as e:
        print(f"Test Failed: {e}")
