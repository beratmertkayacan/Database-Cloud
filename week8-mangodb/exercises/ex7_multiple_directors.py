# Birden fazla yönetmeni olan filmleri getirir.
import pprint

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["imdb"]
movies1 = db.movies1

if movies1.count_documents({}) == 0:
    print("imdb.movies1 boş. Önce movies_v1.json dosyasını mongoimport ile yükle.")
else:
    movies = movies1.find(
        {"directors.1": {"$exists": True}}, {"title": 1, "directors": 1, "_id": 0}
    )
    for movie in movies:
        pprint.pprint(movie)

client.close()

# "directors.1" dizinin 1 numaralı elemanı, yani ikinci yönetmen (sayma 0'dan başlar).
# $exists: True "bu alan var mı" diye bakar.
# İkinci yönetmen varsa, filmin en az iki yönetmeni var demektir.
# Week 6 Slayt 66 aynı işi $where ile yapıyordu, bu yazım daha temiz ve hızlı.
