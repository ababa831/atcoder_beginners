# In progress
# Keypoints of implement doubly linked list
# Make two roles for the list:
# - Structure of a node of doubly linked list
# - Linkage of the nodes
#   - next = prev = new node (if prev == none)
#   - next = new node and new_node.prev = next?
# Update: 2018-12-11 (in progress) (may be WA)


class Node(object):
    def __init__(self, key=None, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    def __init__(self):
        self.state = Node()

    def insert(self, x):
        """Add a node which has `val=x` 
        key to the last of the Linked List
        """
        self.state.next = Node(key=x)
        self.state.next.prev = self.state

    def delete(self, x):
        """Delete the node which is the first node with `key=x`
        """
        is_rightedge = False
        target_node = self.state
        while is_rightedge is False:
            if target_node.key == x:
                # Single node
                if target_node.prev is None and target_node.next is None:
                    target_node = Node()
                    is_rightedge = True
                # First node
                elif target_node.prev is None:
                    target_node = target_node.prev
                # Last node
                elif target_node.next is None:
                    target_node.prev = None
                    is_rightedge = True
                # Node which holds links
                else:
                    target_node.nexy.prev = target_node.prev.next
                    target_node.prev = target_node.next
                break
            # Search the next node
            target_node = target_node.next

    def delete_first(self):
        if self.state is not None:
            self.state = self.state.next
            self.state.prev = None

    def delete_last(self):
        is_rightedge = False
        target_node = self.state
        while is_rightedge is False:
            if target_node.next is None:
                target_node.prev.next = None
            # Increment the next node
            target_node = target_node.next
