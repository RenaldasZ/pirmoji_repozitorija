class PaskolosKalkuliatorius:
    def __init__(self, paskolos_dydis, metines_palukanos, terminas):
        # Initialize the object with input values
        self.paskolos_dydis = paskolos_dydis
        self.metines_palukanos = metines_palukanos
        self.terminas = terminas

    def menesio_imoka(self):
        # Calculate the monthly payment based on input values
        n = self.terminas * 12  # number of months
        r = self.metines_palukanos / 12  # monthly interest rate
        k = (1 + r) ** n
        m = self.paskolos_dydis * (r * k) / (k - 1)  # monthly payment
        return m
    
    def lyginis_nelyginis(self, skaicius):
        if skaicius % 2 == 0:
            return "Įvestas skaičius yra lyginis."
        else:
            return "Įvestas skaičius yra nelyginis."



paskola = PaskolosKalkuliatorius(10000, 0.05, 5)

print(paskola.lyginis_nelyginis(2))
# Output: Įvestas skaičius yra lyginis.

print(paskola.lyginis_nelyginis(3))
# Output: Įvestas skaičius yra nelyginis.

