# countries1 içindeki kıtaların tekrarsız listesini getirir.
# Shell karşılığı: db.countries1.distinct("continent")
# distinct bir alandaki farklı değerleri liste olarak döndürür.
# find'dan farkı: cursor değil, doğrudan Python listesi gelir. O yüzden döngüye gerek yok.

import pprint

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["world"]
countries1 = db.countries1
continents = countries1.distinct("continent")
pprint.pprint(continents)
