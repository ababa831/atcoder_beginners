# WIP
N, M = map(int, input().split())
# src (smaller num) -> dst (larger num)
links = [tuple(map(int, input().split())) for _ in range(M)]

# DFS:
# IF there are sets of same number, the network is not tree.