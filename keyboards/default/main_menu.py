from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Marcub = ReplyKeyboardMarkup(keyboard=
    [
        [KeyboardButton(text="USD 🇺🇸"), KeyboardButton(text="RUB 🇷🇺")],
        [KeyboardButton(text="EVRO 🇪🇺"), KeyboardButton(text="KZT 🇰🇿")],
        [KeyboardButton(text="UZB 🇺🇿")],
        [KeyboardButton(text="Valyuta kurslari 🪙")]
    ],
    resize_keyboard=True
)