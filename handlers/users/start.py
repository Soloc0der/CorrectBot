import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.currensy import get_currncy

from data.config import ADMINS
from loader import dp, db, bot
from data.currensy import get_curency_text
from keyboards.default.main_menu import Marcub

text = "\n\n💱 Valyuta hisoblagich Botiga xush kelibsiz.\nBot yordamida valyuta narxlarini bilishingiz va hisob kitob qilishingiz mumkin.\n"
text += get_curency_text()

@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"Assalomu aleeykum {name}\nbo'timizga xush kelibsiz 😇" + text, reply_markup=Marcub)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazada mavjud...")
        await message.answer(f"Assalomu aleeykum {name}\nbo'timizga xush kelibsiz 😇" + text, reply_markup=Marcub)

