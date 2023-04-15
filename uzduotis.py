krepselis = 0


# Produktu menu
mesa = {"jautiena", "kiauliena", "vistiena"}
darzoves = {"brokolis", "morkos", "pomidorai"}
pieno = {"jogurtas", "pienas", "sūris"}

# Produktu aprasymas
jautiena = {"name": "jautiena", "Kaina": 15.99, "Kcal": 250, "Galiojimo laikas": "2023-04-30"}
kiauliena = {"name": "vistiena", "Kaina": 10.99, "Kcal": 200, "Galiojimo laikas": "2023-04-25"}
vistiena = {"name": "kiauliena", "Kaina": 12.99, "Kcal": 220, "Galiojimo laikas": "2023-04-27"}

brokolis = {"name": "morkos", "Kaina": 2.99, "Kcal": 50, "Galiojimo laikas": "2023-04-26"}
morkos = {"name": "brokolis", "Kaina": 3.99, "Kcal": 70, "Galiojimo laikas": "2023-04-28"}
pomidorai = {"name": "pomidorai", "Kaina": 1.99, "Kcal": 30, "Galiojimo laikas": "2023-04-23"}

jogurtas = {"name": "pienas", "Kaina": 1.99, "Kcal": 120, "Galiojimo laikas": "2023-04-25"}
pienas = {"name": "sūris", "Kaina": 3.99, "Kcal": 150, "Galiojimo laikas": "2023-04-28"}
sūris = {"name": "jogurtas", "Kaina": 2.99, "Kcal": 100, "Galiojimo laikas": "2023-05-01"}

# Produktu list'as
produktai = [jautiena, vistiena, kiauliena, morkos, brokolis, pomidorai, pienas, sūris, jogurtas]

# paversti sarasa nuo a-z
sorted_mesa = sorted(mesa)
sorted_darzoves = sorted(darzoves)
sorted_pieno = sorted(pieno)


while True:
    print("Pasirinkite gaminį:")
    print("1 - Mesos gaminiai")
    print("2 - Daržovės")
    print("3 - Pieno gaminiai")
    print("0 - Baigti")
    
    pasirinkimas = input("Įvesk pasirinkimo numeri: ")

    
    if pasirinkimas == "1":
        print(f"Tu pasirinkai mesos gaminius: {sorted_mesa}")

        antras_pasirinkimas = input("Pasirinkite (1,2,3) arba 0 - jei nenorite nieko pasirinkti: ")

        if antras_pasirinkimas == "0":
            break

        elif antras_pasirinkimas in {"1", "2", "3"}:
            print(f"Tu pasirinkai: {list(mesa)[int(antras_pasirinkimas) - 1]}")
            if antras_pasirinkimas == "1":
                print(jautiena)
                print("1 - ideti i krepseli")
                print("2 - isimti is krepselio")
                trecias_pasirinkimas = input("tavo pasirinkimas: ")

            if trecias_pasirinkimas in {"1"}:            
                krepselis += 1
                print('tavo krepselyje yra' [krepselis])

            if antras_pasirinkimas == "2":
                print(vistiena)
            if antras_pasirinkimas == "3":
                print(kiauliena)
            break




    elif pasirinkimas == "2":
        print(f"Tu pasirinkai: {darzoves}")
        antras_pasirinkimas = input("Pasirinkite antrą gaminį (1-3) arba 0, jei nenorite nieko pasirinkti: ")
        if antras_pasirinkimas == "0":
            break
        elif antras_pasirinkimas in {"1", "2", "3"}:
            print(f"Tu pasirinkai: {list(darzoves)[int(antras_pasirinkimas) - 1]}")
            if antras_pasirinkimas == "3":
                print(morkos)
            if antras_pasirinkimas == "2":
                print(brokolis)
            if antras_pasirinkimas == "1":
                print(pomidorai)
            break




    elif pasirinkimas == "3":
        print(f"Tu pasirinkai: {pieno}")
        antras_pasirinkimas = input("Pasirinkite antrą gaminį (1-3) arba 0, jei nenorite nieko pasirinkti: ")
        if antras_pasirinkimas == "0":
            break
        elif antras_pasirinkimas in {"1", "2", "3"}:
            print(f"Tu pasirinkai: {list(pieno)[int(antras_pasirinkimas) - 1]}")
            if antras_pasirinkimas == "3":
                print(pienas)
            if antras_pasirinkimas == "2":
                print(sūris)
            if antras_pasirinkimas == "1":
                print(jogurtas)
            break
        else:
            print("Neteisingas pasirinkimo numeris. Bandykite dar kartą.")





