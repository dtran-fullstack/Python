import unittest
from singly_linked_list import Slist

class Test_SList(unittest.TestCase):
    def test_add_from_front(self):
        mySlist = Slist()
        mySlist.add_to_front(10).add_to_front(9).add_to_front(8).add_to_front(7)
        self.assertEqual(mySlist,[7,8,9,10])
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown")


if __name__ == "__main__":
    unittest.main()