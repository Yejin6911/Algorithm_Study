import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, L, R = map(int, input().split()) # 땅크기, L명이상, R명이하
P = [list(map(int, input().split())) for _ in range(N)] # 인구수
check = [[True] * N for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
count = 0

def go(x, y):
    global stack
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0<=nx<N and 0<=ny<N and check[nx][ny]):
            if(L<=abs(P[x][y]-P[nx][ny])<=R):
                check[nx][ny] = False
                stack.append([nx, ny])
                go(nx, ny)

while(1):
    check = [[True] * N for _ in range(N)]
    flag = True
    for i in range(N):
        for j in range(N):
            stack = []     
            if(check[i][j]):
                stack.append([i, j])
                check[i][j] = False
                go(i, j)

                if(len(stack) > 1):
                    flag = False
                    avg = sum([P[x][y] for x, y in stack]) // len(stack)
                    for x, y in stack:
                        P[x][y] = avg
    if flag:
        break
    count += 1

print(count)
