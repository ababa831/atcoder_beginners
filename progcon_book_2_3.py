# answers of programming probrems written in 
# "プログラミングコンテスト攻略のためのアルゴリズムとデータ構造"

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