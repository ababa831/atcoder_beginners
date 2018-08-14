# Third trial of https://qiita.com/drken/items/fd4e5e3630d0f5859067
# 0. OK
a = int(input())
b, c = map(int, input().split())
print(a+b+c, input())

#1. OK
a, b = map(int, input().split())
if a * b % 2 == 1:
    print("Odd")
else:
    print("Even")

#2. OK
print(sum(map(int, list(input()))))

#3. OK
n = int(input())
a_list = list(map(int, input().split()))

is_even = 1
n_operation = 0
while(is_even):
    a_list = [a/2 for a in a_list if a % 2 == 0]
    if len(a_list) < n:
        is_even = 0
    else:
        n_operation += 1

print(n_operation)