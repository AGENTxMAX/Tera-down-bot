import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()


ADMINS = list(map(int, os.environ.get('ADMINS', '1687601586').split()))
api_id = os.environ.get('TELEGRAM_API', '26337689')
api_hash = os.environ.get('TELEGRAM_HASH', '22cd104354b08dd79d0fb3082366c4b7')
bot_token = os.environ.get('BOT_TOKEN', '7464051534:AAFh0S27cHY0_vg1Ahm2Gn5J77b4-KS7MHs')
dump_id = os.environ.get('DUMP_CHAT_ID', '-1002577970040')
fsub_id = os.environ.get('FSUB_ID', '-1002606881347')
mongo_url = os.environ.get('MONGO_URL', 'mongodb+srv://drive082005:AiJSaaQ2zXg8ssMa@cluster0.mhw5cfu.mongodb.net/?retryWrites=true&w=majority')



#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://drive082005:AiJSaaQ2zXg8ssMa@cluster0.mhw5cfu.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "drive082005")

#Shortner (token system) 
# check my discription to help by using my refer link of shareus.io


SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "https://gplinks.com/")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "324b4084576edec534a6876eb48965ffcd98ec71")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 43200)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/AgentxMax/3") # shareus ka tut_vid he 


import logging

logging.basicConfig(level=logging.INFO)

if not ADMINS:
    logging.error("ADMINS variable is missing! Exiting now")
    exit(1)

if not api_id:
    logging.error("TELEGRAM_API variable is missing! Exiting now")
    exit(1)

if not api_hash:
    logging.error("TELEGRAM_HASH variable is missing! Exiting now")
    exit(1)

if not bot_token:
    logging.error("BOT_TOKEN variable is missing! Exiting now")
    exit(1)

if not dump_id:
    logging.error("DUMP_CHAT_ID variable is missing! Exiting now")
    exit(1)
else:
    dump_id = int(dump_id)

if not fsub_id:
    logging.error("FSUB_ID variable is missing! Exiting now")
    exit(1)
else:
    fsub_id = int(fsub_id)

if not mongo_url:
    logging.error("MONGO_URL variable is missing! Exiting now")
    exit(1)
