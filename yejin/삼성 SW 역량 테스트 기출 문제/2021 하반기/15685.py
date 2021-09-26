import copy
import sys
input = sys.stdin.readline


dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # (행,열) (y,x)


def draw(x, y, d, g):
    new = [(y, x)]
    for i in range(g+1):
        if i == 0:
            nx = x+dir[d][1]
            ny = y+dir[d][0]
            new.append((ny, nx))
        else:
            for j in range(len(new)-1, 0, -1):
                start = new[-1]
                # 기존방향구하기
                d = (new[j][0]-new[j-1][0], new[j][1]-new[j-1][1])
                # 회전
                nd = (dir.index(d)+1) % 4
                # 새로운 위치추가
                nx = start[1]+dir[nd][1]
                ny = start[0]+dir[nd][0]
                new.append((ny, nx))
    dragon.extend(new)


n = int(input())
dragon = []
for _ in range(n):
    x, y, d, g = map(int, input().split())
    draw(x, y, d, g)

dragon = list(set(dragon))
cnt = 0
for (y, x) in dragon:
    if (y, x) in dragon and (y+1, x) in dragon and (y, x+1) in dragon and (y+1, x+1) in dragon:
        cnt += 1
print(cnt)
