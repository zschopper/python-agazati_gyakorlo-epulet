'''
A.	Írasson ki a konzolra kötőjellel (-) elválasztva 7 pénzérmével való dobást véletlen számsorozat alapján a mintának megfelelően! (4p)
B.	A generált értékeket tárolja lista adatszerkezetben logikai típusokkal (0: írás, 1: fej)! (1p)
C.	A „–” jel csak az értékek között szerepeljen (a végén ne)! (2p)
D.	Írjon függvényt fejek_szama néven, amiben számolja meg, hogy hány olyan elem van, ami fej (1). A visszatérési érték legyen egy egész szám! (3p)
E.	A fejek_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_kiir nevű metódusban fogalmazzon meg! (2p)
F.	A fejek_szama függvény eredményét írassa ki a mintának megfelelően a fejek.txt nevű fájlba, amit file_kiir nevű metódusban fogalmazzon meg! (2p)
'''

from random import random
class Sorozat:

    def __init__(self) -> None:
        self.dobasok = []

    nevek = ["ÍRÁS", "FEJ"]

    def veletlen_generalas(self, db):
        self.dobasok = []
        while len(self.dobasok) < db:
            self.dobasok.append(int(random() * 2))

    def fejek_szama(self):
        i = 0
        db = 0
        while i < len(self.dobasok):
            if self.dobasok[i] == 1:
                db += 1
            i += 1
        return db

    def konzol_kiir(self, elvalaszto):
        szoveg = ""
        if len(self.dobasok) > 0:
            szoveg = Sorozat.nevek[self.dobasok[0]]
            i = 1
            while i < len(self.dobasok):
                szoveg += elvalaszto + Sorozat.nevek[self.dobasok[i]]
                i += 1
        return szoveg

    def file_kiir(self, fajlnev, szoveg):
        fh = open(fajlnev, "w", encoding="utf-8")
        fh.write(szoveg)
        fh.close()
