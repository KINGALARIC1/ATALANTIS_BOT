import os
import time
import requests

TOKEN = os.getenv("RUBIKA_TOKEN")

if not TOKEN:
    raise RuntimeError("RUBIKA_TOKEN تنظیم نشده است.")

BASE_URL = f"https://botapi.rubika.ir/v3/{TOKEN}"


def api_call(method, data=None):
    response = requests.post(
        f"{BASE_URL}/{method}",
        json=data or {},
        timeout=30
    )
    response.raise_for_status()
    return response.json()


def send_message(chat_id, text):
    return api_call("sendMessage", {
        "chat_id": str(chat_id),
        "text": text
    })


offset_id = None

print("ربات اتلانتیس وار فعال شد!")

while True:
    try:
        data = {
            "limit": 10
        }

        if offset_id:
            data["offset_id"] = offset_id

        result = api_call("getUpdates", data)

        for update in result.get("updates", []):
            chat_id = update.get("chat_id")

            message = update.get("new_message") or {}
            text = message.get("text") or ""

            if not chat_id:
                continue

            if text == "/start":
                send_message(
                    chat_id,
                    "🌊 به ربات اتلانتیس وار خوش آمدید!\n\n"
                    "🤖 ربات با موفقیت فعال است."
                )

            elif text == "/help":
                send_message(
                    chat_id,
                    "📚 راهنمای ربات\n\n"
                    "/start - شروع ربات\n"
                    "/help - راهنما"
                )

            elif text:
                send_message(
                    chat_id,
                    "✅ پیام شما دریافت شد."
                )

        next_offset = result.get("next_offset_id")

        if next_offset:
            offset_id = str(next_offset)

        time.sleep(2)

    except Exception as error:
        print("خطا:", error)
        time.sleep(5)
