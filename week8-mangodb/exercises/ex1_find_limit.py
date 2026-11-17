# Mongo shell'deki db.countries1.find().limit(10) sorgusunun Python karşılığı.
import pprint

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["world"]
countries1 = db.countries1

for country in countries1.find().limit(10):
    pprint.pprint(country)
