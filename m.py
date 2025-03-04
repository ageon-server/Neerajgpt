import dotenv
import logging
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from config import config
from modules import aichat, downloader, fun, moderation, security, owner, utilities

# Load environment variables from .env file
dotenv.load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Command descriptions
COMMANDS = {
    "start": "Start the bot",
    "help": "Show this help message",
    "chat": "Chat with the AI (usage: /chat <message>)",
    "download": "Download a file (usage: /download <url>)",
    "joke": "Tell a joke",
    "kick": "Kick a user (reply to a user's message with /kick)",
    "ban": "Ban a user (reply to a user's message with /ban)",
    "owner": "Show owner info",
    "ping": "Check bot's responsiveness"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hello! I am your bot.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = "Available commands:\n"
    for command, description in COMMANDS.items():
        help_text += f"/{command} - {description}\n"
    await update.message.reply_text(help_text)

async def error_handler(update: object, context: CallbackContext) -> None:
    """Log the error and send a message to the user."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    if update.effective_message:
        await update.effective_message.reply_text('An error occurred while processing your request.')

def main() -> None:
    """Start the bot."""
    application = ApplicationBuilder().token(config.TOKEN).build()

    # Set bot commands for UI
    application.bot.set_my_commands([
        BotCommand(command, description) for command, description in COMMANDS.items()
    ])

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Load all modules
    aichat.setup(application)
    downloader.setup(application)
    fun.setup(application)
    moderation.setup(application)
    security.setup(application)
    owner.setup(application)
    utilities.setup(application)

    # Error handler
    application.add_error_handler(error_handler)

    # Start the bot
    logger.info("Starting the bot...")
    application.run_polling()

if __name__ == '__main__':
    main()
