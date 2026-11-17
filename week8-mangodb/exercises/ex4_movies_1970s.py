# 1970 ile 1979 arasındaki filmleri yıla göre yeniden eskiye,
# aynı yılın içinde de ada göre A'dan Z'ye sıralar.

import pprint

import pymongo  # DESCENDING ve ASCENDING sabitleri için
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["imdb"]
movies1 = db.movies1

if movies1.count_documents({}) == 0:
    print("imdb.movies1 boş. Önce movies_v1.json dosyasını mongoimport ile yükle.")
else:
    movies = movies1.find(
        {"year": {"$gte": 1970, "$lt": 1980}}, {"title": 1, "year": 1, "_id": 0}
    ).sort([("year", pymongo.DESCENDING), ("title", pymongo.ASCENDING)])
    for movie in movies:
        pprint.pprint(movie)

client.close()

# $gte = büyük eşit, $lt = küçük. Yani 1970 dahil, 1980 hariç.
# İkinci süslü parantez projection: title ve year gelsin, _id gelmesin.
# Python'da sort, shell'den farklı olarak (alan, yön) çiftlerinden oluşan bir liste alır.
# Shell karşılığı: .sort({year: -1, title: 1})
