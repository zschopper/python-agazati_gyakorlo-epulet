class Epulet:
    def __init__(self, nev, varos, orszag, magassag, emelet, epult) -> None:
        self.nev = nev
        self.varos = varos
        self.orszag = orszag
        self.magassag = float(magassag.replace(",", "."))
        self.emelet = int(emelet)
        self.epult = int(epult)

    def magassag_lab(self):
        return self.magassag * 3.280839895
