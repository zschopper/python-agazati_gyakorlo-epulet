# Ágazati vizsga Python - 2023

A feladatokat külön modulokban oldja meg, a modulok nevei a feladatokban találhatók! 
A főprogramból (main.py) hívja meg az egyes modulok metódusait a feladatban meghatározott neveikkel (1p)! 
A projektet sajat_nev_ 202302 néven mentse, majd a munkáját sajat_nev_ 202302.zip (Pl.: Nagy_Virag_202302.zip) nevű állományban adja le! (1p)

## 1. feladat:  összesen 7p szerezhető, a modul neve: bevezetes.py

**minta**  
(a stílus kialakítása nem része a feladatnak, de a sorszámok és betűjelek kiíratása igen):

```
I/A:
    Játékos neve: Gandalf 
    szerepkör: varázsló 
 
I/B:
    Üdvözlünk Gandalf, 2 életed van!  
```

A. Kérje be az alábbi adatokat a fenti mintának megfelelően:  
  Játékos neve és szerepköre!  (2p)  
B. A program az adatbekérés után írasson ki egy üdvözlést az alábbiak alapján!  
    Amennyiben „varázsló” a játékosunk, 2 élete van.  
    Amennyiben „harcos” a játékosunk, 10 életereje van.  
    Amennyiben ismeretlen a játékosunk szerepköre, 8 életereje van. (4p)  
    A **mintának megfelelően** jelenítette meg az eredményt, és kérte be az adatokat. (1p)  
 
## **2. feladat:**  összesen **14p** szerezhető, a modul neve: **sorozat.py**

**minta:**

```
II/A, B, C:
    FEJ-ÍRÁS-ÍRÁS-ÍRÁS-FEJ-ÍRÁS-ÍRÁS

II/D, E:
    A fejek száma: 2.

A fejek.txt tartalma:

II/F:
    A fejek száma: 2.
```

A. Írasson ki a konzolra kötőjellel (-) elválasztva 7 pénzérmével való dobást véletlen számsorozat alapján a mintának megfelelően! (4p)  
B. A generált értékeket tárolja lista adatszerkezetben logikai típusokkal (0: írás, 1: fej)! (1p)  
C. A „–” jel csak az értékek között szerepeljen (a végén ne)! (2p)  
D. Írjon függvényt fejek_szama néven, amiben számolja meg, hogy hány olyan elem van, ami fej (1). A visszatérési érték legyen egy egész szám! (3p)  
E. A fejek_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_kiir nevű metódusban fogalmazzon meg! (2p)  
F. A fejek_szama függvény eredményét írassa ki a mintának megfelelően a fejek.txt nevű fájlba, amit file_kiir nevű metódusban fogalmazzon meg! (2p)  
 
## 3. feladat:    összesen 17p szerezhető, a modul neve: epuletek.py

Az epulet.txt forrásállomány, épületek adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
Az epulet.txt állomány szerkezete:

* az épület neve: pl: Centrum LIM
* az épület városa: pl.: Varsó
* az épület országa: pl.: Lengyelország
* az épület magassága m-ben: pl.: 140
* az épület emeleteinek a száma, pl.: 43
* az épület építésének az éve, pl.1949

Az állomány első sora a mezőneveket tartalmazza „$” jellel elválasztva.
A megoldás mintája:

```
III/A, B:
    Az épületek száma: 8

III/C:
    Az 555 lábnál magasabb épületek száma: 2.

III/D:
    A legöregebb épület országa: Lengyelország.
```

A. Olvassa be **osztály** segítségével (utóbbit hozza létre **külön modulban**) a epulet.txt fájlból a játékosok adatait, és **tárolja el** összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)  
B. Írassa ki az **épületek számát** a mintának megfelelően a konzolra! (2p)  
C. Adja meg az **555 lábnál magasabb épületek számát**, ha 1 m = 3.280839895 láb! (4p)  
D. Írassa ki konzolra a mintának megfelelően a **legöregebb épület** (ha több is van, akkor az első legöregebb adatait) **országát**. (4p)  
