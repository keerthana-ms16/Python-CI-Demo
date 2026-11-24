
import unittest
from main import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers
)


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add_numbers(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(subtract_numbers(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(multiply_numbers(10, 5), 50)

    def test_division(self):
        self.assertEqual(divide_numbers(10, 5), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)


if __name__ == "__main__":
    unittest.main()
