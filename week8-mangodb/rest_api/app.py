import json

from flask import Flask, Response, jsonify
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["world"]
countries1 = db.countries1

app = Flask(__name__)


@app.route("/world/api/v1.0/countries/<code>", methods=["GET"])
def countryByCode(code):
    return jsonify(countries1.find_one({"_id": code}))


@app.route("/world/api/v1.0/countries", methods=["GET"])
def countries():
    data = json.dumps([e for e in countries1.find({})], ensure_ascii=False)
    return Response(data, mimetype="application/json")


if __name__ == "__main__":
    app.run(port=5001, debug=True)

# AIN3003 Week 7 ve 8, Slayt 44: Flask ile REST API örneği
# countries1 verisini HTTP üzerinden dışarı açan küçük bir data service.
# İki endpoint var:
#   GET /world/api/v1.0/countries         tüm ülkeler
#   GET /world/api/v1.0/countries/<code>  tek ülke, örnek: /world/api/v1.0/countries/TUR


# MongoDB bağlantısı, alıştırmalardaki ile aynı.
# Uygulama açılırken bir kez kuruluyor, her istekte yeniden bağlanılmıyor.

# Flask uygulamasını oluştur. __name__ Flask'a bu dosyanın nerede olduğunu söylüyor.

# Item kalıbı (Slayt 36: GET /container/item): tek bir kaynağı ID'siyle okur.
# <code> URL'deki değişken kısım. /countries/TUR çağrılınca code = "TUR" olur.
# REST'in "Give everything an ID" ilkesi (Slayt 28): her ülkenin kendi adresi var.

# find_one tek belge döndürür, bulamazsa None döner.
# Bizim veride _id ülke kodu ("TUR") olduğu için doğrudan _id ile arıyoruz.
# jsonify Python sözlüğünü JSON'a çevirip doğru Content-Type ile döndürür.

## Container kalıbı (Slayt 36: GET /container): koleksiyonun tamamını listeler.

# find({}) bütün belgeleri getirir, list comprehension cursor'ı listeye çevirir.
# Slaytta sadece json.dumps(...) döndürülüyor. O haliyle tarayıcıya JSON değil
# düz metin (text/html) olarak gider. Slaytta import edilip kullanılmayan Response ile
# içerik tipini application/json yaptım (Slayt 33: Support multiple representations).

# debug=True: kodu kaydedince sunucu kendini yeniden başlatır, hataları tarayıcıda gösterir.
