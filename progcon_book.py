# answers of programming probrems written in 
# "プログラミングコンテスト攻略のためのアルゴリズムとデータ構造"

# 2.2 Top 3
# 10人分のプレイヤーの得点が記録されたデータを読み込んで，
# その中から上位3人の得点を順に出力してください．ただし，得点は100点満点とします．
# 入力例： 25 36 4 55 71 18 0 71 89 65
# 出力例： 89 71 71
scores = sorted(map(int, input().split()), reverse=True)
print(scores[0], scores[1], scores[2])

# 2.3 Top N
# m個の整数a_i(i = 1, 2, ..., m)が与えられます．
# その中で値が大きい順にn個出力してください．
# 制約： m <= 1,000,000, n <= 1,000, 0 <= a_i <= 10^6
# 入力例: 
# N
# a_1, ..., a_m
n = int(input())
scores = sorted(map(int, input().split()), reverse=True)
scores_str = [str(score) for score in scores]
print(" ".join(scores_str[:n]))

# 2.5 ALDS1_1_D: Maximum Profit p.46
# Don't use duplicated loops (avoid o(n^2) complexity)
n =  int(input())
r_list = list(map(int, [input() for _ in range(n)]))
min_sub = r_list[0] # left edge (min canditate is located on the left from max one!)
max_sub = float("-inf")
for i in range(1, n):
    max_sub = max(max_sub, r_list[i] - min_sub)
    min_sub = min(min_sub, r_list[i])
print(max_sub)

# 3. Problems related to sort algorithms are passed, 
# because you don't need to code them by full scratch 
# thanks to "sorted()" function in Python standard modules.
# (If you have enough free time, you should learn the algorithms)

# 4. 
# 4.2 ALDS1_3_A: Stack (reverse Polish notation)
input_list = list(input().split())
operator = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: float(x) / y
}
stack = []
for val in input_list:
    if val not in ["+", "-", "*", "/"]:
        stack.append(int(val))
    else:
        # Note: Last In First Out (Be aware of the order) 
        y = stack.pop()
        x = stack.pop()
        stack.append(operator[val](x, y))
print(stack[0])