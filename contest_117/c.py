# WIP
# BFS?
N, M = map(int, input().split())
XXX = list(map(int, input().split()))
XXX.sort()

dists = [abs(XXX[i] - XXX[i+1]) for i in range(M) if i < M-1]
already_passed = [False] * M


# Sort -> place komas on the two edges 
# -> calc distance between elements in sorted XXX


