import json
import os
from pyrogram import Client, filters
from config import OWNER_ID

@Client.on_message(filters.command("backup") & filters.user(OWNER_ID))
async def backup_data(client, message):
    chat_data = {}
    for dialog in await client.get_dialogs():
        if dialog.chat.type in ["supergroup", "group"]:
            chat = dialog.chat
            chat_data[chat.id] = {
                "title": chat.title,
                "members_count": await client.get_chat_members_count(chat.id)
            }
    with open("group_backup.json", "w") as file:
        json.dump(chat_data, file, indent=4)
    await message.reply_document("group_backup.json", caption="Here is your Group Data Backup")
    os.remove("group_backup.json")
