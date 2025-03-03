from pyrogram import Client, filters
import config
from plugins import *

app = Client("PriyaBot", bot_token=config.BOT_TOKEN, api_id=config.API_ID, api_hash=config.API_HASH)

# Auto Load Plugins (हर Plugin खुद लोड होगा)
plugins = [
    welcome, moderation, fun, notes, music, ai_chat, insta_downloader,
    yt_downloader, weather, report, userinfo, poll, banned_words,
    antighost, autorole, broadcast, backup, updater, system_tools
]

for plugin in plugins:
    plugin.init(app)

@app.on_message(filters.command("start"))
def start(_, message):
    message.reply_text("Hello! मैं Priya Bot (NEERAJ sir Edition) हूँ, तेरे ग्रुप का असली बॉस!")

app.run()
