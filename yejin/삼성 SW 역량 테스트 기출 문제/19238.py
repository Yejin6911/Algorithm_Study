from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, fuel = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(n)]

r, c = map(int, input().rstrip().split())
start = (r-1, c-1)

S = []
E = []
for i in range(m):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    S.append((x1-1, y1-1))
    E.append((x2-1, y2-1))


def select(taxi):
    global fuel
    if taxi in S:
        return taxi
    visited = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append((taxi))
    visited[taxi[0]][taxi[1]] = 1
    dist = 0
    customer = []
    while queue:
        dist += 1
        if dist >= fuel:
            return 0
        length = len(queue)
        for _ in range(length):
            x, y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and visited[nx][ny] == 0:
                    if (nx, ny) in S:
                        customer.append((nx, ny))
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
        if customer:
            break
    if not customer:
        return 0
    fuel -= dist
    customer.sort(key=lambda x: (x[0], x[1]))
    return customer[0]


def move(customer):
    global fuel
    idx = S.index(customer)
    visited = [[-1]*n for _ in range(n)]
    queue = deque()
    queue.append(customer)
    visited[customer[0]][customer[1]] = 0
    while queue:
        x, y = queue.popleft()
        if visited[x][y] >= fuel:
            return 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y]+1
                if (nx, ny) == E[idx]:
                    # 연료 충전
                    fuel += visited[nx][ny]
                    S.pop(idx)
                    E.pop(idx)
                    return (nx, ny)
    return 0


for _ in range(m):
    customer = select(start)
    # 선택할 수 있는 손님 없는 경우
    if customer == 0:
        fuel = -1
        break
    # 연료가 부족한 경우
    if fuel < 0:
        fuel = -1
        break
    start = move(customer)
    # 도착지까지 갈 수 없는 경우
    if start == 0:
        fuel = -1
        break
print(fuel)
