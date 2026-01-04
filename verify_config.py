import asyncio
from src.backend.app.services.config_loader import ConfigLoader
from src.backend.app.services.aegis_core import AEGISSystem, DeviceType

async def verify_config_loading():
    print("--- Verifying Configuration Loading ---")
    
    # 1. Load Config
    loader = ConfigLoader()
    config = loader.config
    
    print(f"✅ Config Loaded: System Name = {config.system.name}")
    print(f"✅ Config Loaded: Location = {config.system.location}")
    print(f"✅ Config Loaded: Smart Home Enabled = {config.modules.smart_home.enabled}")
    
    # Verify values match YAML
    assert config.system.name == "AEGIS-Corporate-HQ"
    assert config.modules.smart_home.enabled == False
    assert config.api.port == 8000
    
    # 2. Initialize AEGIS Core with Config
    aegis = AEGISSystem()
    print("✅ AEGIS System Initialized with Config")
    
    # 3. Verify Module Initialization based on Config
    modules = aegis.integration_modules
    
    if DeviceType.SMART_HOME in modules:
        print("❌ Error: Smart Home module should NOT be initialized")
    else:
        print("✅ Smart Home module correctly disabled")
        
    if DeviceType.NETWORK in modules:
        print("✅ Network module initialized")
        
    if DeviceType.TELEPHONY in modules:
        print("✅ Telephony module initialized")
        
    print("--- Configuration Verification Complete ---")

if __name__ == "__main__":
    asyncio.run(verify_config_loading())
