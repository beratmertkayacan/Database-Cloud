# Adı tam 5 karakter olan ülkeleri getirir.
# Shell'deki { name: /^....$/ } sorgusunun (Slayt 13) Python karşılığı.

import pprint
import re  # Python'un regular expression kütüphanesi

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["world"]
countries1 = db.countries1

# ^ başlangıç, .{5} herhangi 5 karakter, $ bitiş.
# Shell'de /^....$/ yazıyorduk, Python'da re.compile ile aynı deseni nesneye çeviriyoruz.
# IGNORECASE büyük küçük harfi önemsememek için, burada sonucu değiştirmiyor.
rge_country_name = re.compile("^.{5}$", re.IGNORECASE)

# Projection'da True = getir, False = getirme (shell'deki 1 ve 0 ile aynı)
countries = countries1.find({"name": rge_country_name}, {"name": True, "_id": False})
for country in countries:
    pprint.pprint(country)

client.close()
