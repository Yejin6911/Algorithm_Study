import sys
from copy import deepcopy
input = sys.stdin.readline

r, c, t = map(int, input().split())
a = [] # 미세먼지
loc = [] # 공기청정기 위치
for i in range(r):
    arr = list(map(int, input().split()))
    if(-1 in arr):
        loc.append([i, arr.index(-1)])
    a.append(arr)

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # 반시계 방향
dx2, dy2 = [0, 1, 0, -1], [1, 0, -1, 0] # 시계 방향

def wind():
    # 시계 방향
    x, y = loc[0][0], loc[0][1] + 1
    pre = a[x][y]
    a[x][y] = 0
    for i in range(4):
        while(1):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<r and 0<=ny<c):
                if([nx, ny] in loc):
                    break
                next = a[nx][ny] 
                a[nx][ny] = pre
                pre = next
                x, y = nx, ny
            else:
                break
    # 반시계 방향
    x, y = loc[1][0], loc[1][1] + 1
    pre = a[x][y]
    a[x][y] = 0
    for i in range(4):
        while(1):
            nx = x + dx2[i]
            ny = y + dy2[i]
            if(0<=nx<r and 0<=ny<c):
                if([nx, ny] in loc):
                    break
                next = a[nx][ny]
                a[nx][ny] = pre
                pre = next
                x, y = nx, ny
            else:
                break

def spread():
    temp = deepcopy(a)
    for i in range(r):
        for j in range(c):
            if(a[i][j] > 0):
                amount = a[i][j] // 5
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if(0<=ni<r and 0<=nj<c and [ni, nj] not in loc):
                        temp[ni][nj] += amount
                        temp[i][j] -= amount
    return temp

for _ in range(t):
    a = spread()
    wind()

ans = 0
for i in range(r):
    ans += sum(a[i])

print(ans + 2)