import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split()))
         for _ in range(n)]


# 노가다의 정석 풀이...:)
def check(i, j):
    totals = []
    # ㅡ모양
    if j+3 < m:
        total = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]
        totals.append(total)
    # ㅣ모양
    if i+3 < n:
        total = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
        totals.append(total)
    # ㅁ모양
    if i+1 < n and j+1 < m:
        total = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]
        totals.append(total)
    # 세번째, 네번째 모양, 다섯째 중
    if i+2 < n and j+1 < m:
        total_1 = board[i][j]+board[i+1][j]+board[i+2][j]+board[i+2][j+1]
        total_2 = board[i][j]+board[i][j+1]+board[i+1][j+1]+board[i+2][j+1]
        total_3 = board[i][j]+board[i+1][j]+board[i+2][j]+board[i][j+1]
        total_4 = board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i+2][j+1]
        total_5 = board[i][j]+board[i+1][j]+board[i+2][j]+board[i+1][j+1]
        totals += [total_1, total_2, total_3, total_4, total_5]
    # 다섯번째 모양
    if i+1 < n and j+2 < m:
        total_1 = board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j+2]
        total_2 = board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j]
        total_3 = board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i+1][j+2]
        total_4 = board[i][j]+board[i][j+1]+board[i+1][j+1]+board[i+1][j+2]
        total_5 = board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j+1]
        totals += [total_1, total_2, total_3, total_4, total_5]
    # 나머지
    if i-1 >= 0 and j+2 < m:
        total_1 = board[i][j]+board[i][j+1]+board[i][j+2]+board[i-1][j+2]
        total_2 = board[i][j]+board[i][j+1]+board[i-1][j+1]+board[i-1][j+2]
        total_3 = board[i][j]+board[i][j+1]+board[i][j+2]+board[i-1][j+1]
        totals += [total_1, total_2, total_3]
    if i-2 >= 0 and j+1 < m:
        total = board[i][j]+board[i][j+1]+board[i-1][j+1]+board[i-2][j+1]
        totals.append(total)
    if i-1 >= 0 and i+1 < n and j+1 < m:
        total_1 = board[i][j]+board[i+1][j]+board[i][j+1]+board[i-1][j+1]
        total_2 = board[i][j]+board[i][j+1]+board[i-1][j+1]+board[i+1][j+1]
        totals += [total_1, total_2]
    if len(totals):
        return max(totals)
    else:
        return 0


total = 0
for i in range(n):
    for j in range(m):
        total = max(total, check(i, j))

print(total)


# 전체 경우의 수를 배열에 저장 한 뒤 위 풀이를 사용하는것이 더 깔끔
# tetrominos = [([0, 0], [0, 1], [0, 2], [0, 3]),  # ----
#               ([0, 0], [1, 0], [2, 0], [3, 0]),
#               ([0, 0], [0, 1], [1, 1], [1, 0]),  # ㅁ
#               # ㄴ 모양
#               ([0, 0], [1, 0], [1, 1], [1, 2]),
#               ([0, 0], [0, 1], [1, 0], [2, 0]),
#               ([0, 0], [0, 1], [0, 2], [1, 2]),
#               ([0, 1], [1, 1], [2, 1], [2, 0]),
#               ([0, 0], [0, 1], [1, 1], [2, 1]),
#               ([1, 0], [1, 1], [1, 2], [0, 2]),
#               ([0, 0], [1, 0], [2, 0], [2, 1]),
#               ([0, 0], [1, 0], [0, 1], [0, 2]),
#               # 번개모양
#               ([0, 0], [1, 0], [1, 1], [2, 1]),
#               ([1, 0], [1, 1], [0, 1], [0, 2]),
#               ([2, 0], [1, 0], [1, 1], [0, 1]),
#               ([0, 0], [0, 1], [1, 1], [1, 2]),
#               # ㅜ 모양
#               ([0, 0], [0, 1], [1, 1], [0, 2]),
#               ([1, 0], [0, 1], [1, 1], [2, 1]),
#               ([1, 0], [1, 1], [1, 2], [0, 1]),
#               ([0, 0], [1, 0], [1, 1], [2, 0])]
