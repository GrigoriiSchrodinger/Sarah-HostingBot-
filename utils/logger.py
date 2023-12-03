import logging

logging.basicConfig(
    filename='log_info.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)
