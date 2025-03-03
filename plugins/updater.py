import os
import subprocess
from pyrogram import Client, filters
from config import OWNER_ID

@Client.on_message(filters.command("updatebot") & filters.user(OWNER_ID))
async def update_bot(client, message):
    await message.reply("Updating bot, please wait...")
    subprocess.run(["git", "pull"])
    await message.reply("Bot updated! Use /reload to restart.")
    os.execv("python", ["python", "main.py"])
