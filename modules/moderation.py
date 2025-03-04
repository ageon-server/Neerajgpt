from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"Welcome {member.first_name} to the group!")

async def filter_banned_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    banned_words = ["badword1", "badword2"]
    if any(word in update.message.text.lower() for word in banned_words):
        await update.message.delete()

def register_handlers(app: Application):
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, filter_banned_words))
