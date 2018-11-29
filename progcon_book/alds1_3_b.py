# In progress
class Queue(object):
    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.Q = [None for _ in range(self.queue_size)]
        self.head = 0
        self.tail = 0

    def is_empty(self):
        # An example of fucking codes.
        """
        if self.head == self.tail:
            return True
        else:
            return False
        """
        return self.head == self.tail
    
    def is_full(self):
        return self.head == (self.tail+1) % self.queue_size

    def enqueue(self, x):
        if self.is_full() is False:
            self.Q[self.head] == x
            if self.head + 1 == self.queue_size:
                self.head = 0
            else:
                self.head += 1
        
    def dequeue(self):
        if self.is_empty() is False:
            x = self.Q[self.tail]
            if self.tail + 1 == self.queue_size:
                self.tail = 0
            else:
                self.tail += 1
            return x
        else:
            return None


if __name__ == "__main__":
    # Input
    n, q = list(map(int, input().split()))
    procs = {}
    for i in range(n):
        proc_name, proc_time = input().split()
        proc_time = int(proc_time)
        procs[proc_name] = proc_time
    # Processings
    max_size = int(1000000 / n)
    queue = Queue(max_size)
    elapsed_time = 0
    is_finished = False
    while is_finished is False:
        for proc_n, proc_t in procs.items():
    # TODO: 辞書ごとQueueに登録しないとわからなくなる？

