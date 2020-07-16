import unittest
from doubly_linked_list import Dlist

def insert_front(list):
    myDlist = Dlist()
    if myDlist.first_node == None:
        myDlist.insert_to_front(list[0])
    else:
        for i in range (len(list)):
            myDlist.insert_to_front(list[i])
        myDlist.printForward()
    return myDlist

def insert_back(list):
    myDlist = Dlist()
    if myDlist.first_node == None:
        myDlist.insert_to_back(list[0])
    else:
        for i in range (len(list)):
            myDlist.insert_to_back(list[i])
        myDlist.printBackward()
    return myDlist

def insert_before(list, value):
    myDlist = Dlist()
    new_node = Node(value)
    for
    

class Test_DList(unittest.TestCase):
    case1 = [1]
    case2 = [1,2]
    case2_addFront = [2,1]
    case3 = [1,2,3]
    case3_addFront = [3,2,1]
    case4 = [1,2,3,4,5,6,7,8,9,10]
    case4_addFront = [10,9,8,7,6,5,4,3,2,1,]

    def test_case1(self):
        myDlist = insert_front(Test_DList.case1)
        self.assertEqual(myDlist.first_node.value,Test_DList.case1[0])
        myDlist2 = insert_back(Test_DList.case1)
        self.assertEqual(myDlist2.last_node.value,Test_DList.case1[0])

    def test_case2(self):
        myDlist = insert_front(Test_DList.case2)
        current_node = myDlist.first_node
        for i in range (len(Test_DList.case2)):
            self.assertEqual(current_node.value,Test_DList.case2_addFront[i])
            current_node = current_node.next  

    def test_case3(self):
        myDlist = insert_front(Test_DList.case3)
        current_node = myDlist.first_node
        for i in range (len(Test_DList.case3)):
            self.assertEqual(current_node.value,Test_DList.case3_addFront[i])
            current_node = current_node.next
    
    def test_case4(self):
        myDlist = insert_front(Test_DList.case4)
        current_node = myDlist.first_node
        for i in range (len(Test_DList.case4)):
            self.assertEqual(current_node.value,Test_DList.case4_addFront[i])
            current_node = current_node.next

    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown")


if __name__ == "__main__":
    unittest.main()