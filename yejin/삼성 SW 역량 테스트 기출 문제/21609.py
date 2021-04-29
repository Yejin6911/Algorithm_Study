from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find():
    # [블록 수, 무지개 블록 수, 기준 블록(행), 기준 블록(열), 포함되는 블록]
    block = []
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 일반 블록일 때
            if board[i][j] > 0 and not visited[i][j]:
                color = board[i][j]
                visited[i][j] = 1
                queue = deque()
                queue.append((i, j))
                temp = [(i, j)]
                rainbow = []  # 기준 블록이 무지개색이면 안되기 때문에 따로 저장
                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx = x+dx[d]
                        ny = y+dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] == color and (nx, ny) not in temp:
                                visited[nx][ny] = 1
                                queue.append((nx, ny))
                                temp.append((nx, ny))
                            elif board[nx][ny] == 0 and (nx, ny) not in rainbow:
                                queue.append((nx, ny))
                                rainbow.append((nx, ny))
                if len(temp)+len(rainbow) >= 2:
                    temp.sort()
                    block.append([len(temp)+len(rainbow), len(rainbow), temp[0][0], temp[0][1], temp+rainbow])
    if not len(block):
        return -1
    block.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    return block[0][4]

#가장 큰 블록 제거
def remove(block):
    for b in block:
        board[b[0]][b[1]] = -2
    return len(block)**2

#중력 작용
def move():
    for y in range(n):
        for x in range(n-2, -1, -1):
            if board[x][y] < 0:
                continue
            else:
                if board[x+1][y] == -2:
                    temp = x+1
                    while temp+1 < n:
                        if board[temp+1][y] == -2:
                            temp += 1
                        else:
                            break
                    board[temp][y], board[x][y] = board[x][y], -2

#90도 반시계방향 회전
def spin():
    new_board = []
    for y in range(n-1, -1, -1):
        temp = []
        for x in range(n):
            temp.append(board[x][y])
        new_board.append(temp)
    return new_board


result = 0
while True:
    block = find()
		#더 이상 블록 없는 경우
    if block == -1:
        break
    result += remove(block)
    move()
    board = spin()
    move()

print(result)