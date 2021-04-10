import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(n)]
# 양분
B = [[5]*n for _ in range(n)]
# 죽은나무
died = []
# 땅
board = [[deque() for _ in range(n)] for _ in range(n)]


# 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
# 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다.
# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
# 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
# 여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
# 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
def spring_summer():
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for t in range(len(board[i][j])):
                    if B[i][j] >= board[i][j][t]:
                        B[i][j] -= board[i][j][t]
                        board[i][j][t] += 1
                    else:
                        # 여름 처리
                        for _ in range(t, len(board[i][j])):
                            B[i][j] += board[i][j].pop()//2
                        break


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


# 가을에는 나무가 번식한다.
# 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
# 떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다.
# 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
# 겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
# 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
def autumn_winter():
    for x in range(n):
        for y in range(n):
            trees = board[x][y]
            for tree in trees:
                if tree % 5 == 0:
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            board[nx][ny].appendleft(1)
            B[x][y] += A[x][y]


for i in range(m):
    x, y, z = map(int, input().rstrip().split())
    board[x-1][y-1].append(z)

for i in range(k):
    spring_summer()
    autumn_winter()

result = 0
for i in range(n):
    for j in range(n):
        result += len(board[i][j])
print(result)
