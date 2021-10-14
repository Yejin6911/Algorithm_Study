import sys
from itertools import combinations
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())  # 연구소의 크기, 바이러스의 개수
board = [list(map(int, input().split())) for _ in range(n)]
virus = []
for i in range(n):
    for j in range(n):
        if (board[i][j] == 2):  # 바이러스 위치 찾기
            virus.append([i, j])

comb = list(combinations(virus, m))  # 바이러스 m개 조합

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def check(board):  # 빈칸이 없는지 and 최솟값
    cnt = 0
    flag = 0
    for i in range(n):
        for j in range(n):
            if (board[i][j] == 0):
                return False
            if (board[i][j] < cnt):
                flag = 1  # 1초라도 흘렀음
                cnt = board[i][j]
    if (flag == 0):  # 1초도 안흐름
        return "0"
    else:
        return cnt


def dfs(active):
    tempboard = deepcopy(board)
    q = deque(active)
    cnt = 1  # 경과 시간
    visited = [[0] * n for _ in range(n)]
    
    while (q):
        temp = deque()
        while (q):
            x, y = q.popleft()
            visited[x][y] = 1
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if (0 <= nx < n and 0 <= ny < n):
                    if (visited[nx][ny] == 0 and tempboard[nx][ny] == 0):  # 빈칸이면
                        tempboard[nx][ny] = -cnt
                        temp.append([nx, ny])
                        visited[nx][ny] = 1
                    elif (visited[nx][ny] == 0 and tempboard[nx][ny] == 2):
                        temp.append([nx, ny])
                        visited[nx][ny] = 1
        cnt += 1
        q = q + temp

    result = check(tempboard)
    if (result == "0"):
        return 0
    elif (result):
        return result * (-1)
    else:
        return sys.maxsize


min_cnt = sys.maxsize
flag = 0
for i in range(len(comb)):
    cnt = dfs(comb[i])
    if (cnt < min_cnt):
        flag = 1
        min_cnt = cnt
        # print(i)

if (flag == 0):
    min_cnt = -1

print(min_cnt)