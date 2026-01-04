import sys
import os
import asyncio
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Add src to path
sys.path.append(os.path.join(os.getcwd(), "src"))

try:
    from backend.app.services.aegis_core import AEGISSystem, DeviceType
except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)

async def main():
    print("Initializing AEGIS System...")
    try:
        aegis = AEGISSystem()
    except Exception as e:
        print(f"Initialization Failed: {e}")
        import traceback
        traceback.print_exc()
        return

    print("\n--- Testing Network Discovery ---")
    devices = await aegis.discover_network_devices("192.168.1.0/24")
    print(f"Discovered {len(devices)} devices:")
    for dev in devices:
        print(f"  - [{dev.type.value}] {dev.manufacturer} {dev.model} ({dev.ip_address})")
        
    print("\n--- Testing Integration Lifecycle ---")
    # Try integrating one of each type found
    integrated_count = 0
    for dev in devices:
        if integrated_count >= 3: break # Test first 3 only
        print(f"\nIntegrating {dev.id} ({dev.type.value})...")
        result = await aegis.integrate_device(dev)
        print(f"Integration Result: {result.get('status')}")
        if result.get("error"):
            print(f"  Error: {result.get('error')}")
        integrated_count += 1
        
    print("\n--- Testing Dashboard Aggregation ---")
    dashboard = await aegis.unified_monitoring_dashboard()
    print("Dashboard Data Keys:", list(dashboard.keys()))
    print("Network Status:", dashboard.get("network_devices"))
    
    print("\n--- Testing Automated Response ---")
    mock_event = {
        "id": "evt-999",
        "type": "lateral_movement_attack",
        "source_ip": "10.10.10.5",
        "source_id": "host-compromised"
    }
    response = await aegis.automated_response_system(mock_event)
    print("Response Strategy:", response.get("strategy"))
    print("Actions Taken:", response.get("actions"))

if __name__ == "__main__":
    asyncio.run(main())
