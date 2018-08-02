# 初見分からず
# 考え方：個数の組み合わせを総当たりで全パターン試せばよい！
a, b, c, x = map(int, [input() for val in range(4)])

n_pattern = 0
for i in range(a+1):#0~a+1
    for j in range(b+1):
        for k in range(c+1):
            if i * 500 + j * 100 + k * 50 == x:
                n_pattern += 1

print(n_pattern)




    


