# AC
from copy import copy

s = list(input())

before = ''
for chara in s:
    if chara == before:
        print('Bad')
        exit()
    before = chara
print('Good')
