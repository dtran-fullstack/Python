# import the python testing framework
import unittest

# our "unit"
# this is what we are running our test on
def reverseList(list):
    for i in range (int(len(list)/2)):
        list[i], list[len(list) - 1 - i] = list[len(list) - 1 - i], list[i]
    return list

def isPalindrome(word):
    for i in range (int(len(word)/2)):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True

def coin(amount):
    list = []
    list.append(int(amount/25))
    list.append(int((amount%25)/10))
    list.append(int(((amount%25)%10)/5))
    list.append(int(((amount%25)%10)%5))
    return list

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase
class AllTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testOne(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])
        self.assertEqual(reverseList([1,3,5,7]), [7,5,3,1])
        self.assertEqual( coin(87), [3,1,0,2] )
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(fibonacci(5), 3)
        self.assertEqual(fibonacci(9), 21)

    def testTwo(self):        
        self.assertTrue( isPalindrome("racecar"))
        self.assertFalse( isPalindrome("rabcr") )
    
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main() # this runs our tests

