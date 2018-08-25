# Time limit exceeded at sight
# range(n + 1 -i) in the second roop
# You don't need to add the third roop.
# Alternatively, you should use (k =) n - i - j
n , y= map(int, input().split())

for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if i + j + k == n:
                if  10000 * i + 5000 * j + 1000 * k == y:
                    print(i, j, k)
                    exit()
                    
print(-1, -1, -1)              

# Sample answer
n , y= map(int, input().split())
 
for i in range(n + 1):
    for j in range(n + 1 - i):
            if  10000 * i + 5000 * j + 1000 * (n - i - j) == y:
                print(i, j, n - i - j)
                exit()
                    
print(-1, -1, -1)
