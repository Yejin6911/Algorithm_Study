import sys
from copy import deepcopy
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

a = [[] for _ in range(4)] # 전체 판
fish = [[] for _ in range(16)] # 물고기 좌표
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0, 7, 2):
        a[i].append([temp[j]-1, temp[j+1]-1])
        fish[temp[j]-1] = [i, j // 2]

ans = 0
d, cnt = a[0][0][1], a[0][0][0] + 1
fish[a[0][0][0]], a[0][0] = [], []


def dfs(x, y, d, cnt):
    global ans, a, fish
    move_fish(x, y)
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            ans = max(ans, cnt)
            return
        if not a[nx][ny]: # 물고기 없으면
            x, y = nx, ny
            continue

        temp_a, temp_fish = deepcopy(a), deepcopy(fish)
        temp1, temp2 = fish[a[nx][ny][0]], a[nx][ny]
        fish[a[nx][ny][0]], a[nx][ny] = [], []
        dfs(nx, ny, temp2[1], cnt + temp2[0] + 1)
        a, fish = temp_a, temp_fish
        fish[a[nx][ny][0]], a[nx][ny] = temp1, temp2
        x, y = nx, ny

def move_fish(sx, sy):
    for i in range(16):
        if fish[i]: # 안잡아먹힌 물고기
            x, y = fish[i][0], fish[i][1]
            for _ in range(9):
                nx, ny = x + dx[a[x][y][1]], y + dy[a[x][y][1]]
                if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx == sx and ny == sy):
                    a[x][y][1] = (a[x][y][1] + 1) % 8 # 다음 방향 탐색
                    continue
                if a[nx][ny]:
                    fish[a[nx][ny][0]] = [x, y] # 물고기 위치 바꿔주기
                a[nx][ny], a[x][y] = a[x][y], a[nx][ny]
                fish[i] = [nx, ny] 
                break

dfs(0, 0, d, cnt)
print(ans)

# dx, dy = [0, -1, -1, 0, 1, 1, 1, 0, -1], [0, 0, -1, -1, -1, 0, 1, 1, 1]

# board = [[[] for _ in range(4)] for _ in range(4)]
# for i in range(4):
#     line = list(map(int, input().split()))
#     for j in range(4):
#         temp = line[:2]
#         line = line[2:]
#         board[i][j] = temp

# result = board[0][0][0] # 시작할 때 먹는 물고기
# board[0][0][0] = -1


# def eat(x, y, d):
#     global result, board
#     while(1):
#         move(x, y)
#         print(board)
#         d = board[x][y][1]
#         cand = [] # 먹을 물고기 후보
#         while(1):
#             nx = x + dx[d] # 다음 좌표
#             ny = y + dy[d]
#             if(0<=nx<4 and 0<=ny<4):
#                 num = board[nx][ny][0]
#                 if(num > 0): # 물고기가 있으면
#                     cand.append([num, nx, ny])
#                     x, y = nx, ny
#             else:
#                 break
#         if(cand): # 후보가 있으면
#             cand.sort(reverse=True, key = lambda x:x[0]) # 큰 번호 순으로 물고기 정렬
#             result += cand[0][0]
#             print(result)
#             x, y = cand[0][1], cand[0][2]
#             board[x][y][0] = -1 # 먹음
#             d = board[x][y][1]
#         else:
#             return

# def move(x, y): # 상어 위치
#     num = 1
#     global board
#     while(num < 17):
#         flag = 0
#         for i in range(4):
#             for j in range(4):
#                 if(board[i][j][0] == num):
#                     d = board[i][j][1]
#                     for _ in range(8):
#                         ni = i + dx[d]
#                         nj = j + dy[d]
#                         if(0<=ni<4 and 0<=nj<4 and [x, y]!=[ni, nj]):
#                             if(board[ni][nj][0] == -1): # 빈칸이면
#                                 board[ni][nj][0] = num
#                                 board[ni][nj][1] = d
#                                 board[i][j][0] = -1
#                                 board[i][j][1] = -1
#                             else: # 다른 물고기가 있으면
#                                 num2, d2 = board[ni][nj][0], board[ni][nj][1]
#                                 board[ni][nj][0], board[ni][nj][1] = num, d
#                                 board[i][j][0], board[i][j][1] = num2, d2
#                             break
#                         else:
#                             d += 1
#                             if(d == 9):
#                                 d = 1
#                     flag = 1
#                     break
#             if(flag == 1):
#                 break
#         num += 1




# eat(0, 0, board[0][1])  
# print(result)