from pyrogram import filters

def init(app):
    @app.on_message(filters.command("report"))
    def report(_, message):
        parts = message.text.split()
        if len(parts) < 3:
            return message.reply_text("Usage: !report @user reason")
        reported_user = parts[1]
        reason = " ".join(parts[2:])
        message.reply_text(f"{reported_user} reported for: {reason}")
