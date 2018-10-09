# Accepted
n, a, b = map(int, input().split())
canditates = [i for i in range(1, n+1) 
              if a <= sum(map(int, list(str(i)))) <= b]
print(sum(canditates))