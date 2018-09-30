from unittest import TestCase
from NumberSequence import NumberSequence


class NumberSequenceTest(TestCase):
    def test_elementMaxMin(self):
        self.assertEqual(NumberSequence().elementMaxMin(""),[0], "Cadena Vacia")
