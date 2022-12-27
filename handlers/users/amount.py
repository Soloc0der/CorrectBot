from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.main_state import CurrencyState
from data.currensy import cheaking_numbers, get_all_curencies, get_currncy
from data.currencies_to import *


@dp.message_handler(state=CurrencyState.amount)
async def get_amound(message:types.Message, state : FSMContext):
    data = await state.get_data()
    currency = str(data.get('currency'))
    amound = message.text


   



    
    if cheaking_numbers(amound):
        sum = get_all_curencies()
        amound = float(amound)
        #davlatni tekshirish
        if currency.lower() == "usd":
            text = f"🏠 Kiritildi {amound} Aqsh dollari. 🇺🇸\n\n🇺🇿 {round(sum[1] * amound, 2)} O'zbek so'mi.\n🇷🇺 {round(usd_rub * amound, 2)} Rossiya rubli\n🇪🇺 {round(usd_eur * amound, 2)} EVRO.\n🇰🇿 {round(usd_kzt * amound, 2)} Qozog'iston tengesi."
            await message.answer(text)

        elif currency.lower() == "rub":
            text = f"🏠 Kiritildi {amound} Rossiya rubli. 🇷🇺\n\n🇺🇿 {round(sum[0] * amound, 2)} O'zbek so'mi.\n🇺🇸 {round(rub_usd * amound, 2)} Aqsh dollari.\n🇰🇿 {round(rub_kzt * amound, 2)} Qozog'iston tengesi.\n🇪🇺 {round(rub_eur * amound, 2)} EVRO"
            await message.answer(text)

        elif currency.lower() == "eur":
            text = f"🏠 Kiritildi {amound} EVRO 🇪🇺.\n\n🇺🇿 {round(sum[2] * amound, 2)} O'zbek so'mi.\n🇷🇺 {round(eur_rub * amound, 2)} Rossiya rubli\n🇺🇸 {round(eur_usd * amound, 2)} Aqsh dollari.\n🇰🇿 {round(eur_kzt * amound, 2)} Qozog'iston tengesi."
            await message.answer(text)

        elif currency.lower() == "kzt":
            text = f"🏠 Kiritildi {amound} Qozog'iston tengesi. 🇰🇿\n\n🇺🇿 {round(sum[3] * amound, 2)} O'zbek so'mi.\n🇷🇺 {round(kzt_rub * amound, 2)} Rossiya rubli.\n🇺🇸 {round(kzt_usd * amound, 2)} Aqsh dollari.\n🇪🇺 {round(kzt_eur * amound, 2)} EVRO."
            await message.answer(text)
        elif currency.lower() == "uzs":
            text = f"🏠 Kiritildi {amound} O'zbekiston so'mi. 🇺🇿\n\n🇷🇺 {round(amound / sum[0], 2)} Rossiya rubli.\n🇺🇸 {round(sum[1] / amound, 2)} Aqsh dollari.\n🇪🇺 {round(sum[2] / amound, 2)} EVRO.\n🇰🇿 {round(amound / sum[3], 2)} Qozog'iston tengesi."
            await message.answer(text)


    else:
        await message.reply("Iltimos son kiriting! 😊")
        


        