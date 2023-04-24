from zoneinfo import ZoneInfo
from datetime import datetime

# Paprašome vartotojo įvesti laiką
time_str = input("Įveskite laiką HH:MM formatu: ")

# Išskiriame valandas ir minutes
hours, minutes = map(int, time_str.split(":"))

# Paprašome vartotojo įvesti laiko zonos skaičių
print("Pasirinkite laiko zoną:")
print("1 - Sydney'aus")
print("2 - Dubai'aus")
print("3 - Vilniaus")
print("4 - London'o")
print("5 - New York'o")
print("6 - Los Angeles'as")
timezone_num = int(input("Įveskite laiko zonos skaičių: "))

# Nustatome atitinkamą laiko zoną pagal vartotojo pasirinkimą
if timezone_num == 1:
    timezone = ZoneInfo("Australia/Sydney")
elif timezone_num == 2:
    timezone = ZoneInfo("Asia/Dubai")
elif timezone_num == 3:
    timezone = ZoneInfo("Europe/Vilnius")
elif timezone_num == 4:
    timezone = ZoneInfo("Europe/London")
elif timezone_num == 5:
    timezone = ZoneInfo("America/New_York")
elif timezone_num == 6:
    timezone = ZoneInfo("America/Los_Angeles")
else:
    print("Neteisingas laiko zonos skaičius.")
    exit()

# Sukuriame datetime objektą
time = datetime(2023, 4, 24, hours, minutes)

# Spausdiname įvestą laiką skirtingose pasaulio vietose
print("Sydney'aus laikas:", time.astimezone(ZoneInfo("Australia/Sydney")).strftime("%H:%M"))
print("Dubai'aus laikas:", time.astimezone(ZoneInfo("Asia/Dubai")).strftime("%H:%M"))
print("Vilniaus laikas:", time.astimezone(timezone).strftime("%H:%M"))
print("London'o laikas:", time.astimezone(ZoneInfo("Europe/London")).strftime("%H:%M"))
print("New York'o laikas:", time.astimezone(ZoneInfo("America/New_York")).strftime("%H:%M"))
print("Los Angeles'o laikas:", time.astimezone(ZoneInfo("America/Los_Angeles")).strftime("%H:%M"))
