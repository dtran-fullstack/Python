from node import Node

class Slist:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head == None:
            print("List is empty!")
            return True
        else: 
            return False

    def add_to_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def add_to_back(self, val):
        if self.isEmpty():
            self.add_to_front(val)
            return self
        new_node = Node(val)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        return self

    def remove_from_front(self):
        if self.isEmpty == False:
            self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.isEmpty():
            return None
        if self.head.next == None:
            self.head = None
            return self
        current_node = self.head
        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None
        return self

    def remove_val(self, val):
        if self.isEmpty():
            return None
        print("<Remove Val> Value: ", val)
        if self.head.value == val:
            self.remove_from_front()
            return self
        current_node = self.head   
        while current_node.next.value != val and current_node.next != None:
            current_node = current_node.next
        current_node.next = current_node.next.next
        return self

    def print_value(self):
        current_node = self.head
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next
        return self

        

mySlist = Slist()
mySlist.add_to_front(10).add_to_front(9)#.add_to_front(8).add_to_front(7).add_to_back(11).print_value()
# print("<Remove Head> Value: ",mySlist.remove_from_front())
mySlist.remove_from_back().print_value()
# mySlist.remove_val(7).remove_val(9).remove_val(11).print_value()