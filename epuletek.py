from epulet import Epulet

class Epuletek:
    def __init__(self, fajlnev, elvalaszto) -> None:
        self.fajlnev = fajlnev
        self.elvalaszto = elvalaszto
        self.epulet_lista = []

    def beolvas(self):
        with open(self.fajlnev, "r", encoding="utf-8") as fh:
            sor = fh.readline()
            while sor:
                sor = fh.readline()
                if sor:
                    adat = sor.rstrip().split(self.elvalaszto)
                    nev = adat[0]
                    varos = adat[1]
                    orszag = adat[2]
                    magassag = adat[3]
                    emelet = adat[4]
                    epult = adat[5]
                    self.epulet_lista.append(Epulet(nev, varos, orszag, magassag, emelet, epult))

    def epuletek_szama(self):
        return len(self.epulet_lista)

    def magasabb(self, magassag_lab):
        db = 0
        i = 0
        while i < len(self.epulet_lista):
            if self.epulet_lista[i].magassag_lab() > magassag_lab:
                db += 1
            i += 1
        return db

    def legoregebb_orszaga(self):
        idx = 0
        i = 1
        while i < len(self.epulet_lista):
            if self.epulet_lista[i].epult < self.epulet_lista[idx].epult:
                idx = i
            i += 1
        return self.epulet_lista[idx]
