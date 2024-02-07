import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "25537043"))
  API_HASH = os.environ.get("API_HASH", "513962d838d498ca36461d6f9de2e66b")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6949256418:AAHmfgVxgbbR9xicO48enMBSrpTJHDqmunI")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "SipiccpBot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002002408186"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "publicearn.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "c2208684d7ebad60b2b12a48dd9cbab82f4f33db")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6816465945"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mgworks24:jhUVcpZ0Uiw8Svhd@cluster0.rj2bxk0.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002055755406")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002113782068"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/SipiccpBot)
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟

  
