import os

from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).with_name(".env")
load_dotenv(env_path)


class Config:
    BASE_URL = os.getenv("BASE_URL")
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
    access_cookie_name = "memos.access-token"
