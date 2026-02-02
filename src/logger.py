import logging
from logging.handlers import WatchedFileHandler


LOG_FILE  = "logs/app.log"

formatter = logging.Formatter(
    fmt="%(asctime)s %(levelname)s %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

handler = WatchedFileHandler(
    filename=LOG_FILE, 
    encoding="utf-8")

handler.setFormatter(formatter)
logger.addHandler(handler)

# logging.info("Passed!\u2705")
# logging.error("Failed!\u274c")
