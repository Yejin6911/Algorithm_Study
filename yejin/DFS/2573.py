from collections import deque
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 메모리초과
def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] > 0 and not visited[nx][ny]:
            dfs(nx, ny)


def bfs(x, y):
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if new_matrix[nx][ny] != 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


def melt():
    temp = copy.deepcopy(matrix)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if matrix[nx][ny] == 0:
                            temp[i][j] -= 1
                            if temp[i][j] == 0:
                                break
    return temp


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
q = deque()
year = 1

while True:
    new_matrix = melt()
    flag = 0
    for i in new_matrix:
        flag += i.count(0)
    # 이미 빙하가 다 녹은 경우
    if flag == n*m:
        print(0)
        sys.exit()
    matrix = copy.deepcopy(new_matrix)
    visited = [[0]*m for _ in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(m):
            if new_matrix[i][j] != 0 and visited[i][j] == 0:
                # 빙하 개수가 2개가 된 경우
                if cnt == 2:
                    print(year)
                    sys.exit()
                bfs(i, j)
                cnt += 1
    year += 1
