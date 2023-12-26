from tkinter import *
from  tkinter import ttk
import sqlite3

baglanti = sqlite3.connect("BilgeDÖĞÜCÜ.db")
sorgu = baglanti.cursor()
sonuc = sorgu.execute("SELECT * FROM Eser")

pencere  = Tk()
pencere.title('Katalog: Eserleri Listele')
pencere.geometry('800x300')
pencere.resizable = True
pencere['bg'] = '#FBE54E'

eserTabloCercevesi = ttk.Frame(pencere, padding=25)
eserTabloCercevesi.pack()

eserTablosu = ttk.Treeview(eserTabloCercevesi)

eserTablosu['columns'] = ('eserISBN', 'eserAdi', 'eserBasimYeri', 'eserSayfaSayısı', 'eserDili')

eserTablosu.column("#0", width=0,  stretch=NO)
eserTablosu.column("eserISBN",anchor=CENTER, width=130)
eserTablosu.column("eserAdi",anchor=CENTER,width=250)
eserTablosu.column("eserBasimYeri",anchor=CENTER,width=130)
eserTablosu.column("eserSayfaSayısı",anchor=CENTER,width=150)
eserTablosu.column("eserDili",anchor=CENTER,width=100)

eserTablosu.heading("#0",text="",anchor=CENTER)
eserTablosu.heading("eserISBN",text="Eser ISBN",anchor=CENTER)
eserTablosu.heading("eserAdi",text="Eser Adı",anchor=CENTER)
eserTablosu.heading("eserBasimYeri",text="Eser Basım Yeri",anchor=CENTER)
eserTablosu.heading("eserSayfaSayısı",text="Eser Sayfa Sayısı",anchor=CENTER)
eserTablosu.heading("eserDili",text="Eser Dili",anchor=CENTER)

for index, eser in enumerate(sonuc.fetchall()):
    eserTablosu.insert(parent='',index='end',iid=index,text='',
    values=(eser[1],eser[3],eser[4],eser[6],eser[7]))

eserTablosu.pack()
pencere.mainloop()