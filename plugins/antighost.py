def init(app):
    @app.on_message(filters.new_chat_members)
    def check_ghost(_, message):
        for user in message.new_chat_members:
            if not user.first_name:
                message.chat.kick_member(user.id)
                message.reply_text("Ghost User Auto-Kicked!")
