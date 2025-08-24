import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

BOT_TOKEN = "8231280897:AAESZBm1WJ3xslx3VBU5tKXRK1fXqe42XE0"

# Image URLs
START_IMAGE = "https://i.ibb.co/Mk5jTp1s/x.jpg"
PREMIUM_IMAGE = "https://i.ibb.co/7tm7hNpf/x.jpg"

# Updated START_MESSAGE
START_MESSAGE = (
    "𝗗𝗶𝗿𝗲𝗰𝘁 𝗣#𝗿𝗻 𝗩𝗶𝗱𝗲𝗼 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 🌸\n\n"
    "𝗗#𝘀𝗶 𝗠𝗮𝗮𝗹 𝗞𝗲 𝗗𝗲𝗲𝘄𝗮𝗻𝗼 𝗞𝗲 𝗟𝗶𝘆𝗲 😋\n\n"
    "𝗡𝗼 𝗦𝗻#𝗽𝘀 𝗣𝘂𝗿𝗲 𝗗#𝘀𝗶 𝗠𝗮𝗮𝗹 😙\n\n"
    "𝟱𝟭𝟬𝟬𝟬+ 𝗿𝗮𝗿𝗲 𝗗#𝘀𝗶 𝗹𝗲#𝗸𝘀 𝗲𝘃𝗲𝗿.... 🎀\n\n"
    "𝗝𝘂𝘀𝘁 𝗽𝗮𝘆 𝗮𝗻𝗱 𝗴𝗲𝘁 𝗲𝗻𝘁𝗿𝘆...\n\n"
    "𝗗𝗶𝗿𝗲𝗰𝘁 𝘃𝗶𝗱𝗲𝗼 𝗡𝗼 𝗟𝗶𝗻𝗸 - 𝗔𝗱𝘀 𝗦𝗵#𝘁 🔥\n\n"
    "𝗣𝗿𝗶𝗰𝗲 :- ₹𝟲𝟵/-\n\n"
    "𝗩𝗮𝗹𝗶𝗱𝗶𝘁𝘆 :- 𝗹𝗶𝗳𝗲𝘁𝗶𝗺𝗲"
)

PREMIUM_MESSAGE = (
    "𝗣𝗮𝘆 𝗝𝘂𝘀𝘁 ₹𝟲𝟵/-\n\n"
    "𝗔𝗻𝗱 𝗚𝗲𝘁 𝗟𝗶𝗳𝗲𝘁𝗶𝗺𝗲 𝗔𝗰𝗰𝗲𝘀𝘀🔥\n\n"
    "𝗦𝗲𝗻𝗱 𝗦𝗦 𝗮𝗳𝘁𝗲𝗿 𝗽𝗮𝘆𝗺𝗲𝗻𝘁🦋✅\n\n"
    "𝗦𝗘𝗡𝗗 𝗦𝗖𝗥𝗘𝗘𝗡𝗦𝗛𝗢𝗧 to\n\n"
    @MMSWALA069 💖\n\n""
)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("💎 Get Premium", callback_data="get_premium")],
        [InlineKeyboardButton("🎥 Premium Demo", url="https://t.me/+bzLmBT9OeKRlMjU1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_photo(
        photo=START_IMAGE,
        caption=START_MESSAGE,
        reply_markup=reply_markup,
    )

# Button actions
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == "get_premium":
        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="back")],
            [InlineKeyboardButton("🎥 Premium Demo", url="https://t.me/+bzLmBT9OeKRlMjU1")]
        ]
        await query.edit_message_media(
            media=InputMediaPhoto(PREMIUM_IMAGE, caption=PREMIUM_MESSAGE),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("💎 Get Premium", callback_data="get_premium")],
            [InlineKeyboardButton("🎥 Premium Demo", url="https://t.me/+bzLmBT9OeKRlMjU1")]
        ]
        await query.edit_message_media(
            media=InputMediaPhoto(START_IMAGE, caption=START_MESSAGE),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

# Main function
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot started successfully ✅")
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    asyncio.run(main())
