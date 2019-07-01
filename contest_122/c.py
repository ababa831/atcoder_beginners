# AC
# a typical solution by using "cumulative sum"

N, Q = map(int, input().split())
S = input()

t = [0] * (N + 2)
t[0] = 1 if S[:2] == 'AC' else 0

for i in range(N - 2):
    t[i + 1] = t[i] + (1 if S[i:i + 2] == 'AC' else 0)

for _ in range(Q):
    l, r = map(int, input().split())
    print(t[r - 1] - t[l - 1])
