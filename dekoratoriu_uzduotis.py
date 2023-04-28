# ###################################################################### Pirma užduotis ######################################################################

# # Sukurkite klasę Studentas su atributais vardas, pavarde ir amzius. Pridėkite tris metodus:

# # pilnas_vardas(): Grąžina pilną studento vardą, naudojant @property dekoratorių.
# # ar_pilnametis(): Grąžina True, jei studento amžius yra didesnis arba lygus 18, ir False, jei ne. Naudokite @staticmethod dekoratorių.
# # sukurti_studenta(cls, vardas: str, pavarde: str, amzius: int): Grąžina naują Studentas objektą. Naudokite @classmethod dekoratorių.
# # Sukurkite keletą studentų objektų, naudojant klasės metodą sukurti_studenta(), ir išbandykite visus metodus.

# class Studentas:
#     def __init__(self, vardas, pavarde, amzius):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.amzius = amzius

#     @property
#     def pilnas_vardas(self):
#         return f"{self.vardas} {self.pavarde}"

#     @staticmethod
#     def ar_pilnametis(amzius):
#         return amzius >= 18

#     @classmethod
#     def sukurti_studenta(cls, vardas: str, pavarde: str, amzius: int):
#         return cls(vardas, pavarde, amzius)


# def create_student():
#     vardas = input("Įveskite vardą: ")
#     pavarde = input("Įveskite pavardę: ")
#     amzius = int(input("Įveskite amžių: "))

#     studentas = Studentas.sukurti_studenta(vardas, pavarde, amzius)
#     return studentas


# studentas1 = Studentas.sukurti_studenta("Jonas", "Jonaitis", 20)
# studentas2 = Studentas.sukurti_studenta("Petras", "Petraitis", 17)

# # Sukurkite studentą naudojant wrapper funkciją
# studentas3 = create_student()

# # Išbandykite visus metodus
# print(studentas1.pilnas_vardas)  # Output: "JONAS JONAITIS"
# print(studentas2.pilnas_vardas)  # Output: "PETRAS PETRAITIS"
# print(f"{studentas3.vardas.capitalize()} {studentas3.pavarde.capitalize()}, {studentas3.amzius} years old, is an adult: {Studentas.ar_pilnametis(studentas3.amzius)}")

# print(Studentas.ar_pilnametis(studentas1.amzius))  # Output: True
# print(Studentas.ar_pilnametis(studentas2.amzius))  # Output: False
# print(Studentas.ar_pilnametis(studentas3.amzius))  # renaldas True nes 32 metai!


# ###################################################################### Antra užduotis ######################################################################
# # Parašykite dekoratorių, kuris:

# # visus dekoruotos funkcijos tekstinius argus ir kwargus paverčia didžiosiomis raidėmis.
# # visus funkcijos teksinius rezultatus paverčia didžiosiomis raidėmis.

# def text_to_uppercase(func):
#     def wrapper(*args, **kwargs):
#         # paverčiame tekstinius argumentus didžiosiomis raidėmis
#         args = [str(arg).upper() for arg in args]
#         kwargs = {k: str(v).upper() for k, v in kwargs.items()}
#         # iškviečiame originalią funkciją ir paverčiame jos rezultatą didžiosiomis raidėmis
#         result = func(*args, **kwargs)
#         return str(result).upper()
#     return wrapper


# @text_to_uppercase
# def pasveikinimas(name):
#     return f"Laba diena, {name}!"

# name = input("What's your name? ")
# greeting = pasveikinimas(name)
# print(greeting)



# def capitalize_names(func):
#     def wrapper(name, last_name, age):
#         name = name.upper()
#         last_name = last_name.upper()
#         return func(name, last_name, age)
#     return wrapper

# @capitalize_names
# def check_if_adult(name, last_name, age):
#     if age >= 18:
#         return f"{name} {last_name} is an adult."
#     else:
#         return f"{name} {last_name} is not an adult yet."

# name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# age = int(input("Enter your age: "))

# print(check_if_adult(name, last_name, age))
