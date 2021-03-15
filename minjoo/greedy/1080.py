# 문제 읽을 때는 어려워 보였는데 막상 해보니까 됨.. 근데 왜 되는지 모르겠음 ^^..

import sys

def switch(matrix, x, y): # 3*3 크기만큼 1->0으로, 0->1로 변환
    for i in range(x, x+3):
        for j in range(y, y+3):
            if(matrix[i][j]=='0'):
                matrix[i][j] = '1'
            else:
                matrix[i][j] = '0'
    return matrix

def check(a, b, n, m): # a, b가 같은지 확인
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return 0
    return 1

n, m = map(int, sys.stdin.readline().strip().split())
a = []
b = []

for _ in range(n):
    a.append(list(sys.stdin.readline()))
for _ in range(n):
    b.append(list(sys.stdin.readline()))

answer = 0
for i in range(n-2):
    for j in range(m-2):
        if(a[i][j]!=b[i][j]): # 값이 다르면
            a = switch(a, i, j)
            answer += 1
            
        if(check(a, b, n, m)):
            break
    if(check(a, b, n, m)): 
        break

if(check(a, b, n, m)):
    print(answer)
else:
    print("-1")

