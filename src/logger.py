import logging
import os
from datetime import datetime

# Create the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the logs directory path
logs_dir = os.path.join(os.getcwd(), "logs")  # Directory path for logs
os.makedirs(logs_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Main block
if __name__ == "__main__":
    logging.info("Logging has started")
