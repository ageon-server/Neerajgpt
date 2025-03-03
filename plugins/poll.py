from pyrogram import filters

def init(app):
    @app.on_message(filters.command("poll"))
    def create_poll(_, message):
        parts = message.text.split("|")
        if len(parts) < 3:
            return message.reply_text("Usage: !poll Question | Option1 | Option2")
        question = parts[0].split(" ", 1)[1]
        options = parts[1:]
        message.reply_poll(question, options)
