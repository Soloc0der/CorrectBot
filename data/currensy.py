import requests



def get_currncy(cur1, cur2):
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{cur1}/{cur2}.json"
    response = dict(requests.get(url).json())
    return response



def get_all_curencies():
    rub = get_currncy("rub", "uzs")['uzs']
    usd = get_currncy("usd", "uzs")['uzs']
    eur = get_currncy("eur", "uzs")['uzs']
    kzt = get_currncy("kzt", "uzs")['uzs']

    return rub, usd, eur, kzt

def get_currencies_data():
    data = get_currncy("rub", "uzs")['date']
    return data
    
    
def get_curency_text():
    data = get_currencies_data()
    curency = list(get_all_curencies())


    text = f"\n\n🇷🇺 1 Rossiya rubli = {round(curency[0], 2)} so'm 🇺🇿\n🇺🇸 1 Aqsh dollari = {round(curency[1], 2)} so'm 🇺🇿\n🇪🇺 1 EVRO = {round(curency[2], 2)} so'm 🇺🇿\n🇰🇿 1 Qozog'iston tengesi = {round(curency[3], 2)} so'm 🇺🇿"
    return text






def cheaking_numbers(amound):
    cheak = "0123456789."
    #cheakig float text

    cheak_numb = 0
    for cheaking in amound:
        if cheaking in cheak:
            cheak_numb +=1
        else:
            cheak_numb -=1
        
    if cheak_numb == len(amound):
        return True
    else:
        return False
    

