# WIP
N, M = map(int, input().split())
connect = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    connect[u - 1].append(v)
    connect[v - 1].append(u)

already_passed = [False] * N

def DFS():
    pass
