import config

def init(app):
    @app.on_message(filters.text)
    def banned_word_checker(_, message):
        for word in config.BANNED_WORDS:
            if word in message.text.lower():
                message.delete()
                message.reply_text(f"Banned word used! Warning issued.")
