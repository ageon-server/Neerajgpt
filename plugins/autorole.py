import config

def init(app):
    @app.on_message(filters.new_chat_members)
    def auto_role(_, message):
        for user in message.new_chat_members:
            message.reply_text(f"Welcome {user.mention}, you are now '{config.DEFAULT_ROLE}'!")
