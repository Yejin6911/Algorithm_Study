import sys

input = sys.stdin.readline

def dfs(x, y, shape):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
        return

    if shape == 0 or shape == 2:
        if y + 1 < n:
            if a[x][y+1] == 0:
                dfs(x, y+1, 0)
    if shape == 1 or shape == 2:
        if x + 1 < n:
            if a[x+1][y] == 0:
                dfs(x+1, y, 1)
    if shape == 0 or shape == 1 or shape == 2:
        if x + 1 < n and y + 1 < n:
            if a[x+1][y] == 0 and a[x][y+1] == 0 and a[x+1][y+1] == 0:
                dfs(x+1, y+1, 2)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(0, 1, 0)
print(ans)

# import sys
# from collections import deque
# input = sys.stdin.readline
#
# n = int(input()) # 집의 크기
# house = [list(map(int, input().split())) for _ in range(n)]
# dx, dy = [0, 1, 1], [1, 0, 1] # 가로, 세로, 대각선
# d_list = [[0, 2], [1, 2], [0, 1, 2]] # 가로, 세로, 대각선이 회전할 수 있는 방향
# end_x, end_y = 0, 1
#
# def bfs(end_x, end_y):
#     global house
#
#     q = deque()
#     q.append([end_x, end_y, 0])
#     cnt = 0
#     while(q):
#         x, y, d = q.popleft() # x, y, 현재방향
#         for i in d_list[d]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if(0<=nx<n and 0<=ny<n):
#                 if([nx, ny] == [n-1, n-1] and house[n-1][n-1] == 0):
#                     cnt += 1 # 도착하면
#                     continue
#                 if(i < 2): # 가로 세로
#                     if(house[nx][ny] == 0):
#                         q.append([nx, ny, i])
#                 else: # 대각선
#                     if(house[nx][ny] == 0 and house[nx-1][ny] == 0 and house[nx][ny-1] == 0):
#                         q.append([nx, ny, i])
#     return cnt
#
# print(bfs(end_x, end_y))
#
#
#
