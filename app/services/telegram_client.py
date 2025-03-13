import os
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
SESSION_FILE_NAME = "bookNook_session.session"

client = TelegramClient(SESSION_FILE_NAME, API_ID, API_HASH)
