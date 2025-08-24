from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8350094964:AAGuq7wGITTob4ASpHj6dxDmVIxppqNlhBY"

START_MESSAGE = """
> 📢 Direct P\\#rn Video Channel 🌸  
>  
> D\\#si Maal Ke Deewano Ke Liye 😋  
>  
> No Sn\\#ps Pure D\\#si Maal 😙  
>  
> 51000+ rare D\\#si le\\#ks ever.... 🎀  
>  
> Just pay and get entry...  
>  
> Direct video No Link \\- Ads Sh\\#t 🔥  
>  
> 💰 Price :- ₹69/-
> ♾️ Validity :- lifetime
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 DEMO", url="https://t.me/your_demo_channel")],
        [InlineKeyboardButton("💰 Buy Now", url="https://t.me/your_payment_bot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        START_MESSAGE,
        reply_markup=reply_markup,
        parse_mode="MarkdownV2"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    main()
