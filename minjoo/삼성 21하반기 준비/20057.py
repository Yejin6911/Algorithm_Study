import sys
input = sys.stdin.readline

n = int(input()) # 격자의 크기
board = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0] # 왼, 아래, 오, 위
portion = [[[-1, 1, 1], [-1, 0, 7], [-1, -1, 10], [-2, 0, 2], [0, -2, 5], [1, -1, 10], [1, 0, 7], [1, 1, 1], [2, 0, 2]], 
[[-1, -1, 1], [-1, 1, 1], [0, -2, 2], [0, -1, 7], [0, 1, 7], [0, 2, 2], [1, -1, 10], [1, 1, 10], [2, 0, 5]],
[[-2, 0, 2], [-1, -1, 1], [-1, 0, 7], [-1, 1, 10], [0, 2, 5], [1, -1, 1], [1, 0, 7], [1, 1, 10], [2, 0, 2]],
[[-2, 0, 5], [-1, -1, 10], [-1, 1, 10], [0, -2, 2], [0, -1, 7], [0, 1, 7], [0, 2, 2], [1, -1, 1], [1, 1, 1]]] # y 기준 (nx, ny)

alpha = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def wind(board):
    ans = 0 # 격자 밖으로 나간 모래
    x, y = n//2, n//2 # 가장 중심 (시작)
    length = 1
    idx = 0 # 방향 인덱스, 왼쪽부터 시작
    while([x, y] != [0, 0]):
        cnt = 0
        while(cnt < 2):
            for _ in range(length):
                if([x, y] == [0, 0]):
                    break
                nx = x + dx[idx]
                ny = y + dy[idx]
                sand = board[nx][ny]
                blow = 0
                for i in range(len(portion[idx])):
                    ddx, ddy, p = portion[idx][i]
                    nnx = nx + ddx
                    nny = ny + ddy
                    if(0<=nnx<n and 0<=nny<n):
                        board[nnx][nny] += (sand * p)//100
                    else:
                        ans += (sand * p)//100
                    blow += (sand * p)//100
                sand -= blow
                nnx, nny = nx + alpha[idx][0], ny + alpha[idx][1]
                if(0<=nnx<n and 0<=nny<n):
                    board[nnx][nny] += sand # 알파
                else:
                    ans += sand

                x, y = nx, ny

            idx += 1
            if(idx > 3):
                idx = 0
            cnt += 1

        length += 1
    return ans

ans = wind(board)
print(ans)