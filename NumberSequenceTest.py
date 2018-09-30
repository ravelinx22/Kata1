from unittest import TestCase
from NumberSequence import NumberSequence


class NumberSequenceTest(TestCase):
    def test_elementMaxMinI1(self):
        self.assertEqual(NumberSequence().elementMaxMin(""),[0], "Cadena Vacia")

    def test_elementMaxMinI1UnNumero(self):
        self.assertEqual(NumberSequence().elementMaxMin("1"), [1], "1 numero")

    def test_elementMaxMinI1DosNumero(self):
        self.assertEqual(NumberSequence().elementMaxMin("1,2"), [2], "2 numero")

    def test_elementMaxMinI1NNumero(self):
        self.assertEqual(NumberSequence().elementMaxMin("1, 3, 6, 5, 8, 4, 2, 7, 0"), [9], "N numeros")

