from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import config
from modules import moderation, downloader, fun, ai_chat, security, utilities, owner

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Welcome to Neerajpro Bot! Managed by {config.OWNER_USERNAME}")

def main():
    app = Application.builder().token(config.BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    moderation.register_handlers(app)
    downloader.register_handlers(app)
    fun.register_handlers(app)
    ai_chat.register_handlers(app)
    security.register_handlers(app)
    utilities.register_handlers(app)
    owner.register_handlers(app)

    print("Neerajpro Bot Started!")
    app.run_polling()

if __name__ == "__main__":
    main()
