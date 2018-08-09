# answers of programming probrems written in 
# "プログラミングコンテスト攻略のためのアルゴリズムとデータ構造"

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