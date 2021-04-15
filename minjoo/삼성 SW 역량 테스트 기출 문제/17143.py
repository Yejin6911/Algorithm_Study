# pypy 제출
import sys
from copy import deepcopy
input = sys.stdin.readline

r, c, m = map(int, input().split()) # 격자판 크기 rc, 상어의 수
board = [[[] for _ in range(c)] for _ in range(r)]
dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, 1, -1] # 위 아래 오른쪽 왼쪽

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    board[x-1][y-1] = [z, s, d] # 크기, 속력, 방향

result = 0
def catch(location):
    global board, result
    for i in range(r):
        if(board[i][location]):
            result += board[i][location][0] # 크기 더하기
            board[i][location] = [] # 상어 잡기
            break

def move():
    global board
    tempboard = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if(board[i][j]):
                x, y = i, j # 원래 위치
                z, s, d = board[i][j] # 크기, 속력, 방향
                for _ in range(s): # 속력만큼 상어 이동
                    nx = x + dx[d] 
                    ny = y + dy[d]
                    if(not(0<=nx<r and 0<=ny<c)):
                        if(d == 1):
                            d = 2
                        elif(d == 2):
                            d = 1
                        elif(d == 3):
                            d = 4
                        elif(d == 4):
                            d = 3
                        nx = x + dx[d]
                        ny = y + dy[d]
                    x, y = nx, ny 

                if(tempboard[x][y]): # 이미 있으면
                    if(type(tempboard[x][y][0]) == int):
                        tempboard[x][y] = [tempboard[x][y], [z, s, d]]
                    else:
                        tempboard[x][y].append([z, s, d])
                else:
                    tempboard[x][y] = [z, s, d]
                    
    for i in range(r):
        for j in range(c):
            if(len(tempboard[i][j]) > 1 and type(tempboard[i][j][0]) == list):
                # print(tempboard)
                tempboard[i][j].sort(reverse=True, key=lambda x:x[0]) # 크기순 정렬
                tempboard[i][j] = tempboard[i][j][0]

    board = deepcopy(tempboard)

for location in range(c):
   
    catch(location)
    move()  

print(result)               
                               

