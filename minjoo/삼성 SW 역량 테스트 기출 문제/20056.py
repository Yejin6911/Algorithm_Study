# pypy로 제출
import sys
from copy import deepcopy
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split()) # 격자크기, 파이어볼 개수, 명령 개수
fireballnumber = m+2
board = [[[] for _ in range(n)] for _ in range(n)]
fireball = {}
for i in range(1, m+1):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1] = [i] # i번 파이어볼
    fireball[i] = [r-1, c-1, m, s, d] # 위치(x, y), 질량, 속력, 방향

cnt = 0

while(cnt < k):
    key = list(fireball.keys())
    for u in range(len(key)): # 파이어볼 이동
        i = key[u]
        x, y, m, s, d = fireball[i]
        board[x][y].remove(i) # 제거
    
        x = x + (dx[d]*s)
        y = y + (dy[d]*s)
        if(x < 0):
            x = (((x*(-1)) % n)*(-1)) + n
        if(y < 0):
            y = (((y*(-1)) % n)*(-1)) + n
        if(x >= n):
            x = x % n
        if(y >= n):
            y = y % n
        board[x][y].append(i)
        fireball[i] = [x, y, m, s, d]
    
    for i in range(n): # 겹치는 파이어볼 체크
        for j in range(n):
            if(len(board[i][j]) > 1):
                num = len(board[i][j]) # 합쳐지는 파이어볼의 개수
                sum_m, sum_s, direc = 0, 0, []
                for f in range(num):
                    idx = board[i][j][f]
                    sum_m += fireball[idx][2]
                    sum_s += fireball[idx][3]
                    direc.append(fireball[idx][4] % 2)
                    del fireball[idx]
                m = sum_m // 5
                if(m == 0):
                    board[i][j] = []
                    continue
                s = sum_s // num
                if(len(list(set(direc))) > 1):
                    d = [1, 3, 5, 7]
                else:
                    d = [0, 2, 4, 6]
                f = fireballnumber
                board[i][j] = [f, f+1, f+2, f+3]
                fireball[f] = [i, j, m, s, d[0]]
                fireball[f+1] = [i, j, m, s, d[1]]
                fireball[f+2] = [i, j, m, s, d[2]]
                fireball[f+3] = [i, j, m, s, d[3]]
                fireballnumber = f+4
              

    # print(board)
    # print(fireball)
    cnt += 1

result = 0
key = list(fireball.keys())
for i in range(len(key)):
    result += fireball[key[i]][2]

print(result)


