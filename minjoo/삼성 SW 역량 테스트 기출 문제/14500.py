import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

tetrominos = [([0, 0], [0, 1], [0, 2], [0, 3]),  # ----
              ([0, 0], [1, 0], [2, 0], [3, 0]),
              ([0, 0], [0, 1], [1, 1], [1, 0]),  # ㅁ
              # ㄴ 모양
              ([0, 0], [1, 0], [1, 1], [1, 2]),
              ([0, 0], [0, 1], [1, 0], [2, 0]),
              ([0, 0], [0, 1], [0, 2], [1, 2]),
              ([0, 1], [1, 1], [2, 1], [2, 0]),
              ([0, 0], [0, 1], [1, 1], [2, 1]),
              ([1, 0], [1, 1], [1, 2], [0, 2]),
              ([0, 0], [1, 0], [2, 0], [2, 1]),
              ([0, 0], [1, 0], [0, 1], [0, 2]),
              # 번개모양
              ([0, 0], [1, 0], [1, 1], [2, 1]),
              ([1, 0], [1, 1], [0, 1], [0, 2]),
              ([2, 0], [1, 0], [1, 1], [0, 1]),
              ([0, 0], [0, 1], [1, 1], [1, 2]),
              # ㅜ 모양
              ([0, 0], [0, 1], [1, 1], [0, 2]),
              ([1, 0], [0, 1], [1, 1], [2, 1]),
              ([1, 0], [1, 1], [1, 2], [0, 1]),
              ([0, 0], [1, 0], [1, 1], [2, 0])]

def cal_sum(r, c, t):
    ans = 0
    global n, m
    for dx, dy in t:
        nx = r + dx
        ny = c + dy
        if(0 <= nx < n and 0 <= ny < m):
            ans += board[nx][ny]
        else:
            return -1
    return ans

max_sum = 0
for r in range(n):
    for c in range(m):
        for tetromino in tetrominos:
            max_sum = max(max_sum, cal_sum(r, c, tetromino))

print(max_sum)

# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# board_sym = [] # 대칭 보드판
# for i in range(n):
#     board_sym.append(board[i][::-1])

# a = [[1, 1, 1, 1]]
# b = [[1, 1], 
#      [1, 1]]
# c = [[1, 0], 
#      [1, 0], 
#      [1, 1]] 
# d = [[1, 0], 
#      [1, 1], 
#      [0, 1]]
# e = [[1, 1, 1], 
#      [0, 1, 0]]

# tetromino = [a, b, c, d, e]

# def rotation(board):
#     new_board = [[0 for _ in range(len(board))] for _ in range(len(board[0]))]
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             new_board[j][i] = board[i][j]
#     return new_board

# def getresult(board):
#     result = []
#     for x in range(len(tetromino)):
#         maxans = 0
#         for q in range(len(board)):
#             for w in range(len(board[q])):
#                 ans = 0
#                 for i in range(len(tetromino[x])):
#                     for j in range(len(tetromino[x][i])):
#                         xx = q + i
#                         yy = w + j
#                         if(not(0<=xx<len(board) and 0<=yy<len(board[q]))):
#                             continue
#                         ans += tetromino[x][i][j] * board[xx][yy]
#                 if(ans > maxans):
#                     maxans = ans
#         result.append(maxans)
#     return result

# answer = 0
# for _ in range(4):
#     result = getresult(board)
#     if(max(result) > answer):
#         answer = max(result)
#     board = rotation(board)

# for _ in range(4):
#     result = getresult(board_sym)
#     if(max(result) > answer):
#         answer = max(result)
#     board_sym = rotation(board_sym)

# print(answer)