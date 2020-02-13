import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")
#API_KEY = os.getenv("SPORTSDATAIO_REAL_TIME_API_KEY_NBA")
#SAMPLE_SPREADSHEET_ID = os.getenv("SAMPLE_SPREADSHEET_ID")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("PASSWORD")
RECIPIENT = os.getenv("RECIPIENT")
GOOGLE_DOC = os.getenv("YOUR_GOOGLE_DOC")

#print(os.getenv("SAMPLE_SPREADSHEET_ID", "default value if none"))
#print(RECIPIENT)