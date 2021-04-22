import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input()) # 수의 개수
a = list(map(int, input().split()))
op = list(map(int, input().split())) # + - * //
ops = []
for _ in range(op[0]):
    ops.append('+')
for _ in range(op[1]):
    ops.append('-')
for _ in range(op[2]):
    ops.append('*')
for _ in range(op[3]):
    ops.append('%')

comb = list(permutations(ops, n-1))
comb = list(set(comb))

max_result = sys.maxsize * (-1)
min_result = sys.maxsize
for c in comb:
    result = a[0]
    for i in range(1, n):
        if(c[i-1] == '+'):
            result += a[i]
        elif(c[i-1] == '-'):
            result -= a[i]
        elif(c[i-1] == '*'):
            result *= a[i]
        else:
            if(result < 0):
                result = result * (-1)
                result = result // a[i]
                result = result * (-1)
            else:
                result = result // a[i]

    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)