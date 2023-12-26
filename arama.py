import sqlite3

con = sqlite3.connect("BilgeDÖĞÜCÜ.db")
cur = con.cursor()

anahtar = input("Anahtar kelimeyi giriniz: ")

res = cur.execute(
    "SELECT * FROM Yazar WHERE yazarAdı LIKE('%{}%') OR yazarSoyadı LIKE('%{}%') ".format(anahtar,anahtar)
)
veriler = res.fetchall()
for satir in veriler:
    print(satir)