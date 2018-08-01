a, b = map(int, input().split())
if a*b % 2: # == 1 (うっかり逆にしないこと)
    print('Odd')
else: # == 0
    print('Even')