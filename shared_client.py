# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.

from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN, STRING
from pyrogram import Client
import sys
import os

# Ensure /tmp folders exist (always writable on any host)
os.makedirs("/tmp/sessions", exist_ok=True)

client = TelegramClient("/tmp/sessions/telethonbot", API_ID, API_HASH)

app = Client(
    "/tmp/sessions/pyrogrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

userbot = Client(
    "/tmp/sessions/4gbbot",
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
            print(f"Hey honey!! check your premium string session, it may be invalid or expired: {e}")
            sys.exit(1)

    await app.start()
    print("Pyro App Started...")
    return client, app, userbot
