# 0.
a = int(input())
b, c = map(int, input().split())
s = input()
print(a+b+c, s)

# 1.
a, b = map(int, input().split())
if a * b % 2:
    print("Odd")
else:
    print("Even") 

# 2.
print(input().count("1"))

# 3. continuing a roop if a_list can't be divided by 2
n = int(input())
a_list = list(map(int, input().split()))
n_operation = 0
while(1):
    even_len = len([a for a in a_list if a % 2 == 0])
    if len(a_list) != even_len:
        print(n_operation)
        exit()
    else:
        a_list = [a / 2 for a in a_list]
        n_operation += 1

# another answer (You don't need to imitate the code because I don't think this code would be a straight resolution)
# bin(): decimal -> binary
# rfind(): search keyword from right edge of a number
import math
n = input()
a_list = list(map(int, input().split()))
ans = float("inf") # set max value
for i in a_list:
    ans = min(ans, len(bin(i) - bin(i).rfind("1") - 1))
print(round(ans))

# 4. The number of i+j+k isn't be constrained, so you just try full search.
a, b, c, x = map(int, [input() for _ in range(4)])
n = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 500 * i + 100 * j + 50 * k == x:
                n += 1
print(n)

# 5. 
n, a, b = map(int, input().split())
sum_num = 0
for i in range(1, n+1):
    i_digit_sum = sum(map(int, list(str(i))))
    if a <= i_digit_sum <= b: # don't forget <= (not < !) 
        sum_num += i
print(sum_num)


