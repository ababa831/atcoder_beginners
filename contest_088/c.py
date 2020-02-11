# WIP (WA: in18.txt, in19.txt)
C11, C12, C13 = map(int, input().split())
C21, C22, C23 = map(int, input().split())
C31, C32, C33 = map(int, input().split())

# Strategy:
# 3(a1+a2+a3+b1+b2+b3) = Σ_i Σ_j C_i_j
# sum of all C_i,j must be a mltiple of 3

sum_C = C11 + C12 + C13 + C21 + C22 + C23 + C31 + C32 + C33

if sum_C % 3 == 0:
    print('Yes')
else:
    print('No')
