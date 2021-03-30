import sys
import copy
from itertools import combinations
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
blank = []
virus = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    board.append(row)
    for j in range(m):
        if row[j] == 0:
            blank.append((i, j))
        elif row[j] == 2:
            virus.append((i, j))

# 방법 1 - combination으로 모든 경우 다 구해서 계산하기
steps = list(combinations(blank, 3))

dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]


# 바이러스 퍼뜨리기(bfs)
def spread_bfs(board):
    for v in virus:
        queue = deque()
        queue.append(v)
        while queue:
            now = queue.popleft()
            for i in range(4):
                nx = now[0]+dx[i]
                ny = now[1]+dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if board[nx][ny] == 0:
                        queue.append((nx, ny))
                        board[nx][ny] = 2
    return board


result = 0
for step in steps:
    # 1. 울타리 세우기
    new_board = copy.deepcopy(board)
    for (row, col) in step:
        new_board[row][col] = 1
    # 2. 바이러스 퍼뜨리기
    new_board = spread_bfs(new_board)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_board[i][j] == 0:
                cnt += 1
    if cnt > result:
        result = cnt

print(result)


# 방법 2 - 깊이 우선 탐색으로 울타리 설치하면서, 매번 안전 영역 크기 계산 -> PyPy3으로 해야 시간초과 안남
temp = [[0] * m for _ in range(n)]


def spread_dfs(virus):
    for i in range(4):
        nx = virus[0]+dx[i]
        ny = virus[1]+dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                spread_dfs((nx, ny))
    return board


def dfs(cnt):
    global result
    # 울타리가 3개 설치된 경우
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]
        # 바이러스 전파 진행
        for v in virus:
            spread_dfs(v)
        # 안전 영역 계산
        now_result = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    now_result += 1
        # 최댓값 계산
        result = max(result, now_result)
        return
    # 빈공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                cnt += 1
                dfs(cnt)
                board[i][j] = 0
                cnt -= 1


result = 0
dfs(0)
print(result)
