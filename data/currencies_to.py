from data.currensy import get_currncy


usd_rub = get_currncy("usd", "rub")['rub']
usd_eur = get_currncy("usd", "eur")['eur']
usd_kzt = get_currncy("usd", "kzt")['kzt']

rub_usd = get_currncy("rub", "usd")['usd']
rub_eur = get_currncy("rub", "eur")['eur']
rub_kzt = get_currncy("rub", "kzt")['kzt']

kzt_rub = get_currncy("kzt", "rub")['rub']
kzt_usd = get_currncy("kzt", "usd")['usd']
kzt_eur = get_currncy("kzt", "eur")['eur']

eur_rub = get_currncy("eur", "rub")['rub']
eur_usd = get_currncy("eur", "usd")['usd']
eur_kzt = get_currncy("eur", "kzt")['kzt']
