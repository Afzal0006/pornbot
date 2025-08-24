import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

BOT_TOKEN = "7607621887:AAHVpaKwitszMY9vfU2-s0n60QNL56rdbM0"

START_MESSAGE = (
    "Direct P#rn Video Channel 🌸\n\n"
    "D#si Maal Ke Deewano Ke Liye 😋\n\n"
    "No Sn#ps Pure D#si Maal 😙\n\n"
    "51000+ rare D#si le#ks ever.... 🎀\n\n"
    "Just pay and get entry...\n\n"
    "Direct video No Link - Ads Sh#t 🔥\n\n"
    "Price :- ₹69/-\n\n"
    "Validity :- lifetime"
)

PREMIUM_MESSAGE = (
    "𝗣𝗮𝘆 𝗝𝘂𝘀𝘁 ₹𝟲𝟵/- 𝗔𝗻𝗱 𝗚𝗲𝘁 𝗟𝗶𝗳𝗲𝘁𝗶𝗺𝗲 𝗔𝗰𝗰𝗲𝘀𝘀 🔥\n\n"
    "𝗦𝗲𝗻𝗱 𝗦𝗦 𝗮𝗳𝘁𝗲𝗿 𝗽𝗮𝘆𝗺𝗲𝗻𝘁🦋✅\n\n"
    "𝗦𝗘𝗡𝗗 𝗦𝗖𝗥𝗘𝗘𝗡𝗦𝗛𝗢𝗧 @MMSWALA069 💖"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("💎 Get Premium", callback_data="get_premium")],
        [InlineKeyboardButton("🎥 Premium Demo", url="https://t.me/SexyEmoji")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        START_MESSAGE,
        reply_markup=reply_markup,
        reply_to_message_id=update.message.message_id,
        do_quote=True
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == "get_premium":
        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="back")],
            [InlineKeyboardButton("🎥 Premium Demo", url="https://t.me/SexyEmoji")]
        ]
        await query.edit_message_text(PREMIUM_MESSAGE, reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("💎 Get Premium", callback_data="get_premium")],
            [InlineKeyboardButton("🎥 Premium Demo", url="https://t.me/SexyEmoji")]
        ]
        await query.edit_message_text(START_MESSAGE, reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot started successfully ✅")
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    asyncio.run(main())
