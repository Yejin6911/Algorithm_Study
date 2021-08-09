import copy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(start, degree):
    visited[start] = 1
    if start == b:
        global answer
        answer = min(answer, degree)
        return
    for i in range(1, n+1):
        if matrix[start][i] == 1 and not visited[i]:
            dfs(i, degree+1)


n = int(input().rstrip())
a, b = map(int, input().rstrip().split())
m = int(input().rstrip())
matrix = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().rstrip().split())
    matrix[x][y], matrix[y][x] = 1, 1

answer = n
visited = [0 for _ in range(n+1)]
dfs(a, 0)

# 촌수 없는 경우
if answer == n:
    print(-1)
else:
    print(answer)
