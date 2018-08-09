# answers of programming probrems written in 
# "プログラミングコンテスト攻略のためのアルゴリズムとデータ構造"

# 4.3 ALDS1_3_B Queue p.87
# Wrong answer at sight (Conditional branch should be modified)
"""
n_process, quantum = map(int, input().split())
p_t_list = [input().split() for _ in range(n_process)]

fincount = 0
i = 0
elapsed_time = 0
while(fincount < n_process):
    if i == n_process:
        i = 0
    p = p_t_list[i][0]
    t = int(p_t_list[i][1])
    if t <= 0:
        print(p, elapsed_time)
        fincount += 1
    else:
        p_t_list[i][1] = str(t - quantum)
        elapsed_time = elapsed_time + min(t, quantum)
    i += 1
"""
# Second trial with Queue class() (in standard modules)
"""
import numpy as np
import queue
p = queue.Queue()
t = queue.Queue()

n_process, quantum = map(int, input().split())
# Add all elements to the queues
for _ in range(n_process):
    p_i, t_i = input().split()
    p.put(p_i)
    t.put(int(t_i))

fincount = 0
elapsed_time = 0
finish_p = []
while(fincount < n_process):
    # Get process_name and time
    p_val = p.get()
    t_val = t.get()
    # Calculate processing time
    elapsed_time = elapsed_time + min(t_val, quantum)
    # Update remaining time
    t_val = max(t_val - quantum, 0)
    # Check whether the process is finished
    if t_val == 0 and p_val not in finish_p:
        print(p_val, elapsed_time)
        fincount += 1
        finish_p.append(p_val)
    # Add current process to end of the queue
    p.put(p_val)
    t.put(t_val)
"""
## Full scratch code (refered from p.91)
import sys 

class Queue(object):
    def __init__(self, n_process):
        self.MAX = n_process + 1 # Don't forget "+1"
        self.head = 0
        self.tail = 0
        self.Q = self.MAX * [0]

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.head == (self.tail + 1) % self.MAX

    def enqueue(self, x):
        if self.is_full():
            sys.stderr.write('Overflow occurred!')
        self.Q[self.tail] = x
        if self.tail + 1 == self.MAX:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.is_empty():
            sys.stderr.write('Underflow occurred!')
        x = self.Q[self.head]
        if self.head + 1 == self.MAX:
            self.head = 0
        else:
            self.head += 1
        return x

# Implementation of Round-robin scheduling
import numpy as np

n_process, quantum = map(int, input().split())

# Queue instance
p = Queue(n_process) # for process_name
t = Queue(n_process) # for processing_time

# Add all elements to the queues
for _ in range(n_process):
    p_i, t_i = input().split()
    p.enqueue(p_i)
    t.enqueue(int(t_i))

fincount = 0
elapsed_time = 0
finish_p = []
while(fincount < n_process):
    # Get process_name and time
    p_val = p.dequeue()
    t_val = t.dequeue()
    # Calculate processing time
    elapsed_time = elapsed_time + min(t_val, quantum)
    # Update remaining time
    t_val = max(t_val - quantum, 0)
    # Check whether the process is finished
    if t_val == 0 and p_val not in finish_p:
        print(p_val, elapsed_time)
        fincount += 1
        finish_p.append(p_val)
    # Add current process to end of the queue
    p.enqueue(p_val)
    t.enqueue(t_val)
    