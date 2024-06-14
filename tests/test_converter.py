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


# class TestFrenchNumberConverterTens(unittest.TestCase):
#     """
#     Test that it returns the correct result if it is given a number between 10 and 99
#     """

#     def test_ten(self):
#         """
#         Test that it returns 'zéro' if the input is 0
#         """
#         self.assertEqual(Converter.convert(10), "zéro")


if __name__ == "__main__":
    unittest.main()
