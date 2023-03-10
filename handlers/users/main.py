from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.main_state import CurrencyState

@dp.message_handler(text="USD πΊπΈ", state="*")
async def get_usd(message: types.Message, state : FSMContext):

    await state.update_data({
        "currency" : "usd"
    })

    usd_text = "πΊπΈ Hisoblamoqchi bo'lgan Aqsh dollorini  kiriting.\n\nMasalan: 100"
    await message.answer(usd_text)
    await CurrencyState.amount.set()

@dp.message_handler(text="RUB π·πΊ", state="*")
async def get_usd(message: types.Message, state : FSMContext):

    await state.update_data({
        "currency" : "rub"
    })

    rub_text = "π·πΊ Hisoblamoqchi bo'lgan Rossiya rublini kiriting.\n\nMasalan: 100"
    await message.answer(rub_text)
    await CurrencyState.amount.set()


@dp.message_handler(text="EVRO πͺπΊ", state="*")
async def get_usd(message: types.Message, state : FSMContext):

    await state.update_data({
        "currency" : "eur"
    })

    eur_text = "πͺπΊ Hisoblamoqchi bo'lgan EVROni kiriting.\n\nMasalan: 100"
    await message.answer(eur_text)
    await CurrencyState.amount.set()

@dp.message_handler(text="KZT π°πΏ", state="*")
async def get_usd(message: types.Message, state : FSMContext):

    await state.update_data({
        "currency" : "kzt"
    })

    kzt_text = "π°πΏ Hisoblamoqchi bo'lgan Qozog'iston tengesini kiriting.\n\nMasalan: 100"
    await message.answer(kzt_text)
    await CurrencyState.amount.set()


@dp.message_handler(text="UZB πΊπΏ", state="*")
async def get_usd(message: types.Message, state : FSMContext):

    await state.update_data({
        "currency" : "uzs"
    })

    uzs_text = "πΊπΏ Hisoblamoqchi bo'lgan O'zbek so'mini kiriting.\n\nMasalan: 100"
    await message.answer(uzs_text)
    await CurrencyState.amount.set()
