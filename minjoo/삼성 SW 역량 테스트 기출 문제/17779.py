import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input()) # 재현시의 크기
a = [[]]
for _ in range(n): 
    a.append([0] + list(map(int, input().split())))

def solution(x, y, d1, d2):
    result = [0 for _ in range(6)] # 인구수
    board = [[0]*(n+1) for _ in range(n+1)] # 선거구

    # 경계선 채우기
    for i in range(d1+1):
        board[x+i][y-i] = 5
        board[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        board[x+i][y+i] = 5
        board[x+d1+i][y-d1+i] = 5

    # 경계선 안쪽 채우기
    for i in range(x+1, x+d1+d2):
        flag = 0
        for j in range(n):
            if(flag == 1 and board[i][j] != 5):
                board[i][j] = 5
            elif(flag == 0 and board[i][j] == 5):
                flag = 1
            elif(flag == 1 and board[i][j] == 5):
                break
    
    # 지역구 인구 계산
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if(r < x + d1 and c <= y and board[r][c] == 0): 
                result[1] += a[r][c]
            elif(r <= x + d2 and y < c and board[r][c] == 0): 
                result[2] += a[r][c]
            elif(x + d1 <= r and c < y - d1 + d2 and board[r][c] == 0): 
                result[3] += a[r][c]
            elif(x + d2 < r and y - d1 + d2 <= c and board[r][c] == 0): 
                result[4] += a[r][c]
            elif(board[r][c] == 5): 
                result[5] += a[r][c]

    return max(result[1:]) - min(result[1:])
        

minans = sys.maxsize
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if(1 <= x < x+d1+d2 <= n and 1 <= y-d1 < y < y+d2 <= n):
                    minans = min(minans, solution(x, y, d1, d2))

print(minans)



