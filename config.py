import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()


ADMINS = list(map(int, os.environ.get('ADMINS', '5084389526').split()))
#All Variables Are Required
BOT_TOKEN = "7838756294:AAHl13XUVw-8wgVJmla-Dz5qUl-8C9ijB_I"
TELEGRAM_API = "20026290"
TELEGRAM_HASH = "561ae93345a2a4e435cff3c75a088b72"
FSUB_ID = "-1002688354661"
DUMP_CHAT_ID = "-1002688354661"
ADMIN_ID = "5084389526"
PORT = "8000"
# Your code to start the web server on the specified port



#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://hegodal811:rsRu17pspZAcp6V7@cluster0.prsvqax.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "cphdlust")

#Shortner (token system) 
# check my discription to help by using my refer link of shareus.io


SHORTLINK_URL = os.environ.get("SHORTLINK_URL", None)
SHORTLINK_API = os.environ.get("SHORTLINK_API", None)
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 43200)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/ultroid_official/18") # shareus ka tut_vid he 

