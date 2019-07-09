# Importing OS
import os

# Importing dotenv
from dotenv import load_dotenv

# Loading dotenv()
load_dotenv()

# Setting enviroment constants
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HTTP_URL = os.getenv("BASE_HTTP_URL")