from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Marcub = ReplyKeyboardMarkup(keyboard=
    [
        [KeyboardButton(text="USD πΊπΈ"), KeyboardButton(text="RUB π·πΊ")],
        [KeyboardButton(text="EVRO πͺπΊ"), KeyboardButton(text="KZT π°πΏ")],
        [KeyboardButton(text="UZB πΊπΏ")],
        [KeyboardButton(text="Valyuta kurslari πͺ")]
    ],
    resize_keyboard=True
)