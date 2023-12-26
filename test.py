import sqlite3

#Veritabanı ile bağlantının kurulması
con = sqlite3.connect("BilgeDÖĞÜCÜ.db")
cur = con.cursor()

#Sorgulama
res = cur.execute("SELECT * FROM Eser")

#Sorgulama Sonuçlarının görüntülenmesi
for eser in res.fetchall():
    print(eser)