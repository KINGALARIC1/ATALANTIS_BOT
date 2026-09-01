import os
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

    response = requests.post(
        url,
        json=data,
        timeout=30
    )

    return response.json()


def format_statement(country, statement):
    return f"""🏳️ 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐒𝐓𝐀𝐓𝐄𝐌𝐄𝐍𝐓
━━━━━━━━━━━━━━━━━━
📜 𝐒𝐓𝐀𝐓𝐄𝐌𝐄𝐍𝐓

{statement}

━━━━━━━━━━━━━━━━━━
🌐 {country["group"]}
🏳️ {country["name"]}"""


def get_country_info(country_name):
    country = get_country_by_name(country_name)

    if not country:
        return None

    return {
        "name": country["name"],
        "group": country["group"],
        "tag": country["tag"],
        "vip": country["vip"],
        "occupied": country["occupied"]
    }


def main():
    print("Atlantis War Bot Started")

    # تست اتصال به اطلاعات کشورها
    country = get_country_info("بریتانیا")

    if country:
        print("کشور:", country["name"])
        print("کد:", country["tag"])
        print("گروه:", country["group"])
        print("VIP:", country["vip"])


if __name__ == "__main__":
    main()
