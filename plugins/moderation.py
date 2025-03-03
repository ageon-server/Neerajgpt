from pyrogram import filters
import config

warns = {}

def init(app):
    @app.on_message(filters.text & ~filters.private)
    def auto_moderation(_, message):
        for word in config.BANNED_WORDS:
            if word in message.text.lower():
                message.delete()
                warns[message.from_user.id] = warns.get(message.from_user.id, 0) + 1
                message.reply_text(f"{message.from_user.mention}, Warning! Banned Word Used! Total Warns: {warns[message.from_user.id]}")
