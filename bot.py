import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8350094964:AAE-ebwWQBx_YWnW_stEqcxiKKVVx8SZaAw"

MESSAGE = (
    "Direct P#rn Video Channel 🌸\n\n"
    "D#si Maal Ke Deewano Ke Liye 😋\n\n"
    "No Sn#ps Pure D#si Maal 😙\n\n"
    "51000+ rare D#si le#ks ever.... 🎀\n\n"
    "Just pay and get entry...\n\n"
    "Direct video No Link - Ads Sh#t 🔥\n\n"
    "Price :- ₹69/-\n\n"
    "Validity :- lifetime"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.delete()
    await update.message.reply_text(MESSAGE)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot started successfully ✅")
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    asyncio.run(main())
