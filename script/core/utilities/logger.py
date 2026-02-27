import logging
import os

# Create logs folder
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "app.log")

# Create a completely independent logger
logger = logging.getLogger("APP_LOGGER")

logger.setLevel(logging.INFO)

# Remove existing handlers (important)
logger.handlers.clear()

# Stop propagation to root logger
logger.propagate = False

# Create file handler
file_handler = logging.FileHandler(log_file)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)