import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split()) # 세로, 가로
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1) # 왼, 위, 오, 아
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

q = deque()

def init():
    rx, ry, bx, by = [0] * 4 # 초기화
    for i in range(n):
        for j in range(m):
            if(board[i][j] == 'R'): # 빨간공 위치
                rx, ry = i, j
            elif(board[i][j] == 'B'): # 파란공 위치
                bx, by = i, j
    # print(rx, ry, bx, by)
    q.append((rx, ry, bx, by, 1)) # 위치정보와 몇번 움직였는지
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    count = 0 # 이동한 칸 수
    while(board[x+dx][y+dy] != '#' and board[x][y] != 'O'):
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    init()
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10: # 이동횟수 10번 넘으면 실패
            break

        for i in range(len(dx)):
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i])

            if(board[next_bx][next_by] == 'O'): # 파란공이 구멍에 있으면 다음 동작으로
                continue
            if(board[next_rx][next_ry] == 'O'): # 빨간공이 구멍에 있으면
                print(depth) # 성공
                return
            if(next_rx == next_bx and next_ry == next_by): # 둘이 같은 곳으로 쏠렸을 경우
                if(r_count > b_count): # 더 많이 이동한 구슬을 한칸 뒤로
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]

            if not visited[next_rx][next_ry][next_bx][next_by]: # 방문 안했으면
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth+1)) # 큐에 넣어주기
    print(-1) # 실패

bfs()