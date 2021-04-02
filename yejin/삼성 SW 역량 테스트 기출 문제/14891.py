import sys
from collections import deque

gears = []
for i in range(4):
    gear = deque(list(map(int, list(sys.stdin.readline().rstrip()))))
    gears.append(gear)

k = int(sys.stdin.readline().rstrip())
orders = [list(map(int, sys.stdin.readline().rstrip().split()))
          for _ in range(k)]


def spin(gears, g, direction):
    left = gears[g][6]
    right = gears[g][2]
    # 1. 해당 톱니바퀴 회전
    if direction == 1:
        temp = gears[g].pop()
        gears[g].appendleft(temp)
    else:
        temp = gears[g].popleft()
        gears[g].append(temp)
    # 2. 왼쪽 톱니바퀴 회전
    now_dir = direction
    for i in range(g-1, -1, -1):
        if gears[i][2] != left:
            left = gears[i][6]
            # 전 톱니바퀴가 시계방향 -> 현재 반시계방향
            if now_dir == 1:
                temp = gears[i].popleft()
                gears[i].append(temp)
                now_dir = -1
            # 전 톱니바퀴가 반시계방향 -> 현재 시계방향
            else:
                temp = gears[i].pop()
                gears[i].appendleft(temp)
                now_dir = 1
        else:
            break
    # 3. 오른쪽 톱니바퀴 회전
    now_dir = direction
    for i in range(g+1, 4):
        if gears[i][6] != right:
            right = gears[i][2]
            # 전 톱니바퀴가 시계방향 -> 현재 반시계방향
            if now_dir == 1:
                temp = gears[i].popleft()
                gears[i].append(temp)
                now_dir = -1
            else:
                temp = gears[i].pop()
                gears[i].appendleft(temp)
                now_dir = 1
        else:
            break


for order in orders:
    spin(gears, order[0]-1, order[1])

score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += 2 ** i
print(score)
