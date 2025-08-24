import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8350094964:AAE-ebwWQBx_YWnW_stEqcxiKKVVx8SZaAw"

MESSAGE = (
    "Just pay and get entry...\n"
    "Just pay and get entry...Just pay and get entry...Just pay and get entry...Just pay and get entry...Just pay and get entry..."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(MESSAGE)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot started successfully ✅")
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    asyncio.run(main())
