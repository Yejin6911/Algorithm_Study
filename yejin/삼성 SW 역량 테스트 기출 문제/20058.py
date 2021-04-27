import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n, q = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(2**n)]
L = list(map(int, input().rstrip().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 시계방향 회전
def spin(x, y, size):
    new = []
    for i in range(y, y+size):
        temp = []
        for j in range(x+size-1, x-1, -1):
            temp.append(A[j][i])
        new.append(temp)
    for i in range(size):
        for j in range(size):
            A[x+i][y+j] = new[i][j]


# 얼음있는 인접한 칸 개수
def check(x, y, A):
    num = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < len(A) and 0 <= ny < len(A) and A[nx][ny] > 0:
            num += 1
    return num


# 덩어리 크기 구하기(dfs)
def find(x, y, visited):
    size = 1
    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < len(A) and 0 <= ny < len(A) and A[nx][ny] and not visited[nx][ny]:
            size += find(nx, ny, visited)
    return size


n = len(A)
for l in L:
    size = 2**l
    if size > 1:
        for x in range(0, n, size):
            for y in range(0, n, size):
                # 시계방향 회전
                spin(x, y, size)
    temp_A = copy.deepcopy(A)
    for x in range(n):
        for y in range(n):
            if temp_A[x][y] and check(x, y, temp_A) < 3:
                A[x][y] -= 1

result = 0
ice = 0
visited = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        result += A[x][y]
        if A[x][y]:
            ice = max(ice, find(x, y, visited))
print(result)
print(ice)
