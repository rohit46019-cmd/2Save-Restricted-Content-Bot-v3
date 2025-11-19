# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.

from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN, STRING
from pyrogram import Client
import sys
import os

# Render FREE plan: only this directory is writable persistently
SESSION_DIR = "/var/data/sessions"
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

# USERBOT SESSION (String Session)
userbot = Client(
    f"{SESSION_DIR}/4gbbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING
)

async def start_client():
    if not client.is_connected():
        await client.start(bot_token=BOT_TOKEN)
        print("SpyLib started...")

    if STRING:
        try:
            await userbot.start()
            print("Userbot started...")
        except Exception as e:
            print(f"Your premium string session may be invalid/expired: {e}")
            sys.exit(1)

    await app.start()
    print("Pyro App Started...")
    return client, app, userbot
