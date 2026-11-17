# imdb veritabanında her film türünden (genre) kaç film olduğunu sayar.

import pprint

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["imdb"]
movies1 = db.movies1

# Kontrol: veri yoksa sessizce boş çıktı vermek yerine nedenini söylesin.
if movies1.count_documents({}) == 0:
    print("imdb.movies1 boş. Önce movies_v1.json dosyasını mongoimport ile yükle.")
else:
    aggregates = movies1.aggregate(
        [
            {"$project": {"genres": 1}},
            {"$unwind": "$genres"},
            {"$group": {"_id": "$genres.name", "total": {"$sum": 1}}},
        ]
    )
    for agg in aggregates:
        pprint.pprint(agg)

client.close()

# Pipeline üç aşamadan oluşuyor, her aşama bir öncekinin çıktısını alıyor:
# 1) $project: sadece genres alanını tut, gerisini at (SELECT genres gibi)
# 2) $unwind: genres bir dizi. Her türü ayrı belgeye böler.
# 3) türü olan bir film, 3 ayrı belge haline gelir.
# 3) $group: tür adına göre grupla, $sum: 1 ile say (GROUP BY + COUNT(*) gibi)
