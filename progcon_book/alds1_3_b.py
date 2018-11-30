# Accepted
class Queue(object):
    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.Q = [None] * self.queue_size
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


if __name__ == "__main__":
    # Input
    n, q = list(map(int, input().split()))
    pt = list([input().split() for _ in range(n)])
    p = [val[0] for val in pt]
    t = list(map(int, [val[1] for val in pt]))
    # Enqueue all data
    q_size = 1000000  # Assumed max_size
    p_queue = Queue(q_size)
    t_queue = Queue(q_size)
    for i in range(n):
        p_queue.enqueue(p[i])
        t_queue.enqueue(t[i])
    # print(t_queue.Q)
    # Do round-robin
    n_finished = 0
    elapsed_time = 0
    while n_finished < n:
        tmp_t, tmp_p = t_queue.dequeue(), p_queue.dequeue()
        tmp_lefttime = tmp_t - q
        if tmp_lefttime <= 0:
            # If the process was done
            elapsed_time += tmp_t
            print(tmp_p, elapsed_time)
            n_finished += 1
        else:
            # If the process was not finished
            elapsed_time += q
            t_queue.enqueue(tmp_lefttime)
            p_queue.enqueue(tmp_p)
