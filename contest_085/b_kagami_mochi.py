# Accepted, you sould code "set" function by full scratch
n = int(input())

d_set = set(map(int, [input() for _ in range(n)]))
print(len(d_set))