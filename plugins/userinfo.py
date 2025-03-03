from pyrogram import filters

def init(app):
    @app.on_message(filters.command("userinfo"))
    def userinfo(_, message):
        user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
        message.reply_text(f"User Info:\nName: {user.first_name}\nID: {user.id}\nUsername: @{user.username}")
