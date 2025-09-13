import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
from pymongo import MongoClient

# ==== CONFIG ====
BOT_TOKEN = "8229496805:AAEUDhTxTsBQsaXfpwcJjIZBuwK5h2FHo3M"
MONGO_URI = "mongodb+srv://afzal99550:afzal99550@cluster0.aqmbh9q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
OWNER_IDS = [6998916494]  # <-- Apna Telegram ID yaha daalna hai

# ==== MongoDB Setup ====
mongo = MongoClient(MONGO_URI)
db = mongo["botdb"]
users_col = db["users"]

# ==== Image URLs ====
START_IMAGE = "https://i.ibb.co/Mk5jTp1s/x.jpg"
PREMIUM_IMAGE = "https://i.ibb.co/7tm7hNpf/x.jpg"

# ==== Messages ====
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
    "𝗣𝗮𝘆 𝗝𝘂𝘀𝘁 ₹𝟲𝟵/- 𝗔𝗻𝗱 𝗚𝗲𝘁 𝗟𝗶𝗳𝗲𝘁𝗶𝗺𝗲 𝗔𝗰𝗰𝗲𝘀𝘀 🔥\n\n"
    "𝗦𝗲𝗻𝗱 𝗦𝗦 𝗮𝗳𝘁𝗲𝗿 𝗽𝗮𝘆𝗺𝗲𝗻𝘁🦋✅\n\n"
    "𝗦𝗘𝗡𝗗 𝗦𝗖𝗥𝗘𝗘𝗡𝗦𝗛𝗢𝗧 @MMSBHAI069 💖"
)

# ==== Save Users in Mongo ====
async def save_user(update: Update):
    chat = update.effective_chat
    user_id = chat.id
    chat_type = chat.type
    users_col.update_one({"_id": user_id}, {"$set": {"chat_type": chat_type}}, upsert=True)

# ==== Start Command ====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await save_user(update)
    keyboard = [
        [InlineKeyboardButton("💎 Get Premium", callback_data="get_premium")],
        [InlineKeyboardButton("🎥 Premium Demo", url="https://t.me/+nfSL70ptD3NhN2Y1")],
        [InlineKeyboardButton("✅ SELLING PROOFS", url="https://t.me/+8me1hbUoaZkxYmVl")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_photo(photo=START_IMAGE, caption=START_MESSAGE, reply_markup=reply_markup)

# ==== Button Actions ====
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == "get_premium":
        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="back")],
            [InlineKeyboardButton("🎥 Premium Demo", url="https://t.me/+nfSL70ptD3NhN2Y1")],
            [InlineKeyboardButton("✅ SELLING PROOFS", url="https://t.me/+8me1hbUoaZkxYmVl")]
        ]
        await query.edit_message_media(media=InputMediaPhoto(PREMIUM_IMAGE, caption=PREMIUM_MESSAGE),
                                       reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("💎 Get Premium", callback_data="get_premium")],
            [InlineKeyboardButton("🎥 Premium Demo", url="https://t.me/+nfSL70ptD3NhN2Y1")],
            [InlineKeyboardButton("✅ SELLING PROOFS", url="https://t.me/+8me1hbUoaZkxYmVl")]
        ]
        await query.edit_message_media(media=InputMediaPhoto(START_IMAGE, caption=START_MESSAGE),
                                       reply_markup=InlineKeyboardMarkup(keyboard))

# ==== Broadcast Command ====
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in OWNER_IDS:
        await update.message.reply_text("⛔ You are not allowed to use this command.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /broadcast Your message here")
        return

    msg = " ".join(context.args)
    await update.message.reply_text("✅ Broadcasting started...")

    count = 0
    for user in users_col.find():
        try:
            await context.bot.send_message(chat_id=user["_id"], text=msg)
            count += 1
            await asyncio.sleep(0.1)
        except Exception:
            pass

    await update.message.reply_text(f"✅ Broadcast completed.\n📩 Sent to {count} users/groups.")

# ==== Handle Photo in DM ====
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await save_user(update)
    chat = update.effective_chat

    if chat.type == "private":  # Sirf DM ke liye
        user = update.effective_user
        username = f"@{user.username}" if user.username else user.full_name
        profile_link = f"[Open Profile](tg://user?id={user.id})"

        text = (
            "🆕 New Premium User\n\n"
            f"👤 Name: {username}\n"
            f"🔗 Profile: {profile_link}"
        )

        for owner in OWNER_IDS:
            try:
                await update.message.forward(owner)  # photo forward karega
                await context.bot.send_message(owner, text, parse_mode="Markdown")
            except Exception:
                pass

# ==== Track All Users ====
async def track_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await save_user(update)

# ==== Main Function ====
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.ALL, track_users))
    print("Bot started successfully ✅")
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    asyncio.run(main())
