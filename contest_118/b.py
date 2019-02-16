# Accepted
n, m = map(int, input().split())

leftover = None
for i in range(n):
    k_a_list = list(map(int, input().split()))
    if i == 0:
        leftover = k_a_list[1:]
    else:
        k = k_a_list[0]
        leftover = [a for a in k_a_list[1:] if a in leftover]
    if leftover == []:
        print(0)
        exit()

print(len(leftover))
