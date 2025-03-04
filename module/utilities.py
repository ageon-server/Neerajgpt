from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

async def qr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={text}"
    await update.message.reply_photo(photo=url)

def register_handlers(app: Application):
    app.add_handler(CommandHandler("qr", qr))
