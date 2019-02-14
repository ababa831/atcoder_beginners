s = input()

answer = 0
for canditate in range(1 << len(s)-1):
    combi = s[0]
    for n_digit in range(len(s) - 1):
        if (canditate >> n_digit) & 1:
            combi += '+'
        combi += s[n_digit+1]  # 足される数's[0]'を除いた数値部分を取り出す
    answer += eval(combi)

print(answer)
