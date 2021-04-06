import sys
import copy
from collections import defaultdict

input = sys.stdin.readline

n, m, h = map(int, input().rstrip().split())

bridge = [[False]*n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    bridge[a-1][b-1] = True


def check():
    for i in range(n):
        start = i
        for j in range(h):
            if bridge[j][start]:
                start += 1
            elif start > 0 and bridge[j][start-1]:
                start -= 1
        if i != start:
            return False
    return True


# x: 현재 가로선 위치, y: 현재 세로선 위치
def dfs(cnt, x, y):
    global result
    if check():
        result = min(result, cnt)
        return
    elif cnt == 3 or result <= cnt:
        return
    for i in range(x, h):
        # 여기 잘 이해 안됌...
        k = y if i == x else 0
        for j in range(k, n-1):
            if not bridge[i][j] and not bridge[i][j+1]:
                bridge[i][j] = True
                dfs(cnt+1, i, j+2)
                bridge[i][j] = False


result = 4
dfs(0, 0, 0)
if result < 4:
    print(result)
else:
    print(-1)
