import unittest

from FrenchNumberConverter.converter import Converter


class TestFrenchNumberConverterBadInput(unittest.TestCase):
    """
    Test that it throws an error if the input is not an integer
    """

    def test_bad_input_str(self):
        """
        Test that it throws an error if the input is not an integer (string)
        """
        with self.assertRaises(ValueError):
            Converter.convert("test")

    def test_bad_input_float(self):
        """
        Test that it throws an error if the input is not an integer (float)
        """
        with self.assertRaises(ValueError):
            Converter.convert(0.5)

    def test_bad_input_negative_integer(self):
        """
        Test that it throws an error if the input is not an integer (float)
        """
        with self.assertRaises(ValueError):
            Converter.convert(-2)


class TestFrenchNumberConverterUnits(unittest.TestCase):
    """
    Test that it returns the correct result if it is given a number between 0 and 9
    """

    def test_zero(self):
        """
        Test that it returns 'zéro' if the input is 0
        """
        self.assertEqual(Converter.convert(0), "zéro")

    def test_one(self):
        """
        Test that it returns 'un' if the input is 1
        """
        self.assertEqual(Converter.convert(1), "un")

    def test_five(self):
        """
        Test that it returns 'cinq' if the input is 5
        """
        self.assertEqual(Converter.convert(5), "cinq")


class TestFrenchNumberConverterTens(unittest.TestCase):
    """
    Test that it returns the correct result if it is given a number between 10 and 99
    """

    def test_ten(self):
        """
        Test that it returns 'dix' if the input is 10
        """
        self.assertEqual(Converter.convert(10), "dix")

    def test_eleven(self):
        """
        Test that it returns 'onze' if the input is 11
        """
        self.assertEqual(Converter.convert(11), "onze")

    def test_fifteen(self):
        """
        Test that it returns 'quinze' if the input is 15
        """
        self.assertEqual(Converter.convert(15), "quinze")

    def test_nineteen(self):
        """
        Test that it returns 'dix-neuf' if the input is 19
        """
        self.assertEqual(Converter.convert(19), "dix-neuf")

    def test_twenty(self):
        """
        Test that it returns 'vingt' if the input is 20
        """
        self.assertEqual(Converter.convert(20), "vingt")

    def test_twenty_one(self):
        """
        Test that it returns 'vingt-et-un' if the input is 21
        """
        self.assertEqual(Converter.convert(21), "vingt-et-un")

    def test_thirty(self):
        """
        Test that it returns 'trente' if the input is 30
        """
        self.assertEqual(Converter.convert(30), "trente")

    def test_trente_cinq(self):
        """
        Test that it returns 'trente cinq' if the input is 35
        """
        self.assertEqual(Converter.convert(35), "trente-cinq")

    def test_fifty(self):
        """
        Test that it returns 'cinquante' if the input is 50
        """
        self.assertEqual(Converter.convert(50), "cinquante")

    def test_fifty_one(self):
        """
        Test that it returns 'cinquante un' if the input is 51
        """
        self.assertEqual(Converter.convert(51), "cinquante-et-un")

    def test_sixty_eight(self):
        """
        Test that it returns 'soixante huit' if the input is 68
        """
        self.assertEqual(Converter.convert(68), "soixante-huit")

    def test_seventy(self):
        """
        Test that it returns 'soixante-dix' if the input is 70
        """
        self.assertEqual(Converter.convert(70), "soixante-dix")

    def test_seventy_five(self):
        """
        Test that it returns 'soixante-dix cinq' if the input is 75
        """
        self.assertEqual(Converter.convert(75), "soixante-quinze")

    def test_ninety_nine(self):
        """
        Test that it returns 'quatre vingt-dix sept' if the input is 99
        """
        self.assertEqual(Converter.convert(99), "quatre-vingt-dix-neuf")


if __name__ == "__main__":
    unittest.main()
