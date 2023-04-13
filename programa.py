# Pirmoji programėlė --version 1.0
import sys

atsakymu_taskai = 0

vardas = input("Koks Jūsų vardas? ")
miestas = input("Iš kokios jūs šalies? ")
print("\033[91m" + "Sveiki, " + vardas + " iš " + miestas + "\033[0m")

print("\033[91m" + "Tai yra testas kuris susideda iš 3 klausimų. Atsakęs į visus klausimus teisingai, galėsi rytoj neiti į paskaitą!" + "\033[0m")

pasiruosimas = input("Ar esate pasiruošę/-s testui? Parašykite Taip arba Ne: ")

if pasiruosimas.lower() == "taip":
    print("Pirmyn, sėkmės!")
else:
    print("Ne tai ne. Iki!")
    sys.exit()

print("\033[91m" + "Pirmas klausimas!" + "\033[0m")
print("\033[91m" + "Kas šiuo metų yra mūsų Lietuvos prezidentas. Įveskite Vardą ir pavardę? P.s nenaudokite lietuviškų raidžių" + "\033[0m")

teisingas_vardas = ("Gitanas Nauseda")
atsakymas = input("Jūsų atstakymas: ")

if atsakymas.lower() == teisingas_vardas.lower():
    print("Teisingai!")
    atsakymu_taskai += 1
else:
    print("Neteisingai")


print("\033[91m" + "Antras klausimas!" + "\033[0m")
print("\033[91m" + "Kiek yra X ?" + "\033[0m")
print("\033[91m" + "34 - 17 = X " + "\033[0m")
teisingas_skaicius = ("17")
atsakymas = input("Jūsų atstakymas: ")

if atsakymas.lower() == teisingas_skaicius.lower():
    print("Teisingai!")
    atsakymu_taskai += 1
else:
    print("Neteisingai")


print("\033[91m" + "Trečias klausimas!" + "\033[0m")
print("\033[91m" + "Kiek yra 1 kilogramas gramais?" + "\033[0m")

teisingas_skaicius_gramais = ("1000")

atsakymas = input("Jūsų atstakymas: ")

if atsakymas.lower() == teisingas_skaicius_gramais.lower():
    print("Teisingai!")
    atsakymu_taskai += 1
else:
    print("Neteisingai")


print("\033[92m" + "Jūs atsakėte: " + str(atsakymu_taskai) + " iš 3 teisingai. Na ką žinau, šaunuolis!" + "\033[0m")
