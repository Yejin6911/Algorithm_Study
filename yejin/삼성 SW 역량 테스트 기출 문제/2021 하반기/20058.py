# PyPy3 제출
import copy
import sys
sys.setrecursionlimit(10 ** 5)


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


dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def reduce(temp_A):
    for x in range(N):
        for y in range(N):
            if temp_A[x][y]:
                cnt = 0
                for i in range(4):
                    nx = x+dir[i][0]
                    ny = y+dir[i][1]
                    if 0 <= nx < N and 0 <= ny < N and temp_A[nx][ny] > 0:
                        cnt += 1
                if cnt < 3:
                    A[x][y] -= 1
    return


def dfs(x, y, visited):
    size = 1
    visited[x][y] = 1
    for i in range(4):
        nx = x+dir[i][0]
        ny = y+dir[i][1]
        if 0 <= nx < N and 0 <= ny < N and A[nx][ny] and not visited[nx][ny]:
            size += dfs(nx, ny, visited)
    return size


n, q = map(int, input().rstrip().split())
N = 2**n
A = [list(map(int, input().rstrip().split())) for _ in range(2**n)]
L = list(map(int, input().rstrip().split()))

for i in range(q):
    size = 2**L[i]
    if size > 1:
        for x in range(0, N, size):
            for y in range(0, N, size):
                spin(x, y, size)
    temp_A = copy.deepcopy(A)
    reduce(temp_A)

total = 0
maxSize = 0

visited = [[0]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        total += A[x][y]
        if A[x][y]:
            maxSize = max(maxSize, dfs(x, y, visited))
print(total)
print(maxSize)
