import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
 def setUp(self):
        self.calc = SimpleCalculator()


 def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-7, 6), -1)
 def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(9, 4), 5)
        self.assertEqual(self.calc.subtract(-16, 7), -23)
        self.assertEqual(self.calc.subtract(23, 12), 11)
        
 def test_multiplication(self):
       self.assertEqual(self.calc.multiply(3, 4),12)
       self.assertEqual(self.calc.multiply(5, 4),20)
       self.assertEqual(self.calc.multiply(-6, -4),24)
       self.assertEqual(self.calc.multiply(-3, 7),-21)

 def test_division(self):
       self.assertEqual(self.calc.divide(6, 3), 2)
       self.assertEqual(self.calc.divide(16, 4), 4)
       self.assertEqual(self.calc.divide(0, 3), 0)
       self.assertEqual(self.calc.divide(-10, 10), -1)

 def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

 if __name__ == "__main__":
    unittest.main()



