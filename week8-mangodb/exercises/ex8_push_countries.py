# Her kıtanın altına o kıtadaki ülke adlarını liste halinde toplar.

import pprint

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["world"]
countries1 = db.countries1

# $push grubun içindeki her belgenin name değerini bir diziye ekler.
# Ex6'daki $sum sayıyordu, $push ise değerleri topluyor.
countriesByContinent = countries1.aggregate(
    [{"$group": {"_id": "$continent", "countries": {"$push": "$name"}}}]
)

# list() olmadan pprint ediliyor. O haliyle sonuç değil,
# "CommandCursor object" gibi bir satır basar. list() ile cursor'ı açıyoruz.
pprint.pprint(list(countriesByContinent))

client.close()
