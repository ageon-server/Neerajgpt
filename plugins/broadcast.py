from pyrogram import filters
import config

def init(app):
    @app.on_message(filters.command("broadcast") & filters.user(config.OWNER_ID))
    def broadcast(_, message):
        msg = message.text.split(" ", 1)[1]
        # यहाँ Broadcast Logic - Group List से Send करो
        message.reply_text(f"Broadcast Sent: {msg}")
