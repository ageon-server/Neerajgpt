import openai
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import config

openai.api_key = config.OPENAI_API_KEY

async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": update.message.text}]
    )
    reply = response['choices'][0]['message']['content']
    await update.message.reply_text(reply)

def register_handlers(app: Application):
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_chat))
