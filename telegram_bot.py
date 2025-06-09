import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import httpx

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BACKEND_URL = "http://172.20.10.2:8000"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Використай команди:\n"
        "/alt <episode_id> <title|description> <твій prompt>\n"
        "Приклад: /alt 1 title Rewrite for kids"
    )

async def alt_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        episode_id = args[0]
        target = args[1]
        prompt = ' '.join(args[2:])

        payload = {"target": target, "prompt": prompt}
        async with httpx.AsyncClient() as client:
            resp = await client.post(f"{BACKEND_URL}/episodes/{episode_id}/generate_alternative", json=payload)
            resp.raise_for_status()
            result = resp.json()

        await update.message.reply_text(f"Alternative {target}:\n{result['generated_alternative']}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("alt", alt_command))
    app.run_polling()

if __name__ == "__main__":
    run_bot()
