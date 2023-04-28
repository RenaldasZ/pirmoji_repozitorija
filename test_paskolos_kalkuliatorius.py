import unittest
from paskolos_kalkuliatorius import PaskolosKalkuliatorius

class TestPaskolosKalkuliatorius(unittest.TestCase):
    def setUp(self):
        # Create a PaskolosKalkuliatorius instance with default input values
        self.paskola = PaskolosKalkuliatorius(10000, 0.05, 5)

    def test_menesio_imoka(self):
        self.assertAlmostEqual(self.paskola.menesio_imoka(), 188.71, places=2)

        # Add more test cases
        paskola = PaskolosKalkuliatorius(20000, 0.03, 10)
        self.assertAlmostEqual(paskola.menesio_imoka(), 193.12, places=2)

        paskola = PaskolosKalkuliatorius(5000, 0.08, 2)
        self.assertAlmostEqual(paskola.menesio_imoka(), 226.14, places=2)

    def test_lyginis_nelyginis(self):
        self.assertEqual(self.paskola.lyginis_nelyginis(2), "Įvestas skaičius yra lyginis.")
        self.assertEqual(self.paskola.lyginis_nelyginis(3), "Įvestas skaičius yra nelyginis.")

if __name__ == '__main__':
    unittest.main()