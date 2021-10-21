import sys
input = sys.stdin.readline

n, m, iter = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, mm, s, d = map(int, input().split())
    board[r-1][c-1].append([mm, s, d])

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def move():
    new = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if(len(board[i][j]) > 0): # 파이어볼이 있으면
                for k in range(len(board[i][j])):
                    m, s, d = board[i][j][k]
                    if(m == 0): # 질량이 0이면 소멸
                        continue

                    nx = i + s*dx[d]
                    ny = j + s*dy[d]

                    if(nx < 0):
                        while(nx < 0):
                            nx += n
                    else:
                        nx = nx % n

                    if(ny < 0):
                        while(ny < 0):
                            ny += n
                    else:
                        ny = ny % n
                    
                    new[nx][ny].append([m, s, d])
    return new

def solution():
    for i in range(n):
        for j in range(n):
            if(len(board[i][j]) > 1): # 파이어볼이 2개 이상이면
                m_sum, s_sum, count = 0, 0, len(board[i][j])
                direc = 0
                for k in range(len(board[i][j])):
                    m, s, d = board[i][j][k]
                    m_sum += m
                    s_sum += s
                    direc += d % 2
                
                m_next = m_sum // 5
                s_next = s_sum // count

                board[i][j] = []
                if(direc == 0 or direc == count):
                    for z in range(0, 7, 2):
                        board[i][j].append([m_next, s_next, z])
                else:
                    for z in range(1, 8, 2):
                        board[i][j].append([m_next, s_next, z])
                    
for i in range(iter):
    board = move()
    solution()

result = 0
for i in range(n):
    for j in range(n):
        for k in range(len(board[i][j])):
                result += board[i][j][k][0]
print(result)