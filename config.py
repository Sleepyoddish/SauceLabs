import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/v1/")
USERNAME = os.getenv("USERNAME", "standard_user")
PASSWORD = os.getenv("PASSWORD", "secret_sauce")
TIMEOUT = int(os.getenv("TIMEOUT", 5000))
