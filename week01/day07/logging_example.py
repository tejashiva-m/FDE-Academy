import logging

logging.basicConfig(
    level=logging.INFO
)

logger = logging.getLogger(__name__)

logger.info("Application started")
logger.warning("Low disk space")
logger.error("Database unavailable")
