from dotenv import load_dotenv
import os

load_dotenv()

DB_PATH = os.getenv("DB_PATH")
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8001))

