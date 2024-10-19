import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
user = {}
call = {}
dev = {}
logger = {}
logger_mode = {}
botname = {}
appp = {}
helper = {}





API_ID = int(getenv("API_ID", "21031306"))
API_HASH = getenv("API_HASH", "aee71f587c41672ff19ecac9b9994773")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
BOT_TOKEN = "6407040709:AAG3G0qXRXQGCpFx8z8QMkX6bInCaIRbGIQ"
MONGO_DB_URL = "mongodb+srv://anas:anas@cluster0.y7sfipi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
OWNER = ["anas55555555555"]
OWNER_NAME = "ժᥱ᥎ ✘ ᥉᥆υᖇᥴᥱ"
CHANNEL = "https://t.me/EFFB0T"
GROUP = "https://t.me/EFFB0T"
PHOTO = "https://telegra.ph/file/1f97996f8a72627318ab6.jpg"
LOGS = "jdjdjrhj99"
VIDEO = "https://t.me/anmii288/106"