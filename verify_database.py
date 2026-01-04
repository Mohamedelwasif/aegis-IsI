import asyncio
import os
from src.backend.app.services.unified_database import UnifiedDatabaseService, DeviceRecord, EventLog
from src.backend.app.services.aegis_core import Device, DeviceType

async def verify_database():
    print("--- Verifying Unified Database ---")
    
    # 1. Initialize Database
    db_service = UnifiedDatabaseService('sqlite:///test_aegis.db')
    print("✅ Database initialized")

    # 2. Register Device
    device = Device(
        id="test_camera_001",
        type=DeviceType.SURVEILLANCE,
        ip_address="192.168.1.50",
        credentials={},
        protocol="onvif",
        manufacturer="Axis",
        model="P1375"
    )
    
    device_info = {"status": "online", "resolution": "4k"}
    config_result = {"motion_detection": "enabled"}
    
    await db_service.register_device(device, device_info, config_result)
    print("✅ Device registered")
    
    # 3. Verify Device Persistence
    devices = await db_service.get_all_devices()
    assert len(devices) > 0
    print(f"✅ Device retrieved: {devices[0]['id']} ({devices[0]['device_type']})")
    
    # 4. Log Event
    event_data = {
        "event": {
            "source_id": "test_camera_001",
            "type": "MOTION_DETECTED"
        },
        "severity": "medium",
        "response": {"action": "record_clip"}
    }
    
    await db_service.store_alert(event_data)
    print("✅ Event logged")
    
    # 5. Verify Event Persistence
    events = await db_service.get_recent_events()
    assert len(events) > 0
    print(f"✅ Event retrieved: {events[0]['event_type']} from {events[0]['source_device']}")
    
    # Clean up
    if os.path.exists("test_aegis.db"):
        os.remove("test_aegis.db")
        print("✅ Test database cleaned up")
        
    print("--- Database Verification Complete ---")

if __name__ == "__main__":
    asyncio.run(verify_database())
