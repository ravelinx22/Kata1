from unittest import TestCase
from NumberSequence import NumberSequence


class NumberSequenceTest(TestCase):
    def test_elementMaxMinI1(self):
        self.assertEqual(NumberSequence().elementMaxMin(""),[0], "Cadena Vacia")

    def test_elementMaxMinI1UnNumero(self):
        self.assertEqual(NumberSequence.elementMaxMin("1"), [1], "1 numero")
