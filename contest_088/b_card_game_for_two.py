# Accepted
n = int(input())
a_list = sorted(map(int, input().split()), reverse=True)

alice_score = sum(a_list[0::2])
bob_score = sum(a_list[1::2])

print(alice_score - bob_score)