import sys
from copy import deepcopy
input = sys.stdin.readline

n, m, k = map(int, input().split()) #땅 크기, 나무 개수, 연도 수
plus = [list(map(int, input().split())) for _ in range(n)] # 더해지는 양분 수
nutrient = [[5]*n for _ in range(n)] # 초기 양분
board = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    x, y, z = map(int, input().split())
    board[x][y].append(z) # 나무 나이

print(board)
cnt = 0
while(cnt < k):
    temp = deepcopy(nutrient)
    for i in range(n):
        for j in range(n):
            if(board[i][j]):
                board[i][j].sort()
            for k in range(len(board[i][j])):
                if(nutrient[i][j] < board[i][j][k]):

                else:
                    nutrient[i][j] -= board[i][j][k]
                    board[i][j][k] += 1

