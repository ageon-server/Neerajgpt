from pyrogram import filters

def init(app):
    @app.on_message(filters.new_chat_members)
    def welcome_message(_, message):
        for member in message.new_chat_members:
            message.reply_text(f"Welcome {member.mention} to {message.chat.title}! Enjoy your stay.")
