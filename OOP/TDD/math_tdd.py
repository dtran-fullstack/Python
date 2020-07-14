import unittest

class MathDojo:
    def __init__(self):
        self.result=0
    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self
    def substract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self

class MathTest(unittest.TestCase):
    def test(self):
        md = MathDojo()
        x = md.add(2).add(2,5,1).substract(3,2).result
        self.assertEqual(x,5)
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown")

if __name__ == '__main__':    
    unittest.main()