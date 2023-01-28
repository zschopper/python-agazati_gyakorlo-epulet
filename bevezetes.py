'''
A.	Kérje be az alábbi adatokat a fenti mintának megfelelően:
Játékos neve és szerepköre!  (2p)

B.	A program az adatbekérés után írasson ki egy üdvözlést az alábbiak alapján!
Amennyiben „varázsló” a játékosunk, 2 élete van.
Amennyiben „harcos” a játékosunk, 10 életereje van.
Amennyiben ismeretlen a játékosunk szerepköre, 8 életereje van. (4p)
A mintának megfelelően jelenítette meg az eredményt, és kérte be az adatokat. (1p)
'''

class Jatekos:
    def __init__(self) -> None:
        self.nev = ""
        self.szerepkor = ""
        self.eletero = ""

    def beker(self):
        self.nev = input("\tJátékos neve: ")
        self.szerepkor = input("\tszerepkör: ")
        self.szamol()

    def szamol(self):
        match self.szerepkor.lower():
            case "varázsló":
                self.eletero = 2
            case "harcos":
                self.eletero = 10
            case "_":
                self.eletero = 8

    def udvozles(self):
        return f"Üdvözlünk {self.nev}, {self.eletero} életed van!"
