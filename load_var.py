# load_env.py
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

print("API_version:", os.getenv("API_version"))