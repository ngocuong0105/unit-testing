'''
Name of file shou
'''
import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, -5), -6)
        self.assertEqual(calc.add(10, -5), 5)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, -5), 4)
        self.assertEqual(calc.subtract(10, -5), 15)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, -5), 5)
        self.assertEqual(calc.multiply(10, -5), -50)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, -5), 0.2)
        self.assertEqual(calc.divide(10, -5), -2)

        # testing exceptions
        # test will pass with division by zero
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # alternatively use a context manager
        with self.assertRaises(ValueError):
            calc.divide(10)
        
        # Motivation fo why test should pass: We want our test to fail
        # only if there is problem with our code, not because of maths. 

if __name__ == '__main__':
    unittest.main()