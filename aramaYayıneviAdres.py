import sqlite3

con = sqlite3.connect("BilgeDÖĞÜCÜ.db")
cur = con.cursor()

yay = cur.execute("SELECT DISTINCT UPPER(SUBSTR(yayıneviAdresi, 1, 1)) || SUBSTR(yayıneviAdresi, 2) FROM Yayınevi ORDER BY yayıneviAdresi")
yayListe = yay.fetchall()

print("Yayınevi Adresi listesi:")
for count, yaySatir in enumerate(yayListe):
    print(str(count+1) +" - "+ yaySatir[0])

yayıneviAdresi = int(input("Lütfen yayınevi adresi giriniz: "))

if yayıneviAdresi == 1:
    secilenYayınevi = "İstanbul"
elif yayıneviAdresi == 2:
    secilenKategori = "Eskişehir"
else:
    print("Seçim Hatalı..!")

res = cur.execute(
    "SELECT * FROM Yayınevi WHERE yayıneviAdresi = '{}'".format(secilenYayınevi)
)

veriler = res.fetchall()
for satir in veriler:
    print(satir)
print("Toplam kayıt sayısı " + str(len(veriler)))