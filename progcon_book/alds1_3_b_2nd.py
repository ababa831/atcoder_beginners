# Accepted
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
    # Input
    n, q = map(int, input().split())
    # Enqueue all data
    p_queue = Queue(n)
    t_queue = Queue(n)
    for _ in range(n):
        name, time = input().split()
        time = int(time)
        p_queue.enqueue(name)
        t_queue.enqueue(time)
    # Do round-robin scheduling
    elapsed_time = 0
    n_finished = 0
    while n_finished < n:
        # Dequeue and process
        name, time = p_queue.dequeue(), t_queue.dequeue()
        tmp_time = max(time - q, 0)
        elapsed_time += min(q, time)
        # If the processing was not finished
        if tmp_time > 0:
            p_queue.enqueue(name)
            t_queue.enqueue(tmp_time)
        else:
            print(name, elapsed_time)
            n_finished += 1


if __name__ == '__main__':
    main()