from telegram import Update, ChatPermissions
from telegram.ext import Application, MessageHandler, filters, ContextTypes

async def detect_deleted(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.left_chat_member and update.message.left_chat_member.is_deleted:
        await update.message.reply_text(f"Deleted account {update.message.left_chat_member.id} left the group.")

def register_handlers(app: Application):
    app.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, detect_deleted))
