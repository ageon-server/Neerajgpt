notes = {}

def init(app):
    @app.on_message(filters.command("setnote"))
    def set_note(_, message):
        note = message.text.split(None, 1)[1]
        notes[message.chat.id] = note
        message.reply_text("Note Set Successfully!")

    @app.on_message(filters.command("note"))
    def get_note(_, message):
        note = notes.get(message.chat.id, "No Note Found!")
        message.reply_text(f"Important Note: {note}")
