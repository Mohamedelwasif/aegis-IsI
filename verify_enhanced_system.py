import asyncio
import logging
import sys
import os

# Add the src/backend directory to sys.path
sys.path.append(os.path.join(os.getcwd(), 'src', 'backend'))

from app.services.enhanced_aegis_system import EnhancedAEGISSystem

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Verification")

async def verify_enhanced_system():
    logger.info("Verifying Enhanced AEGIS System...")
    
    try:
        aegis = EnhancedAEGISSystem()
        logger.info("System initialized successfully.")
        
        logger.info("Testing comprehensive protection execution...")
        results = await aegis.execute_comprehensive_protection()
        
        logger.info("Protection Execution Results:")
        for layer, result in results.items():
            logger.info(f"{layer}: {result}")
            
        logger.info("Enhanced AEGIS System verification PASSED.")
        
    except Exception as e:
        logger.error(f"Enhanced AEGIS System verification FAILED: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(verify_enhanced_system())
