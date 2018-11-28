class Queue(object):
    def __init__(self, queue_size):
        self.size = queue_size
        self.Q = [None for _ in range(queue_size)]
        self.head = None
        self.tail = None
    
    def enqueue(self, x):
        self.Q.append(x)
    
    def dequeue(self):
        pass
