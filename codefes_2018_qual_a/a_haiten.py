# Accepted
a = int(input())
b = int(input())
c = int(input())
s = int(input())

q1_canditates = [a, a + 1]
q2_canditates = [b, b + 1]
q3_canditates = [c, c + 1]

for q1_cand in q1_canditates:
    for q2_cand in q2_canditates:
        for q3_cand in q3_canditates:
            if q1_cand + q2_cand + q3_cand == s:
                print('Yes')
                exit()
print('No')