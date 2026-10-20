import os
import requests
import time

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

def main():
    send_message(
        "🤖 ChernovTradeBot запущен!\n"
        "Следующий этап — подключение анализа рынка Bitunix."
    )

if __name__ == "__main__":
    main()
