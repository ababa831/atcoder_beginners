# In progress
class Queue(object):
    def __init__(self, queue_size):
        self.size = queue_size
        self.Q = [None for _ in range(queue_size)]
        self.head = None
        self.tail = None
    
    def enqueue(self, x):
        self.Q.append(x)
        if self.tail is not None:
            self.tail += 1
        else:
            self.head = 0
            self.tail = self.head + 1

    def dequeue(self):
        self.Q.pop(self.head)
        self.head += 1

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

