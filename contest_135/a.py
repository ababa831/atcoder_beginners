# AC
A, B = map(int, input().split())

K = (A+B)/2
K_round = (A+B)//2

if isinstance(K, float):
    if K != K_round:
        print('IMPOSSIBLE')
    else:
        print(int(K))
