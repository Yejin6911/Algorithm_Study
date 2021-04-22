import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
def up(board):
    for j in range(n):
        for i in range(n-1):
            if(board[i][j] == board[i+1][j]):
                board[i][j] *= 2
                # if(i+2 < n):
                #     # board[i]

# def dfs(board, cnt):
#     for i in range(4):
