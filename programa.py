# Pirmoji programėlė -- Programėlė Testas -- versija 1.0
import sys

atsakymu_taskai = 0

vardas = input("Koks Jūsų vardas? ")
miestas = input("Iš kokios jūs šalies? ")
print("----------------------------------------------------------------------------------------------------------------------------")
print("\033[92m" + "Sveiki, " + vardas + " iš " + miestas + "\033[0m")
print("----------------------------------------------------------------------------------------------------------------------------")
print("\033[91m" + "Tai yra testas kuris susideda iš 3 klausimų. Atsakęs į visus klausimus teisingai, galėsi rytoj neiti į paskaitą!" + "\033[0m")

pasiruosimas = input("\n\nAr esate pasiruošę/-s testui? Parašykite Taip arba Ne: ")

if pasiruosimas.lower() == "taip":
    print("\033[92m" + "Pirmyn! sėkmės!" + "\033[0m")
    print("------------------------------------------------------------------------------------------------------------------------")
else:
    print("Ne tai ne. Iki!")
    sys.exit()

######################################################### Pirmas klausimas #########################################################
print("\033[92m" + "\n\nPirmas klausimas!" + "\033[0m")
print("\033[91m" + "Kas šiuo metu yra mūsų Lietuvos prezidentas. Įveskite Vardą ir pavardę. P.s nenaudokite lietuviškų raidžių" + "\033[0m")

teisingas_vardas = ("Gitanas Nauseda")
atsakymas = input("Jūsų atstakymas: ")

if atsakymas.lower() == teisingas_vardas.lower():
    print("\033[92m" + "\n\n\n\n\n\n\n\n\n---------------------Teisingai!---------------------" + "\033[0m")
    atsakymu_taskai += 1
else:
    print("\033[91m" + "\n\n\n\n\n\n\n\n\n---------------------Neteisingai!---------------------" + "\033[0m")



#########################################################  Antras klausimas  #########################################################
print("\033[92m" + "\n\nAntras klausimas!" + "\033[0m")
print("\033[91m" + "Kiek yra X ?" + "\033[0m")
print("\033[91m" + "34 - 17 = X " + "\033[0m")
teisingas_skaicius = ("17")
atsakymas = input("Jūsų atstakymas: ")

if atsakymas.lower() == teisingas_skaicius.lower():
    print("\033[92m" + "\n\n\n\n\n\n\n\n\n---------------------Teisingai!---------------------" + "\033[0m")
    atsakymu_taskai += 1
else:
    print("\033[91m" + "\n\n\n\n\n\n\n\n\n---------------------Neteisingai!---------------------" + "\033[0m")

#########################################################  Trečias klausimas  #########################################################
print("\033[92m" + "\n\nTrečias klausimas!" + "\033[0m")
print("\033[91m" + "Kiek yra 1 kilogramas gramais?" + "\033[0m")

teisingas_skaicius_gramais = ("1000")

atsakymas = input("Jūsų atstakymas: ")

if atsakymas.lower() == teisingas_skaicius_gramais.lower():
    print("\033[92m" + "\n\n\n\n\n\n\n\n\n---------------------Teisingai!---------------------" + "\033[0m")
    atsakymu_taskai += 1
else:
    print("\033[91m" + "\n\n\n\n\n\n\n\n\n---------------------Neteisingai!---------------------" + "\033[0m")



#########################################################  Atsakymas  #########################################################
print("\033[92m" + "\n\nJūs atsakėte: " + str(atsakymu_taskai) + " iš 3 teisingai. Na ką žinau, šaunuolis!" + "\033[0m")
