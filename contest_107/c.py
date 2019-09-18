# WIP  DFS?
from collections import deque
import sys
input_s = sys.stdin.readline

N, K = map(int, input_s().split())
xxx = list(map(int, input_s().split()))

stack = deque()
stack.append(0)  # Start point
