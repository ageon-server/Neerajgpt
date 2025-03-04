import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, CallbackContext
import config
from modules import moderation, downloader, fun, ai_chat, security, utilities, owner, fetchera

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
    logger.info("Received /start command")
    keyboard = [
        [InlineKeyboardButton("Use Fetchera", callback_data='fetchera')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"Welcome to Ageon Bot! Managed by {config.Config.OWNER_USERNAME}", reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    logger.info("Received /help command")
    help_text = "Available commands:\n"
    for command, description in COMMANDS.items():
        help_text += f"/{command} - {description}\n"
    await update.message.reply_text(help_text)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses."""
    query = update.callback_query
    await query.answer()
    if query.data == 'fetchera':
        await fetchera.use_fetchera(query, context)

async def error_handler(update: object, context: CallbackContext) -> None:
    """Log the error and send a message to the user."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    if update.effective_message:
        await update.effective_message.reply_text('An error occurred while processing your request.')

def main() -> None:
    """Start the bot."""
    application = ApplicationBuilder().token(config.Config.BOT_TOKEN).build()

    # Set bot commands for UI
    application.bot.set_my_commands([
        BotCommand(command, description) for command, description in COMMANDS.items()
    ])

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button))

    # Load all modules
    moderation.register_handlers(application)
    downloader.register_handlers(application)
    fun.register_handlers(application)
    ai_chat.register_handlers(application)
    security.register_handlers(application)
    utilities.register_handlers(application)
    owner.register_handlers(application)

    # Error handler
    application.add_error_handler(error_handler)

    # Start the bot
    logger.info("Starting the bot...")
    application.run_polling()

if __name__ == '__main__':
    main()
