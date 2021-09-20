import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split()) # 로봇청소기 좌표, 방향

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서

board = [list(map(int, input().split())) for _ in range(n)]

ans = 0 # 로봇청소기가 청소하는 칸의 개수

while(1):
    # 1. 현재 칸 청소
    if(board[x][y] == 0):
        board[x][y] = 2
        ans += 1

    # 2. 현재 방향을 기준으로 왼쪽 방향부터 인접한 칸 탐색
    flag = 0
    for i in range(4):
        nd = d - 1 # 왼쪽 방향
        if(nd < 0):
            nd += 4
        
        nx, ny = x + dx[nd], y + dy[nd]
        # 2. a. 아직 청소하지 않은 공간이 존재한다면
        if(0<=nx<n and 0<=ny<m and board[nx][ny] == 0):
            d = nd # 그 방향으로 회전
            x, y = nx, ny # 한칸 전진
            flag = 1
            break
        # 2. b. 청소할 공간이 없다면
        else:
            d = nd # 그 방향으로 회전
    
    # 2.c 네 방향 모두 청소가 되어있거나 벽인 경우
    if(flag == 0):
        nx, ny = x - dx[d], y - dy[d] # 한칸 후진
        if(0<=nx<n and 0<=ny<m and board[nx][ny] != 1):
            x, y = nx, ny
            
        # 후진도 못하면
        else:
            break
     
print(ans)