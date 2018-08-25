# 初見正解：無駄に複雑なコード
n = int(input())
a_list = list(map(int, input().split())) # list()を忘れずに

def odd_detector(a_list):
    is_odd = 0
    for a_i in a_list:
        if a_i % 2 == 1:
            is_odd = 1
            break
    return is_odd

n_division = 0
while odd_detector(a_list) == 0:
    a_list = [a / 2 for a in a_list]
    n_division += 1

print(n_division)

# 模範解答１
"""
def how_many_times_divisible(n):
	ans = 0
	while n % 2 == 0:
		n /= 2
		ans += 1
	return ans
 
n = int(raw_input())
a = map(int, raw_input().split())
ans = min(map(how_many_times_divisible, a))
 
print ans
"""

# 模範解答２
"""
import math
n = input()
a = list(map(int, input().split()))
ans = float("inf")
for i in a:
    ans = min(ans, len(bin(i)) - bin(i).rfind("1") - 1)
print(round(ans))
"""
