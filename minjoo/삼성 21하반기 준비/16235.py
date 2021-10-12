import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)] # 추가되는 양분
food = [[5]*n for _ in range(n)] # 양분
tree = [[deque() for _  in range(n)] for _ in range(n)] # 나무
for i in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z) # 나무의 나이

def springsummer():
    global tree, food
    for i in range(n):
        for j in range(n):
            for idx in range(len(tree[i][j])):
                if(food[i][j] >= tree[i][j][idx]): # 양분이 나이 이상으로 있으면
                    food[i][j] -= tree[i][j][idx]
                    tree[i][j][idx] += 1
                else: # 양분이 부족하면
                    for _ in range(idx, len(tree[i][j])):
                        food[i][j] += tree[i][j].pop()//2
                    break


def autumn():
    global tree
    dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(n):
        for j in range(n):
            t = tree[i][j]
            for idx in range(len(t)):
                if(t[idx] % 5 == 0):
                    for ii in range(8):
                        nx = i + dx[ii]
                        ny = j + dy[ii]
                        if(0<=nx<n and 0<=ny<n):
                            tree[nx][ny].appendleft(1)
            food[i][j] += a[i][j]



for _ in range(k):
    springsummer()
    autumn()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)