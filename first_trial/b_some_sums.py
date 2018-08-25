# 初見分からず
# 各桁数の取り出し方：
# 数値を文字列に変換→文字列を一つずつリストの要素として分離することで可能
n, a, b = map(int, input().split())

sum_number = 0
for i in range(1, n+1):
    sum_digit = sum(map(int, list(str(i))))
    if sum_digit >= a and sum_digit <= b:
        sum_number += i

print(sum_number) 

