from bevezetes import Jatekos
from sorozat import Sorozat
from epuletek import Epuletek

print("I/A:")
j = Jatekos()
j.beker()
print("I/B:")
print("\t" + j.udvozles())

sor = Sorozat()
sor.veletlen_generalas(7)
print(f"II/A, B, C:\n\t{sor.konzol_kiir('-')}")

szoveg = f"\tA fejek száma: {sor.fejek_szama()}"
print("II/D, E:\n" + szoveg)
sor.file_kiir("fejek.txt", "II/F\n" + szoveg)

ep = Epuletek("epulet.txt", "$")
ep.beolvas()

print(f"III/A, B:\n\tAz épületek száma: {ep.epuletek_szama()}")
mag_lab = 555
print(f"III/C:\n\tAz 555 lábnál magasabb épületek száma: {ep.magasabb(mag_lab)}.")

print(f"III/D:\n\tA legöregebb épület országa: {ep.legoregebb_orszaga().orszag}.")
