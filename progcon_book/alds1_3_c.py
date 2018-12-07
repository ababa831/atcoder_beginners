# In progress
# Keypoints of implement doubly linked list
# Make two roles for the list:
# - Structure of a node of doubly linked list
# - Linkage of the nodes
#   - next = prev = new node (if prev == none)
#   - next = new node and new_node.prev = next?


class Node(object):
    def __init__(self, key=None, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    def insert(self, x, prev_node=None):
        if prev_node is not None:
            new_node = Node(key=x, prev=prev_node.next)
            prev_node.next = new_node.prev
            

    def delete(self):
        pass

    def delete_first(self):
        pass

    def delete_last(self):
        pass