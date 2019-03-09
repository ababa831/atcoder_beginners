# Not submitted
# May be TLE
a, b = map(int, input().split())

ans = a
for i in range(a+1, b+1):
    ans ^=i
print(ans)