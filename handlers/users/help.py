from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS
# from .translation import _
# from keyboards.default.main_menu import BtnMainMenu_defoult
# from keyboards.inline.main_menu_inline import BtnMainMenu_inline , Key_type_inline_defoult
from states.main_state import MainState



@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    # await MainState.Main.set()
    # user = await db.select_user(telegram_id=message.from_user.id)
    # if user is None:
    #     lang = message.from_user.language_code
    #     await message.answer(_("Hush kelibsiz!\n\n Iltimos Tilni tanlang !", lang))
    #     await MainState.Main.set() 
    # else:
    await bot.send_message(message.from_user.id, "Assalomu aleykum \n CaV bo'timizga xush kelibsiz 😇\n\nBot yordamida siz :<b>\n\nCrypto-valyuta va turli davlatlar valyutlarini kursini ko'rishingiz 📈💱\nCrypto valyuta va  turli davlatlar valyutalarini shu vaqtdagi kurs yordamida hisoblashingiz mumkin 🗓🔁</b>")
    # await MainState.Main.set()


    # , reply_markup=Key_type_inline_defoult(key_type, BtnMain1Menu_inline(lang=lang), BtnMain1Menu_defoult(lang=lang))









@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message):
    text = "Assalomu aleykum😁\n\nBu bot sizga xoxlagan turdagi valyutalarni so'm ga aylantirib beradi.😍 \n\nbot dan foydalanish uchun shunchaki aniq son yozing🫡\n\n dasturchi @pn_SOLO🧑‍💻"
    await message.answer(text)



