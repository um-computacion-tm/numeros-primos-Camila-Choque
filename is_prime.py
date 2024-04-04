import unittest

def is_prime(value):
     for i in range(2,value): #del dos hasta el numero ingresado 
      if value % i == 0:
          return False
     return True
     

class TetsIsPrime(unittest.TestCase):
    def test_with_1(self):
        result = is_prime(1)
        self.assertTrue(result)

    def test_with_2(self):
        result = is_prime(2)
        self.assertTrue(result)

    def test_with_3(self):
        result = is_prime(3)
        self.assertTrue(result)

    def test_with_4(self):
        result = is_prime(4)
        self.assertFalse(result)

    def test_with_5(self):
        result = is_prime(5)
        self.assertTrue(result)

    def test_with_30(self):
        result = is_prime(30)
        self.assertFalse(result)
    
    def test_whit_89(self):
        result = is_prime(89)
        self.assertTrue(result)

    


unittest.main()
    