# pypy로 제출
import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split()) # 땅 크기, 나무 정보, 년 수
board = [[deque() for _  in range(n)] for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)] # 양분
nutrient = [[5]*n for _ in range(n)]
dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(m):
    x, y, z = map(int, input().split())
    board[x-1][y-1].append(z) # 나무 나이

def spring(): # 양분을 먹고 나이가 1 중가
    for i in range(n):
        for j in range(n):
            len_t = len(board[i][j])
            for t in range(len_t):
                if(board[i][j][t] <= nutrient[i][j]): # 양분이 먹을만큼 있으면
                    nutrient[i][j] -= board[i][j][t]
                    board[i][j][t] += 1
                else:
                    for _ in range(t, len_t):
                        nutrient[i][j] += board[i][j].pop()//2
                    break

def fall(): # 나무 번식
    for i in range(n):
        for j in range(n):
            for k in board[i][j]:
                if(k % 5 == 0): # 나무 나이가 5의 배수이면
                    for idx in range(8): # 인접한 땅
                        nx = i + dx[idx]
                        ny = j + dy[idx]
                        if(0<=nx<n and 0<=ny<n):
                            board[nx][ny].appendleft(1) # 나이가 1인 나무 심기
            nutrient[i][j] += a[i][j]

for _ in range(k):
    spring()
    fall()


result = 0
for i in range(n):
    for j in range(n):
        result += len(board[i][j])

print(result)



                


