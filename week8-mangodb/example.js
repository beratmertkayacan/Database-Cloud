// Çalıştırma (week8-mangodb klasörünün içindeyken):
//   mongosh world example.js
// "world" kısmı bağlanılacak veritabanı. Script içinde "use" yazmaya gerek kalmıyor.
// mongosh script modunda sonuçları kendiliğinden ekrana basmıyor,

function baslik(metin) {
    print("\n==================================================");
    print(metin);
    print("==================================================");
  }

  baslik("Kontrol: countries1 içinde kaç belge var? (beklenen 239)");
  print(db.countries1.countDocuments());


  //nüfusu 50 milyondan fazla olan ülke sayısı

  baslik("Slayt 7: nüfusu 50 milyonun üstündeki ülke sayısı (slaytta 24)");
  print(db.countries1.find({ population: { $gt: 50000000 } }, { name: true }).count());

  print(db.countries1.countDocuments({ population: { $gt: 50000000 } }));


  //nüfusu 50 ile 100 milyon arasında olan ülkeler
  baslik("Slayt 8: nüfusu 50 ile 100 milyon arası ülkeler");
  printjson(
    db.countries1.find(
      { population: { $gt: 50000000, $lt: 100000000 } },
      { name: true }
    ).toArray()
  );


  //içinde Istanbul ya da New York şehri olan ülkeler
  baslik("Slayt 9a: slayttaki yazım, cities.city.name (bu dosyada boş döner)");
  printjson(
    db.countries1.find(
      { "cities.city.name": { $in: ["Istanbul", "New York"] } },
      { name: true }
    ).toArray()
  );


  baslik("Slayt 9b: bizim dosyaya uygun yazım, cities.name (TUR ve USA beklenir)");
  printjson(
    db.countries1.find(
      { "cities.name": { $in: ["Istanbul", "New York"] } },
      { name: true }
    ).toArray()
  );


  //tekrarsız kıta listesi

  baslik("Slayt 10: distinct continent");
  printjson(db.countries1.distinct("continent"));


  //kıtaya göre ülke sayısı
  // aggregate bir pipeline alır, her aşama bir öncekinin çıktısını işler.
  // $group ile _id alanına göre gruplanır, $sum: 1 her belge için 1 ekleyerek sayar
  // (SQL'deki GROUP BY continent + COUNT(*) gibi).
  baslik("Slayt 11 ve 12: kıtaya göre ülke sayısı");
  printjson(
    db.countries1.aggregate([
      { $group: { _id: "$continent", count: { $sum: 1 } } }
    ]).toArray()
  );


  //adı tam 4 harften oluşan ülkeler
  // /^....$/ bir regular expression: ^ başlangıç, her nokta bir karakter, $ bitiş.
  // Projection'da 1 = getir, 0 = getirme. _id varsayılan olarak geldiği için kapatılmalı.
  baslik("Slayt 13: adı 4 harfli ülkeler");
  printjson(
    db.countries1.find(
      { name: /^....$/ },
      { name: 1, _id: 0 }
    ).toArray()
  );


  //Asya'nın en kalabalık 10 ülkesi
  // sort({ population: -1 }) büyükten küçüğe sıralar (1 olsaydı küçükten büyüğe).
  // limit(10) ilk 10 sonucu alır (SQL'deki ORDER BY ... DESC LIMIT 10 gibi).
  baslik("Slayt 14: Asya, nüfusa göre ilk 10");
  printjson(
    db.countries1.find(
      { continent: "Asia" },
      { name: 1, population: 1, _id: 0 }
    ).sort({ population: -1 }).limit(10).toArray()
  );


  //sayfalama (pagination)
  // skip(10) ilk 10 sonucu atlar, limit(10) sonraki 10'u alır. Yani 2. sayfa.
  // Sayfa n için formül: skip((n - 1) * sayfaBoyutu).limit(sayfaBoyutu)
  baslik("Slayt 15: Asya, nüfusa göre 11. ile 20. sıradakiler");
  printjson(
    db.countries1.find(
      { continent: "Asia" },
      { name: 1, population: 1, _id: 0 }
    ).sort({ population: -1 }).skip(10).limit(10).toArray()
  );

  print("\nBitti.");
