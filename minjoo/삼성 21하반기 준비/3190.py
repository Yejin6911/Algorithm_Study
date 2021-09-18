n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1 # 사과

l = int(input()) # 뱀 변환 횟수
change = []
for _ in range(l):
    x, c = input().split()
    change.append([int(x), c])

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

sec = 0
body = [[0, 0]] # 머리는 맨 앞, 꼬리는 맨 뒤
idx = 0 # 현재 방향 인덱스

while(1):
    sec += 1
    x, y = body[0]
    nx, ny = x + dx[idx], y + dy[idx]
    if(not(0<=nx<n and 0<=ny<n) or [nx, ny] in body): # 벽이나 몸에 부딪히면
        break

    body.insert(0, [nx, ny]) # 머리 옮기기
    if(board[nx][ny] == 1): # 사과가 있으면
        board[nx][ny] = 0 # 사과 냠
    else: # 사과가 없으면
        body.pop() # 꼬리 앞으로 땡기기

    if(change):
        if(change[0][0] == sec):
            if(change[0][1] == 'L'): # 왼쪽으로 90도 회전
                idx -= 1
                if(idx < 0):
                    idx += 4
            else: # 오른쪽으로 90도 회전
                idx += 1
                if(idx > 3):
                    idx -= 4
            change.pop(0)
print(sec)
    


    
