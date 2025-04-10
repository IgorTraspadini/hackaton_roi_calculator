import logging
import uuid
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Configure Logging with Rotating File Handler
handler = RotatingFileHandler("app.log", maxBytes=1000000, backupCount=5)
logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def log_action(action: str, details: str = "") -> str:
    """
    Logs an action with a unique ID and timestamp.

    Args:
        action (str): Description of the action performed.
        details (str): Additional details related to the action.

    Returns:
        str: The generated action ID.
    """
    action_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"Action ID: {action_id} | Action: {action} | Timestamp: {timestamp} | Details: {details}"
    logging.info(log_entry)
    return action_id
