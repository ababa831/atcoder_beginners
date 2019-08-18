# AC
N = int(input())
AAA = list(map(int, input().split()))

AAAinved = [1/a for a in AAA]

print(1/sum(AAAinved))
