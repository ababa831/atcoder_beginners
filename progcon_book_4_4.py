# ALDS1_3_C: Doubly Linked List
## Ref: https://www.youtube.com/watch?v=sDP_pReYNEc
## Ref: http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/
"""
4 types of commands 
- insert x
- delete x
- deleteFirst
- deleteLast
, where x is a key which contains list element

Input:
n
command 1
command 2
...
command n

The commands are selected by any of the four commands

Output:
key order in the doubly linked list is outputted. 
Continuing keys are outputted represented with a space.

"""
class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def insert(self, data):
        new_node = Node(data)
        if self.head == None:
            # add new node
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail # Add prev infomation to the new node 
            new_node.next = None # Add next information to the new node (Top is None)
            self.tail.next = new_node # Add next information to old tail node
            self.tail = new_node # Update new List (insert new node to the tail)
    
    def delete(self, node_val):
        current_node = self.head
        while current_node != None:
            if current_node.data == node_val:
                # If current_node is not the first element
                if current_node.prev != None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # current_node is the first element
                    self.head = current_node.next # Update head (old head is removed)
                    current_node.prev = None # Delete old prev info

            current_node = current_node.next # Update current_node position
    
    def delete_first(self):
        self.head = self.head.next
        self.head.prev = None

    def delete_last(self):
        self.tail = self.tail.prev
        self.tail.next = None
    
    def get_elem(self):
        elems = []
        current_node = self.head
        while current_node != None:
            data = current_node.data
            elems.append(data)
            current_node = current_node.next
        return elems[::-1] # reversed


n = int(input())

my_list = DoublyLinkedList()
for _ in range(n):
    command = input().split()
    command_len = len(command)
    if command_len == 2:
        x = int(command[1]) # data value
        if "insert" in command:
            my_list.insert(x)
        else:
            my_list.delete(x)
    else:
        if "deleteFirst" in command:
            my_list.delete_first()
        else:
            my_list.delete_last()

# elements with int value -> elements with converted str value
elements_str = list(map(str, my_list.get_elem())) 
print(" ".join(elements_str))

"""
wrong answer when below commands inputed

39
insert 1
insert 2
insert 1
insert 1
insert 1
insert 2
insert 2
insert 1
delete 2
deleteLast
deleteFirst
insert 2
insert 2
insert 2
insert 2
insert 2
insert 2
insert 2
insert 2
insert 2
insert 2
deleteFirst
deleteFirst
delete 2
delete 2
deleteFirst
delete 1
insert 3
insert 1
insert 1
delete 2
delete 2
delete 2
deleteLast
insert 4
delete 2
deleteLast
deleteFirst
delete 2

Traceback (most recent call last):
  File "./Main.py", line 68, in <module>
    my_list.delete(x)
  File "./Main.py", line 31, in delete
    current_node.next.prev = current_node.prev
AttributeError: 'NoneType' object has no attribute 'prev'
"""











