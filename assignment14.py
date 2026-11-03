
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Demonstrate different logging levels

logging.debug("This is a debug message")
logging.info("Program execution started")
logging.warning("This is a warning message")
logging.error("An error has occurred")
logging.critical("This is a critical error")

print("Logging messages have been recorded in app.log")
