# https://github.com/laplaceshrugged/lab10-AR-DC.git
# Partner 1: Adityaa Ravi
# Partner 2: Dev Castillo

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(-1, -2), 1)
        self.assertEqual(subtract(0, 0), 0)

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(4,6), 24)
        self.assertEqual(mul(-2,0), 0)
        self.assertEqual(mul(-6,-7), 42)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,10), 5)
        self.assertEqual(div(-2,0),0)
        self.assertEqual(div(-7,-91),13)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(100, 10), 0.5)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(2, 2), 1)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(100, 0)
    # ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(7,-343)
    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(-3,-4),5)
        self.assertEqual(hypotenuse(0,14),14)
        self.assertEqual(hypotenuse(-40,9),41)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError): 
            square_root(-4761)
        self.assertEqual(square_root(0),0)
        self.assertEqual(square_root(1681),41)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
