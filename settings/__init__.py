import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

EMAIL = os.environ.get("LINE_PRIVATE_BOT_EMAIL")
PASSWORD = os.environ.get("LINE_PRIVATE_BOT_PASSWORD")
AUTH_TOKEN = os.environ.get("LINE_PRIVATE_BOT_AUTH_TOKEN")

ADMIN_MIDS = ["u47689615351ce76d35a123c2f415faa0"]
