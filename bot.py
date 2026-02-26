import os
import requests
import asyncio
from telegram import Bot

# =======================
# Настройки бота
# =======================
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")  # берём из GitHub Secrets
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")      # свой Telegram ID или группы

bot = Bot(token=TELEGRAM_TOKEN)

# =======================
# Список токенов для мониторинга
# =======================
TOKENS = {
    "pDAI/DAI": "https://dexscreener.com/pulsechain/0xfc64556faa683e6087f425819c7ca3c558e13ac1",
    "TOM/WPLS": "https://dexscreener.com/pulsechain/0xe45f18acce05af14a16cec2d8edf6ae6950175b3",
    "LNKR/WPLS": "https://dexscreener.com/pulsechain/0x8b7b4f6f76c3e511e623366f947a38aa6bc07b0c", 
    "PIKA/WPLS": "https://dexscreener.com/pulsechain/0x60fb68986190995ed0454174aa85ca3f411eb95d",
    "ZERO/WPLS": "https://dexscreener.com/pulsechain/0x5f838ad5d614d06ec96d458105435f0d35451d2d",
    "DWB/WPLS": "https://dexscreener.com/pulsechain/0xe644f9b23375d07f5fe11cc223716c6db7ea356b",
    "INC/WPLS": "https://dexscreener.com/pulsechain/0xf808bb6265e9ca27002c0a04562bf50d4fe37eaa",
    "FED/TBILL": "https://dexscreener.com/pulsechain/0xad2c3fc5a5a5408b174811758102eb3c77627b5c",
    "TEDDYBEAR/TBILL": "https://dexscreener.com/pulsechain/0x24c4d0532cddae3b0b8935196f2b91e68d6b85ed",
    "FDIC/WPLS": "https://dexscreener.com/pulsechain/0x1334b0e3f2788c226fa19069b3ac64f283417fd3",
    "RH PEPE/WPLS": "https://dexscreener.com/pulsechain/0x2a8f6137ba7749560bb9e84b36cb2ac9536d9e88",
}

# =======================
# Функция отправки сообщений
# =======================
async def send_message(text):
    await bot.send_message(chat_id=CHAT_ID, text=text)

# =======================
# Функция проверки токенов
# =======================
async def check_tokens():
    for name, url in TOKENS.items():
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                await send_message(f"✅ {name} доступен на Dexscreener: {url}")
            else:
                await send_message(f"⚠️ {name} недоступен: {r.status_code}")
        except Exception as e:
            await send_message(f"❌ Ошибка {name}: {e}")

# =======================
# Точка входа
# =======================
if __name__ == "__main__":
    asyncio.run(check_tokens())
