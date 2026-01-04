import asyncio
import logging
import sys
import os

# Ensure backend path is in sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), "src", "backend"))

from app.services.unified_database import UnifiedDatabase

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def init_db():
    logger.info("Initializing AEGIS Unified Database...")
    try:
        db = UnifiedDatabase()
        # The __init__ method of UnifiedDatabase already calls Base.metadata.create_all(self.engine)
        # So just instantiating it is enough to create tables if they don't exist.
        
        logger.info(f"Database initialized successfully at {db.engine.url}")
        
        # Optional: Add some initial seed data if needed
        # ...
        
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(init_db())
