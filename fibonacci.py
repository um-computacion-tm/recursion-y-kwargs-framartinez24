import unittest
def fibonacci(n):
    if n == 0 or n == 1:
        print(n)
        return n
    
    result = fibonacci(n-1) + fibonacci(n-2)
    print(result)
    return result

class test_fibonacci(unittest.TestCase):
    def test_0(self):
        result = fibonacci(0)
        self.assertEqual(result, 0)
    
    def test_1(self):
        result = fibonacci(1)
        self.assertEqual(result, 1)
   
    def test_2(self):
        result = fibonacci(2)
        self.assertEqual(result, 1)
   
    def test_3(self):
        result = fibonacci(3)
        self.assertEqual(result, 2)
  
    def test_4(self):
        result = fibonacci(4)
        self.assertEqual(result, 3)
  
    def test_5(self):
        result = fibonacci(5)
        self.assertEqual(result, 5)
  
    def test_6(self):
        result = fibonacci(6)
        self.assertEqual(result, 8)
  
    def test_7(self):
        result = fibonacci(7)
        self.assertEqual(result, 13)

    def test_8(self):
        result = fibonacci(8)
        self.assertEqual(result, 21)

    def test_9(self):
        result = fibonacci(9)
        self.assertEqual(result, 34)

if __name__ == '__main__':
    unittest.main()