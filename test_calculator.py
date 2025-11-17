# https://github.com/sanjaymohan207-star/lab11-SM-JE
# Partner 1: Sanjay Mohan
# Partner 2: Jessalyn Escobar
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0.5, 0.25), 0.75)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)
    ##########################

    ######## Partner 1
    def test_multiply(self) -> None:
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(4, 7), 28)

    def test_divide(self) -> None:
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-9, 3), -3)
        self.assertEqual(div(3, 1), 3)


    ######## Partner 2
    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self) -> None:
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(3, 9), 2.0)

    def test_log_invalid_base(self) -> None:
        with self.assertRaises(ValueError):
            log(1, 10)
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self) -> None:
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self) -> None:
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(-3, -4), 5)

    def test_sqrt(self) -> None:
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(25), 5)
    ##########################


if __name__ == "__main__":
    unittest.main()

# end of file
