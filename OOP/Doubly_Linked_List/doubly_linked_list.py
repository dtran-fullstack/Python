from node import Node

class Dlist:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def insert_to_front(self, value):
        new_node = Node(value)
        if self.first_node == None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.next = self.first_node
            self.first_node.prev = new_node
            self.first_node = new_node
        return self

    def insert_to_back(self,value):
        new_node = Node(value)
        if self.last_node == None:
            self.last_node = new_node
            self.first_node = new_node
        else:
            self.last_node.next = new_node
            new_node.prev = self.last_node
            self.last_node = new_node
        return self 

    def insert_before(self, node, new_node):
        if node == self.first_node:
            self.insert_to_front(new_node.value)
        elif node == self.last_node:
            self.insert_to_back(new_node.value)
        else:
            node.prev.next = new_node
            new_node.prev = node.prev
            new_node.next = node
            node.prev = new_node
        return self

    def insert_after(self, node, new_node):
        if node == self.first_node:
            self.insert_to_front(new_node.value)
        elif node == self.last_node:
            self.insert_to_back(new_node.value)
        else:
            node.next.prev = new_node
            new_node.next = node.next
            new_node.prev = node
            node.next = new_node
        return self

    # search forward and return target node
    def search_forward(self, value):
        if self.first_node == None:
            print("Search in an Empty List!")
            return None
        if self.first_node.value == value:
            return self.first_node
        current = self.first_node.next
        found = False
        while (found == False) and (current != None):
            if current.value != value:
                current = current.next
            else:    
                found = True
        if found == True:
            print(f"Found the node: {current.value}")
            return current
        else:
            print("Not found!")
            return None

    # search forward and return target node
    def search_backward(self, value):
        if self.last_node == None:
            print("Search in an Empty List!")
            return None
        # if self.last_node.value == value:
        #     return self.last_node
        current = self.last_node
        found = False
        while (found == False) and (current != None):
            if current.value != value:
                current = current.prev
            else:    
                found = True
        if found == True:
            print(f"Found the node: {current.value}")
            return current
        else:
            print("Not found!")
            return None


    def printForward(self):
        print("Print Forward")
        current_node = self.first_node
        count = 1
        while current_node != None:
            print(f"Node {count} Value: {current_node.value}")
            current_node = current_node.next
            count += 1
        return self

    def printBackward(self):
        print("Print Backward")
        current_node = self.last_node
        count = 1
        while current_node != None:
            print(f"Node {count} Value: {current_node.value}")
            current_node = current_node.prev
            count += 1
        return self


mylist = Dlist()
mylist.insert_to_back(1).insert_to_back(2).insert_to_back(3).insert_to_back(4).insert_to_back(5).printForward()

node = mylist.search_forward(4)
new_node = Node(100)
mylist.insert_before(node, new_node).printForward()

node2 = mylist.search_backward(5)
new_node2 = Node(100)
mylist.insert_after(node2, new_node2).printForward()

# Tested with Empty, 1 element, 2 elements, and multi elements

