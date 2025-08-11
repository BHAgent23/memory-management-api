#!/usr/bin/env python3
"""
Render-optimized startup script for Memory Management API.
This script is designed to work with Render's deployment environment.
"""

import os
import sys
import logging
from pathlib import Path

# Add the current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Configure logging for Render
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]  # Only console logging for Render
)

logger = logging.getLogger(__name__)

def main():
    """Main function optimized for Render deployment."""
    logger.info("🚀 Starting Memory Management API on Render")
    
    # Import here to avoid import issues
    try:
        from api import app
        import uvicorn
        
        # Get port from Render's PORT environment variable
        port = int(os.getenv("PORT", "8003"))
        host = "0.0.0.0"
        
        logger.info(f"🌐 Starting server on {host}:{port}")
        
        # Start server with Render-optimized settings
        uvicorn.run(
            app,
            host=host,
            port=port,
            log_level="info",
            access_log=True
        )
        
    except Exception as e:
        logger.error(f"❌ Failed to start server: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
