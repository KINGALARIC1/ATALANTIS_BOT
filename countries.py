# -*- coding: utf-8 -*-

# کشورهای بازی اتلانتیس وار
# هر کشور یک کد ۶ رقمی اختصاصی دارد.

COUNTRIES = {
    # =========================
    # BRICS
    # =========================

    "785241": {
        "name": "بریتانیا",
        "english": "United Kingdom",
        "tag": "🇬🇧",
        "group": "NATO",
        "vip": True,
        "occupied": True
    },

    "120001": {
        "name": "برزیل",
        "english": "Brazil",
        "tag": "🇧🇷",
        "group": "BRICS",
        "vip": False,
        "occupied": False
    },

    "120002": {
        "name": "روسیه",
        "english": "Russia",
        "tag": "🇷🇺",
        "group": "BRICS",
        "vip": True,
        "occupied": True
    },

    "120003": {
        "name": "هند",
        "english": "India",
        "tag": "🇮🇳",
        "group": "BRICS",
        "vip": False,
        "occupied": True
    },

    "120004": {
        "name": "چین",
        "english": "China",
        "tag": "🇨🇳",
        "group": "BRICS",
        "vip": True,
        "occupied": True
    },

    "120005": {
        "name": "ونزوئلا",
        "english": "Venezuela",
        "tag": "🇻🇪",
        "group": "BRICS",
        "vip": False,
        "occupied": False
    },

    "120006": {
        "name": "آفریقای جنوبی",
        "english": "South Africa",
        "tag": "🇿🇦",
        "group": "BRICS",
        "vip": False,
        "occupied": False
    },

    "120007": {
        "name": "مصر",
        "english": "Egypt",
        "tag": "🇪🇬",
        "group": "BRICS",
        "vip": False,
        "occupied": False
    },

    "120008": {
        "name": "کره شمالی",
        "english": "North Korea",
        "tag": "🇰🇵",
        "group": "BRICS",
        "vip": False,
        "occupied": True
    },

    "120009": {
        "name": "ایران",
        "english": "Iran",
        "tag": "🇮🇷",
        "group": "BRICS",
        "vip": True,
        "occupied": True
    },

    "120010": {
        "name": "یمن",
        "english": "Yemen",
        "tag": "🇾🇪",
        "group": "BRICS",
        "vip": False,
        "occupied": True
    },

    "120011": {
        "name": "اندونزی",
        "english": "Indonesia",
        "tag": "🇮🇩",
        "group": "BRICS",
        "vip": False,
        "occupied": False
    },

    "120012": {
        "name": "سوریه",
        "english": "Syria",
        "tag": "🇸🇾",
        "group": "BRICS",
        "vip": False,
        "occupied": False
    },

    "120013": {
        "name": "فیلیپین",
        "english": "Philippines",
        "tag": "🇵🇭",
        "group": "BRICS",
        "vip": False,
        "occupied": False
    },

    "120014": {
        "name": "ویتنام",
        "english": "Vietnam",
        "tag": "🇻🇳",
        "group": "BRICS",
        "vip": False,
        "occupied": False
    },

    "120015": {
        "name": "عراق",
        "english": "Iraq",
        "tag": "🇮🇶",
        "group": "BRICS",
        "vip": False,
        "occupied": False
    },

    "120016": {
        "name": "فلسطین",
        "english": "Palestine",
        "tag": "🇵🇸",
        "group": "BRICS",
        "vip": False,
        "occupied": True
    },

    "120017": {
        "name": "لبنان",
        "english": "Lebanon",
        "tag": "🇱🇧",
        "group": "BRICS",
        "vip": False,
        "occupied": True
    },


    # =========================
    # NATO
    # =========================

    "220001": {
        "name": "امریکا",
        "english": "USA",
        "tag": "🇺🇸",
        "group": "NATO",
        "vip": True,
        "occupied": True
    },

    "220002": {
        "name": "آلمان",
        "english": "Germany",
        "tag": "🇩🇪",
        "group": "NATO",
        "vip": False,
        "occupied": True
    },

    "220003": {
        "name": "ژاپن",
        "english": "Japan",
        "tag": "🇯🇵",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220004": {
        "name": "فرانسه",
        "english": "France",
        "tag": "🇫🇷",
        "group": "NATO",
        "vip": False,
        "occupied": True
    },

    "220005": {
        "name": "پاکستان",
        "english": "Pakistan",
        "tag": "🇵🇰",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220006": {
        "name": "ایتالیا",
        "english": "Italy",
        "tag": "🇮🇹",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220007": {
        "name": "کانادا",
        "english": "Canada",
        "tag": "🇨🇦",
        "group": "NATO",
        "vip": False,
        "occupied": True
    },

    "220008": {
        "name": "کره جنوبی",
        "english": "South Korea",
        "tag": "🇰🇷",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220009": {
        "name": "هلند",
        "english": "Netherlands",
        "tag": "🇳🇱",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220010": {
        "name": "بلژیک",
        "english": "Belgium",
        "tag": "🇧🇪",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220011": {
        "name": "لهستان",
        "english": "Poland",
        "tag": "🇵🇱",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220012": {
        "name": "مکزیک",
        "english": "Mexico",
        "tag": "🇲🇽",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220013": {
        "name": "استونی",
        "english": "Estonia",
        "tag": "🇪🇪",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220014": {
        "name": "لتونی",
        "english": "Latvia",
        "tag": "🇱🇻",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220015": {
        "name": "لیتوانی",
        "english": "Lithuania",
        "tag": "🇱🇹",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220016": {
        "name": "نروژ",
        "english": "Norway",
        "tag": "🇳🇴",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220017": {
        "name": "دانمارک",
        "english": "Denmark",
        "tag": "🇩🇰",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220018": {
        "name": "ترکیه",
        "english": "Turkey",
        "tag": "🇹🇷",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220019": {
        "name": "ایسلند",
        "english": "Iceland",
        "tag": "🇮🇸",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220020": {
        "name": "یونان",
        "english": "Greece",
        "tag": "🇬🇷",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220021": {
        "name": "اسرائیل",
        "english": "Israel",
        "tag": "✡️",
        "group": "NATO",
        "vip": False,
        "occupied": True
    },

    "220022": {
        "name": "عربستان",
        "english": "Saudi Arabia",
        "tag": "🇸🇦",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },

    "220023": {
        "name": "اوکراین",
        "english": "Ukraine",
        "tag": "🇺🇦",
        "group": "NATO",
        "vip": False,
        "occupied": True
    },

    "220024": {
        "name": "استرالیا",
        "english": "Australia",
        "tag": "🇦🇺",
        "group": "NATO",
        "vip": False,
        "occupied": False
    },


    # =========================
    # NEUTRAL
    # =========================

    "330001": {
        "name": "امارات",
        "english": "UAE",
        "tag": "🇦🇪",
        "group": "NEUTRAL",
        "vip": False,
        "occupied": False
    },

    "330002": {
        "name": "اردن",
        "english": "Jordan",
        "tag": "🇯🇴",
        "group": "NEUTRAL",
        "vip": False,
        "occupied": False
    },

    "330003": {
        "name": "بحرین",
        "english": "Bahrain",
        "tag": "🇧🇭",
        "group": "NEUTRAL",
        "vip": False,
        "occupied": False
    },

    "330004": {
        "name": "کرواسی",
        "english": "Croatia",
        "tag": "🇭🇷",
        "group": "NEUTRAL",
        "vip": False,
        "occupied": False
    },

    "330005": {
        "name": "قطر",
        "english": "Qatar",
        "tag": "🇶🇦",
        "group": "NEUTRAL",
        "vip": False,
        "occupied": True
    },

    "330006": {
        "name": "سوئد",
        "english": "Sweden",
        "tag": "🇸🇪",
        "group": "NEUTRAL",
        "vip": False,
        "occupied": False
    },

    "330007": {
        "name": "فنلاند",
        "english": "Finland",
        "tag": "🇫🇮",
        "group": "NEUTRAL",
        "vip": False,
        "occupied": False
    },

    "330008": {
        "name": "سوئیس",
        "english": "Switzerland",
        "tag": "🇨🇭",
        "group": "NEUTRAL",
        "vip": False,
        "occupied": False
    },

    "330009": {
        "name": "اتریش",
        "english": "Austria",
        "tag": "🇦🇹",
        "group": "NEUTRAL",
        "vip": False,
        "occupied": False
    },

    "330010": {
        "name": "کامرون",
        "english": "Cameroon",
        "tag": "🇨🇲",
        "group": "NEUTRAL",
        "vip": False,
        "occupied": False
    },


    # =========================
    # ORGANIZATIONS
    # =========================

    "440001": {
        "name": "سازمان ملل",
        "english": "United Nations",
        "tag": "🇺🇳",
        "group": "ORGANIZATION",
        "vip": False,
        "occupied": False
    }
}


def get_country(code):
    """پیدا کردن کشور با کد"""
    return COUNTRIES.get(str(code))


def get_country_by_name(name):
    """پیدا کردن کشور با نام فارسی یا انگلیسی"""
    name = name.strip().lower()

    for code, country in COUNTRIES.items():
        if (
            country["name"].lower() == name
            or country["english"].lower() == name
        ):
            return code, country

    return None, None


def is_vip_country(code):
    """بررسی VIP بودن کشور"""
    country = get_country(code)
    return country is not None and country["vip"]


def is_occupied(code):
    """بررسی پر بودن کشور"""
    country = get_country(code)
    return country is not None and country["occupied"]


def get_group(code):
    """گروه کشور"""
    country = get_country(code)
    return country["group"] if country else None
