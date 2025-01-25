from requests import get as rget
import os
import logging

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)

MAIN_FILE_URL = os.environ.get('MAIN_FILE_URL')
try:
    if not MAIN_FILE_URL:
        raise ValueError("MAIN_FILE_URL is missing or empty")

    res = rget(MAIN_FILE_URL)
    if res.status_code == 200:
        with open('main.py', 'wb+') as f:
            f.write(res.content)
    else:
        LOGGER.error(f"Failed to download main.py {res.status_code}")
except Exception as e:
    LOGGER.error(f"Error downloading MAIN_FILE_URL: {e}")
