import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("SPORTSDATAIO_REAL_TIME_API_KEY_NBA")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("PASSWORD")
RECIPIENT = os.getenv("RECIPIENT")
