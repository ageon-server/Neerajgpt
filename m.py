import dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import config
from modules import aichat, downloader, fun, moderation, security, owner, utilities

# Load environment variables from .env file
dotenv.load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your bot.')

def main() -> None:
    application = ApplicationBuilder().token(config.TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    # Load all modules
    aichat.setup(application)
    downloader.setup(application)
    fun.setup(application)
    moderation.setup(application)
    security.setup(application)
    owner.setup(application)
    utilities.setup(application)

    application.run_polling()

if __name__ == '__main__':
    main()
