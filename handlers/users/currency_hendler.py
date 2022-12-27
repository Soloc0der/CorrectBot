from loader import dp
from aiogram import types
from data.currensy import get_curency_text

@dp.message_handler(text="Valyuta kurslari 🪙", state="*")
async def get_first_steap(message: types.Message):
    txt = "🇺🇿 Hozirda O'zbekistondagi valyuta narxlari💸 \n⤵️"
    txt += get_curency_text()
    await message.answer(f"VALYUTA KURSLARI 🪙\n{txt}")
    
