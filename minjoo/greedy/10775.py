# 뭔소리야...... ???? # 시간초과
# 유니온-파인드 (union-find)
# https://mygumi.tistory.com/245

import sys
g = int(sys.stdin.readline()) # 게이트의 수
p = int(sys.stdin.readline()) # 비행기의 수

plane = []
for _ in range(p):
    plane.append(int(sys.stdin.readline()))

def parent_find(x): # root 찾기
    if(x == parent[x]): 
        return x
    p = parent_find(parent[x])
    parent[x] = p # 이어주기
    return parent[x]

def union(x, y):
    x = parent_find(x)
    y = parent_find(y)
    parent[x] = y

parent = {i:i for i in range(g+1)}
cnt = 0
for i in plane:
    x = parent_find(i)
    if(x == 0): # 더이상 도킹할 곳이 없다
        break
    union(x, x-1)
    cnt += 1

print(cnt)