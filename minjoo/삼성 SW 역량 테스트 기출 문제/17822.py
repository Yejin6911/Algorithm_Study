import sys
from copy import deepcopy
input = sys.stdin.readline

n, m, t = map(int, input().split()) # 원판의 개수, 숫자의 개수, 회전 수
board = [0]
for _ in range(n):
    board.append(list(map(int, input().split())))

def rotation(b, n): # 시계방향
    temp = b[m-n:]
    b = b[:m-n]
    b = temp + b
    return b

def delete(board):
    tempboard = deepcopy(board)
    flag = 0
    for i in range(1, n+1):
        for j in range(m):
            if(type(board[i][j])==int and type(board[i][j-1])==int and board[i][j] == board[i][j-1]):
                tempboard[i][j], tempboard[i][j-1] = "x", "x" # 지우기
                flag = 1
    for i in range(1, n):
        for j in range(m):
            if(type(board[i][j])==int and type(board[i+1][j])==int and board[i][j] == board[i+1][j]):
                tempboard[i][j], tempboard[i+1][j] = "x", "x" # 지우기
                flag = 1

    if(flag == 0): # 인접하는 수가 없으면
        summ = 0
        cnt = 0
        for i in range(1, n+1):
            for j in range(m):
                if(type(board[i][j]) == int):
                    summ += board[i][j]
                    cnt += 1
        if(cnt > 0):
            avg = summ / cnt
            for i in range(1, n+1):
                for j in range(m):
                    if(type(board[i][j]) == int):
                        if(board[i][j] > avg):
                            tempboard[i][j] -= 1
                        elif(board[i][j] < avg):
                            tempboard[i][j] += 1

    return tempboard

for _ in range(t):
    x, d, k = map(int, input().split()) # 원판번호, 방향, 회전 칸 수
    if(d == 1): # 반시계 -> 시계
        k = m - k

    idx = 1
    while(x*idx <= n):
        board[x*idx] = rotation(board[x*idx], k) # 회전
        idx += 1

    board = delete(board)

result = 0
for i in range(1, n+1):
    for j in range(m):
        if(type(board[i][j]) == int):
            result += board[i][j]

print(result)    

