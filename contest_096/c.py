# WIP (DFS?, input 3 ?)
import sys
from collections import deque

sys_input = sys.stdin.readline

H, W = map(int, sys_input().split())
areamap = [list(sys_input().replace('\n', '')) for h in range(H)]

stack = deque()
