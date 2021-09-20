import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

cands = []
for _ in range(ops[0]):
    cands.append('+')
for _ in range(ops[1]):
    cands.append('-')
for _ in range(ops[2]):
    cands.append('*')
for _ in range(ops[3]):
    cands.append('//')

perm = list(permutations(cands, n-1))
perm = list(set(perm))

_max = sys.maxsize * (-1)
_min = sys.maxsize

for i in range(len(perm)):
    temp = nums[0]
    for j in range(1, n):
        if(perm[i][j-1] == '+'):
            temp += nums[j]
        elif(perm[i][j-1] == '-'):
            temp -= nums[j]
        elif(perm[i][j-1] == '*'):
            temp *= nums[j]
        else:
            if(temp < 0):
                temp = (temp*(-1) // nums[j])*(-1)
            else:
                temp = temp // nums[j]
    
    _max = max(_max, temp)
    _min = min(_min, temp)

print(_max)
print(_min)