import asyncio
import logging
from fastapi.testclient import TestClient
from src.backend.app.main import app

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = TestClient(app)

def test_unified_api():
    print("--- Testing Unified API Endpoints ---")
    
    # 1. Test Dashboard
    print("\n1. Testing GET /api/v1/dashboard")
    response = client.get("/api/v1/dashboard")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Dashboard Data Keys: {list(data.keys())}")
        assert "network_devices" in data
        assert "alerts" in data
    else:
        print(f"Error: {response.text}")

    # 2. Test Connect Device
    print("\n2. Testing POST /api/v1/devices/connect")
    device_payload = {
        "device_type": "surveillance",
        "ip_address": "192.168.99.100",
        "credentials": {"username": "admin", "password": "password"},
        "action": "connect",
        "parameters": {}
    }
    response = client.post("/api/v1/devices/connect", json=device_payload)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print(f"Connect Result: {response.json()}")
    else:
        print(f"Error: {response.text}")
        
    # 3. Test Trigger Automation
    print("\n3. Testing POST /api/v1/automation/trigger")
    automation_payload = {
        "scene_name": "LOCKDOWN_LEVEL_1",
        "parameters": {"zone": "sector_7"}
    }
    # Note: query parameters vs body. The API definition uses query params for scene_name if not in body, 
    # but let's check the implementation: `async def trigger_automation(scene_name: str, parameters: Dict[str, Any] = None):`
    # FastApi interprets `scene_name` as query param and `parameters` as body if it's a Pydantic model or Dict.
    # Let's adjust the call to match FastAPI's default behavior for `Dict` body.
    
    response = client.post(f"/api/v1/automation/trigger?scene_name=LOCKDOWN_LEVEL_1", json={"zone": "sector_7"})
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print(f"Automation Result: {response.json()}")
    else:
        print(f"Error: {response.text}")

    print("\n--- Unified API Verification Complete ---")

if __name__ == "__main__":
    test_unified_api()
