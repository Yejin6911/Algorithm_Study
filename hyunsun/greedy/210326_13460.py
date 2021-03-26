N, M = map(int, input().split())
B = [list(input().rstrip()) for _ in range(N)]  # Board
dx = [-1, 1, 0, 0]  # x축 움직임
dy = [0, 0, -1, 1]  # y축 움직임
queue = []  # BFS : queue 활용
# Red(rx,ry)와 Blue(bx,by)의 탐사 여부 체크
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def pos_init():
    rx, ry, bx, by = 0, 0, 0, 0  # 초기화
    for i in range(N):
        for j in range(M):
            if B[i][j] == 'R':
                rx, ry = i, j
            elif B[i][j] == 'B':
                bx, by = i, j
    # 위치 정보와 depth(breadth 끝나면 +1)
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    cnt = 0  # 이동 칸 수
    # 다음이 벽이거나 현재가 구멍일 때까지
    while B[x+dx][y+dy] != '#' and B[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def solve():
    pos_init()  # 시작 조건
    while queue:  # BFS : queue 기준
        rx, ry, bx, by, depth = queue.pop(0)
        if depth > 10:  # 실패 조건
            break
        for i in range(4):  # 4방향 이동 시도
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])  # Red
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])  # Blue
            if B[nbx][nby] != 'O':  # 실패 조건이 아니면
                if B[nrx][nry] == 'O':  # 성공 조건
                    print(depth)
                    return
                if nrx == nbx and nry == nby:  # 겹쳤을 때
                    if rcnt > bcnt:  # 이동거리가 많은 것을
                        nrx -= dx[i]  # 한 칸 뒤로
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                # breadth 탐색 후, 탐사 여부 체크
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    # 다음 depth의 breadth 탐색 위한 queue
                    queue.append((nrx, nry, nbx, nby, depth+1))
    print(-1)  # 실패 시

solve()

'''
n, m = map(int, input().split())
lists = [list(input().rstrip()) for _ in range(n)]
def move(x, y, mode):
    i = 1 #현위치는 문제없음
    if mode == 'r':
        while(True):
            print('r',x, y+i-1)
            if (lists[x][y+i] == 'O' ):
                return 0, 0
            elif (lists[x][y+i] == '#'):
                return x, y+i-1
            else:
                i += 1
                
    elif mode == 'l':
        while(True):
            print('l',x, y-i+1)

            if (lists[x][y-i] == 'O' ):
                return 0, 0
            elif (lists[x][y-i] == '#'):
                return x, y-i+1
            else:
                i += 1
                
    elif mode == 'u':
        while(True):
            print('u',x-i+1, y)
            if (lists[x-i][y] == 'O' ):
                return 0, 0
            elif (lists[x-i][y] == '#'):
                return x-i+1, y
            else:
                i += 1
                
    elif mode == 'd':
        while(True):
            print('d',x+i-1, y)

            if (lists[x+i][y] == 'O' ):
                return 0, 0
            elif (lists[x+i][y] == '#'):
                return x+i-1, y
            else:
                i += 1

def init_pos():
    for i in range(n):
        for j in range(m):
            if lists[i][j] == 'R':
                rx, ry = i, j
            elif lists[i][j] == 'B':
                bx, by = i, j
    return rx,ry,bx,by

rx,ry,bx,by = init_pos()
queue = []
queue.append((rx, ry, bx, by, 1))
modes = ['r','l','u','d']
i = 0
res=0
while queue:
    i += 1
    rx, ry, bx, by, depth = queue.pop(0)
    prx = rx
    pry = ry
    pbx = bx
    pby = by
    for mode in modes:
        rx, ry = move(rx, ry, mode)
        bx, by = move(bx, by, mode)
        if bx == 0 and by == 0: # 파랑 빨강 동시에 빠지면 실패라 먼저
            bx = pbx
            by = pby
        elif rx == 0 and ry == 0:
            bx = pbx
            by = pby
            break        
        else:
            queue.append((rx, ry, bx, by, i))
        if depth >= 10:
            break
    if rx == 0 and ry == 0:
        res = depth
        break
    if depth >= 10:
        res == -1
        break

#print(rx,ry,bx,by)
print(res)
'''
