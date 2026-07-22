#first data structure

#linked list - all of the nodes are separated and all over the place.
# has a variable called head and points to the first item in the list. it also has a var called tail which points thw the last item in the list
# in a LL, each node points to the next. the last one points to none.


#what is the node? (the value and the pointer) it is essentially a dictionary: 
# {
# "value" : 4,
#  "next": None
# }

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# my_linked_list = LinkedList(4)

# print(my_linked_list.tail.value)

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next): #a diff way of writing this is: while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

my_linked_list = LinkedList(1)
my_linked_list.append(2)

#(2) Items -returns 2 Node
print(my_linked_list.pop())
#(1) Items -returns 2 Node
print(my_linked_list.pop())
#(0) Items -returns 2 None
print(my_linked_list.pop())
