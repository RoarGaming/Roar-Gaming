
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Your bot token
TOKEN = "7445110199:-PCAVCkkYT3Jqly87DhM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the command /start is issued."""
    user = update.effective_user
    welcome_message = (
        f"Hello {user.first_name}! 👋\n\n"
        "Welcome to this bot! I'm here to help you. "
        "Feel free to explore my features and commands.\n\n"
        "Type /help to see what I can do for you!"
    )
    await update.message.reply_html(welcome_message)

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
