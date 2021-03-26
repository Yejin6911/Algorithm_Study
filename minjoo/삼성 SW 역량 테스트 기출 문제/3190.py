import sys

input = sys.stdin.readline

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

board = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

L = int(input())
change = [] # 뱀의 방향 변환
for _ in range(L):
    sec, direc = input().split()
    change.append([int(sec), direc])
sec, direc = change.pop(0)

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
i = 0 

head_x, head_y = 1, 1 # 뱀 머리 위치
tail_x, tail_y = 1, 1 # 뱀 꼬리 위치

time = 0 # 현재 시간
length = 1 # 뱀 길이
visited = []

while(0<head_x<n+1 and 0<head_y<n+1):
    if(time == sec):
        if(direc == 'D'):
            i = (i + 1) % 4
        else:
            i = (i + 3) % 4
        if(change):
            sec, direc = change.pop(0)
    
    head_x += dx[i] # 일단 머리 옮김
    head_y += dy[i]

    if(not(0<head_x<n+1 and 0<head_y<n+1) or ([head_x, head_y] in visited) or (head_x == tail_x and head_y == tail_y)):
        break
 
    visited.append([head_x, head_y])

    if(board[head_x][head_y] == 0): # 사과가 없으면
        tail_x, tail_y = visited.pop(0) # 꼬리 움직임
    else:
        board[head_x][head_y] = 0 # 사과 먹음
        
    time += 1

print(time + 1)
