# Her kıtada kaç ülke olduğunu sayar.
# Shell karşılığı: db.countries1.aggregate([{ $group: ... }])

import pprint

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["world"]
countries1 = db.countries1

pipeline = [{"$group": {"_id": "$continent", "count": {"$sum": 1}}}]

# aggregate de find gibi cursor döndürür. list() ile hepsini bir listeye topluyoruz.
countryCountsByContinent = list(countries1.aggregate(pipeline))
pprint.pprint(countryCountsByContinent)

client.close()

# $group aşaması: _id hangi alana göre gruplanacağını söyler.
# "$continent" başındaki $ işareti "bu bir alan adı" demek, düz metin değil.
# count: { $sum: 1 } her belge için 1 ekler, yani sayar.
