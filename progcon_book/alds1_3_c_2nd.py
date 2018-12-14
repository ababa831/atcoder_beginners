# In progress
class Node(object):
    def __init__(self, key=None, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev

class DoublyLinkedList(object):
    def __init__(self):
        self.nodelist = []

    def insert(self, x):
        self.node = Node(key=x)
        