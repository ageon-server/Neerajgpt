from pyrogram import filters
import os

def init(app):
    @app.on_message(filters.command("reload"))
    def reload_bot(_, message):
        message.reply_text("Restarting...")
        os.execv(sys.executable, ['python'] + sys.argv)
