import sys
from copy import deepcopy
input = sys.stdin.readline

n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board.insert(0, 0)

def spin(x, k): # 시계방향
    global board
    idx = m-k
    board[x] = board[x][idx:] + board[x][:idx]

def delete():
    flag = 0
    temp = deepcopy(board)
    for i in range(1, n+1):
        for j in range(m-1):
            if(board[i][j] != 'x' and board[i][j] == board[i][j+1]):
                temp[i][j] = 'x'
                temp[i][j+1] = 'x'
                flag = 1
        if(board[i][0] != 'x' and board[i][0] == board[i][-1]):
            temp[i][0] = 'x'
            temp[i][-1] = 'x'
            flag = 1
    for i in range(1, n):
        for j in range(m):
            if(board[i][j] != 'x' and board[i][j] == board[i+1][j]):
                temp[i][j] = 'x'
                temp[i+1][j] = 'x'
                flag = 1
    return temp, flag

def getsumcnt():
    ans = 0
    cnt = 0
    for i in range(1, n+1):
        for j in range(m):
            if(board[i][j] != 'x'):
                ans += board[i][j]
                cnt += 1
    return ans, cnt

for _ in range(t):
    x, d, k = map(int, input().split())
    nx = x
    while(nx <= n):
        if(d == 0):
            spin(nx, k%m)
        else:
            spin(nx, (m-k)%m)
        nx = nx + x
   
    board, flag = delete()

    if(flag == 0):
        _sum, cnt = getsumcnt()
        if(cnt != 0):
            avg = _sum / cnt
            for i in range(1, n+1):
                for j in range(m):
                    if(board[i][j] != 'x'):
                        if(avg < board[i][j]):
                            board[i][j] -= 1
                        elif(avg > board[i][j]):
                            board[i][j] += 1
    
ans, cnt = getsumcnt()
print(ans)
