# In progress
class Queue(object):
    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.Q = [None for _ in range(queue_size)]
        self.head = 0
        self.tail = 0
    
    def enqueue(self, x):
        self.Q[self.tail] = x
        self.tail = (self.tail + 1) % self.queue_size
    
    def dequeue(self):
        x = self.Q[self.head]
        self.Q[self.head] = None
        self.head = (self.head + 1) % self.queue_size
        return x

def main():
    # TODO: Write a code of round-robin scheduling 

if __name__ == '__main__':
    main()