import sys
from itertools import combinations

sys_input = sys.stdin.readline

D, G = map(int, input().split())
pc_list = [tuple(map(int, input().split())) for _ in range(D)]

# WIP