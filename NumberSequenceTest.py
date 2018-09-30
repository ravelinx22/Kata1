from unittest import TestCase
from NumberSequence import NumberSequence


class NumberSequenceTest(TestCase):
    # Iteracion 1
    def test_elementMaxMinI1(self):
        ans = NumberSequence().elementMaxMin("")
        self.assertEqual(ans[0], 0, "Cadena Vacia")

    def test_elementMaxMinI1UnNumero(self):
        ans = NumberSequence().elementMaxMin("1")
        self.assertEqual(ans[0], 1, "1 numero")

    def test_elementMaxMinI1DosNumero(self):
        ans = NumberSequence().elementMaxMin("1,2")
        self.assertEqual(ans[0], 2, "2 numero")

    def test_elementMaxMinI1NNumero(self):
        ans = NumberSequence().elementMaxMin("1,2,3,4,5,6,7,8,9")
        self.assertEqual(ans[0], 9, "N numeros")

    # Iteracion 2
    def test_elementMaxMinI2(self):
        ans = NumberSequence().elementMaxMin("")
        self.assertEqual(ans[1], None, "Cadena Vacia")

    def test_elementMaxMinI2UnNumero(self):
        ans = NumberSequence().elementMaxMin("1")
        self.assertEqual(ans[1], 1, "1 numero")

    def test_elementMaxMinI2DosNumero(self):
        ans = NumberSequence().elementMaxMin("0,1")
        self.assertEqual(ans[1], 0, "2 numero")

    def test_elementMaxMinI2NNumero(self):
        ans = NumberSequence().elementMaxMin("4,5,6,7,8,9,10,11,12")
        self.assertEqual(ans[1], 4, "N numeros")

    # Iteracion 3
    def test_elementMaxMinI3(self):
        ans = NumberSequence().elementMaxMin("")
        self.assertEqual(ans[2], None, "Cadena Vacia")

    def test_elementMaxMinI3UnNumero(self):
        ans = NumberSequence().elementMaxMin("1")
        self.assertEqual(ans[2], 1, "1 numero")

    def test_elementMaxMinI3DosNumero(self):
        ans = NumberSequence().elementMaxMin("1,2")
        self.assertEqual(ans[2], 2, "2 numero")
