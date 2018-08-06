# I coudn't reach an answer at first.
# Keypoints:
# Look for conditions which constrain search range!
# 1. There are no paths for t_i < x_i + y_i (e.g. t=4, x=100, y=100)
# 2. There are no paths for t_i % 2 != (x_i + y_i) % 2 (e.g. t=4, x=1, y=0)
#    Because you can only reach the point by either odd or even trials (if you want to rearrive the same point, you sould take 2*i times)
import random

n = int(input())
txy_list = list(map(int, [input().split() for _ in range(n)]))
loc = [0, 0]
n_check = 0 
checkpoint = -1
start = 0

# select one from 4 paths
def add_x(x, y):
    x += 1
    return [x, y]
def add_y(x, y):
    y += 1
    return [x, y]
def sub_x(x, y):
    x -= 1
    return [x, y]
def sub_y(x, y):
    y -= 1
    return [x, y]

for i in range(n):
    for j in range(start, i):
        path = random.randrange(1,5)
        if path == 1:
            loc = add_x(loc[0], loc[1])
        if path == 2:
            loc = add_y(loc[0], loc[1])
        if path == 3:
            loc = sub_x(loc[0], loc[1])
        if path == 4:
            loc = sub_y(loc[0], loc[1])
    if loc == txy_list[i][1:]:
        n_check += 1
        #Gave up at this point.

# A sapmle answer
n =  int(input())
for i in range(n):
    t, x, y = map(int, input().split())
    if x + y > t or (x + y) % 2 != t % 2:
        print('No')
        exit()
print("Yes")
        


        

