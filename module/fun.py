from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random

roasts = ["You're as useful as a white crayon.", "You bring everyone so much joy… when you leave the room."]
facts = ["Honey never spoils.", "Octopuses have three hearts."]

async def roast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(roasts))

async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(facts))

def register_handlers(app: Application):
    app.add_handler(CommandHandler("roast", roast))
    app.add_handler(CommandHandler("fact", fact))
