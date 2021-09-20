import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline


def build(now_board, candidate):
    for x, y in candidate:
        now_board[x][y] = 1
    return now_board


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def spread(now_board, virus):
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and now_board[nx][ny] == 0:
                now_board[nx][ny] = 2
                queue.append((nx, ny))
    return now_board


n, m = map(int, input().split())
board = []
virus = []
space_0 = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            virus.append((i, j))
        elif row[j] == 0:
            space_0.append((i, j))
    board.append(row)

# 벽을 3개 세우는 모든 경우의 수
candidates = list(combinations(space_0, 3))
answer = 0
for candidate in candidates:
    now_board = copy.deepcopy(board)
    # 1. 벽세우기
    now_board = build(now_board, candidate)
    # 2. 바이러스 확산
    now_board = spread(now_board, virus)
    # 3. 안전 영역 크기 계산
    cnt = 0
    for row in now_board:
        cnt += row.count(0)
    answer = max(answer, cnt)

print(answer)
