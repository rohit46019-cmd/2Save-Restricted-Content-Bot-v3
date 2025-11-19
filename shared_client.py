import os
from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN, STRING
from pyrogram import Client
import sys

# USE /tmp INSTEAD OF /var/data
SESSION_DIR = "/tmp/sessions"
os.makedirs(SESSION_DIR, exist_ok=True)

# TELETHON SESSION
client = TelegramClient(
    f"{SESSION_DIR}/telethonbot",
    API_ID,
    API_HASH
)

# PYROGRAM BOT SESSION
app = Client(
    f"{SESSION_DIR}/pyrogrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# USERBOT SESSION (STRING SESSION)
userbot = Client(
    f"{SESSION_DIR}/4gbbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING
)

async def start_client():

    # ---- Telethon ----
    try:
        await client.start(bot_token=BOT_TOKEN)
        print("Telethon Bot Started")
    except Exception as e:
        print("Telethon start error:", e)

    # ---- Userbot ----
    if STRING:
        try:
            await userbot.start()
            print("Userbot Started")
        except Exception as e:
            print("Invalid STRING session:", e)
            sys.exit(1)

    # ---- Pyrogram ----
    try:
        await app.start()
        print("Pyro Bot Started")
    except Exception as e:
        print("Pyrogram start error:", e)

    # MOST IMPORTANT FIX:
    # Make these objects importable from plugins
    globals()["tele_client"] = client
    globals()["pyro_client"] = app
    globals()["userbot_client"] = userbot

    return client, app, userbot
