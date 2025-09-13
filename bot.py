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
    users_col.update_one(
        {"_id": user_id},
        {
            "$set": {
                "chat_type": chat_type,
                "username": update.effective_user.username if update.effective_user else None,
            }
        },
        upsert=True
    )

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

    total = users_col.count_documents({})
    sent, failed = 0, 0

    for user in users_col.find():
        try:
            await context.bot.send_message(chat_id=user["_id"], text=msg)
            sent += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1

    report = (
        "✅ Broadcast completed.\n\n"
        f"📩 Sent: {sent}\n"
        f"❌ Failed: {failed}\n"
        f"👥 Total Saved: {total}"
    )
    await update.message.reply_text(report)

# ==== Stats Command ====
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in OWNER_IDS:
        await update.message.reply_text("⛔ You are not allowed to use this command.")
        return

    total = users_col.count_documents({})
    users = users_col.count_documents({"chat_type": "private"})
    groups = users_col.count_documents({"chat_type": {"$in": ["group", "supergroup"]}})
    premium = users_col.count_documents({"is_premium": True})

    text = (
        "📊 Bot Stats\n\n"
        f"👤 Users: {users}\n"
        f"👥 Groups: {groups}\n"
        f"💎 Premium: {premium}\n"
        f"🔢 Total Saved: {total}"
    )
    await update.message.reply_text(text)

# ==== Premium Command ====
async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in OWNER_IDS:
        await update.message.reply_text("⛔ You are not allowed to use this command.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /premium <username or user_id>")
        return

    target = context.args[0]

    query = {"_id": int(target)} if target.isdigit() else {"username": target.lstrip("@")}
    user = users_col.find_one(query)
    if not user:
        await update.message.reply_text("❌ User not found in database.")
        return

    users_col.update_one(query, {"$set": {"is_premium": True}})
    name = f"@{user.get('username')}" if user.get("username") else str(user.get("_id"))
    await update.message.reply_text(f"✅ {name} added to Premium List")

# ==== Premium List Command ====
async def premiumlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in OWNER_IDS:
        await update.message.reply_text("⛔ You are not allowed to use this command.")
        return

    premium_users = list(users_col.find({"is_premium": True}))
    if not premium_users:
        await update.message.reply_text("❌ No premium users found.")
        return

    text = f"💎 Premium Users ({len(premium_users)})\n\n"
    for i, user in enumerate(premium_users, start=1):
        if user.get("username"):
            text += f"{i}. @{user['username']}\n"
        else:
            text += f"{i}. {user.get('_id')}\n"

    await update.message.reply_text(text)

# ==== Handle Photo in DM ====
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await save_user(update)
    chat = update.effective_chat

    if chat.type == "private":
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
                await update.message.forward(owner)
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
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("premium", premium))
    app.add_handler(CommandHandler("premiumlist", premiumlist))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.ALL, track_users))
    print("Bot started successfully ✅")
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    asyncio.run(main())
