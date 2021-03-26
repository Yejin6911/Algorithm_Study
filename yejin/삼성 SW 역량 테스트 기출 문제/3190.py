import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
apples = []
for i in range(K):
    row, col = map(int, sys.stdin.readline().rstrip().split())
    apples.append((row, col))

L = int(sys.stdin.readline().rstrip())
changes = {}
for i in range(L):
    x, c = sys.stdin.readline().rstrip().split()
    changes[int(x)] = c

head = [1, 1]
snakes = deque()
snakes.append((1, 1))
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
time = 0
now_d = 0
while True:
    # 방향 전환 여부 확인
    if time in changes.keys():
        if changes[time] == "D":
            now_d = (now_d+1) % 4
        else:
            now_d -= 1
            if now_d < 0:
                now_d += 4
    # 머리 한칸 이동
    time += 1
    head[0] += direction[now_d][0]
    head[1] += direction[now_d][1]
    if head[0] > N or head[0] <= 0 or head[1] > N or head[1] <= 0 or (head[0], head[1]) in snakes:
        print(time)
        break
    # 사과 인 경우
    if (head[0], head[1]) in apples:
        # 길이 증가
        snakes.appendleft((head[0], head[1]))
        # 사과 제거
        apples.remove((head[0], head[1]))
    # 사과 아닌 경우
    else:
        snakes.appendleft((head[0], head[1]))
        snakes.pop()
