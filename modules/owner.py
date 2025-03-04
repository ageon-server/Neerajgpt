from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import config

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != config.OWNER_ID:
        return
    text = " ".join(context.args)
    for chat_id in context.bot_data.get("chats", []):
        await context.bot.send_message(chat_id=chat_id, text=text)

def register_handlers(app: Application):
    app.add_handler(CommandHandler("broadcast", broadcast))
