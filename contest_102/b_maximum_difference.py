# Accepted
# (I think a test giver expect you should solve the probrem by full scratch, 
# not using map() or min() functions.)
n = int(input())
a_list = list(map(int, input().split()))
print(max(a_list) - min(a_list))