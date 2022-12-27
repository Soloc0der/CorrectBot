from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp



@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message):
    text = "Assalomu aleykum😁\n\nBu bot sizga xoxlagan turdagi valyutalarni so'm ga aylantirib beradi.😍 \n\nbot dan foydalanish uchun shunchaki aniq son yozing🫡\n\n dasturchi @pn_SOLO🧑‍💻"
    await message.answer(text)



