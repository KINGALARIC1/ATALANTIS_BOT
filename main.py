import os
import time
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

from countries import get_country_by_name

TOKEN = os.getenv("RUBIKA_TOKEN")

if not TOKEN:
    raise ValueError("RUBIKA_TOKEN تنظیم نشده است")

BASE_URL = f"https://botapi.rubika.ir/v3/{TOKEN}"


def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": text
    }

    response = requests.post(url, json=data, timeout=30)
    return response.json()


def format_statement(country, statement):
    return f"""🏳️ 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐒𝐓𝐀𝐓𝐄𝐌𝐄𝐍𝐓
━━━━━━━━━━━━━━━━━━
📜 𝐒𝐓𝐀𝐓𝐄𝐌𝐄𝐍𝐓

{statement}

━━━━━━━━━━━━━━━━━━
🌐 {country["group"]}
🏳️ {country["name"]}"""


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Atlantis War Bot is running")

    def log_message(self, format, *args):
        return


def start_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()


def main():
    print("Atlantis War Bot Started")

    # تست کشور
    country = get_country_by_name("بریتانیا")

    if country:
        print("کشور:", country["name"])
        print("کد:", country["tag"])
        print("گروه:", country["group"])
        print("VIP:", country["vip"])

    # سرور مخصوص Render
    threading.Thread(target=start_server, daemon=True).start()

    while True:
        time.sleep(60)


if __name__ == "__main__":
    main()
