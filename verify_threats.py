import requests
import json
import time

BASE_URL = "http://localhost:8000/api"

def test_uc01_lateral_movement():
    print("\n🔴 Testing UC-01: Lateral Movement...")
    payload = {
        "src_vlan": 10,
        "dst_vlan": 20,
        "volume_bytes": 150000000 # 150MB > 100MB threshold
    }
    try:
        response = requests.post(f"{BASE_URL}/threats/detect/lateral-movement", json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")

def test_uc02_sip_brute_force():
    print("\n🔴 Testing UC-02: SIP Brute Force...")
    payload = {
        "logs": [
            {"method": "REGISTER", "status_code": 403, "src_ip": "10.0.0.50"} for _ in range(60)
        ]
    }
    try:
        response = requests.post(f"{BASE_URL}/threats/detect/sip-brute-force", json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")

def test_uc03_dns_tunneling():
    print("\n🔴 Testing UC-03: DNS Tunneling...")
    payload = {
        "queries": [
            "google.com",
            "a" * 60 + ".com", # Long query
            "ab83291038290182390182930128390128390128390.exfiltration.com" # High entropy
        ]
    }
    try:
        response = requests.post(f"{BASE_URL}/threats/detect/dns-tunneling", json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")

def test_uc04_rogue_iot():
    print("\n🔴 Testing UC-04: Rogue IoT Device...")
    payload = {
        "device_profile": {"id": "iot-temp-01", "allowed_protocols": ["MQTT"]},
        "traffic_log": [
            {"direction": "outbound", "protocol": "SSH", "dst_port": 22}, # Unexpected SSH
            {"direction": "outbound", "protocol": "MQTT", "dst_port": 1883}
        ]
    }
    try:
        response = requests.post(f"{BASE_URL}/threats/detect/rogue-iot", json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")

def test_uc05_insider_threat():
    print("\n🔴 Testing UC-05: Insider Threat...")
    payload = {
        "user_activity": {
            "user": "jdoe",
            "timestamp": "2023-10-27T03:00:00", # 3 AM
            "protocol": "FTP" # Deviation from HTTPS/Outlook
        }
    }
    try:
        response = requests.post(f"{BASE_URL}/threats/detect/insider-threat", json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")

def test_response_engine():
    print("\n⚔️ Testing Automated Response Engine...")
    payload = {
        "action": "ISOLATE_VLAN",
        "entity_id": "iot-temp-01"
    }
    try:
        response = requests.post(f"{BASE_URL}/response/execute", json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Wait for server reload...")
    time.sleep(2)
    test_uc01_lateral_movement()
    test_uc02_sip_brute_force()
    test_uc03_dns_tunneling()
    test_uc04_rogue_iot()
    test_uc05_insider_threat()
    test_response_engine()
