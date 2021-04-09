import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
chicken = []
house = []

for i in range(n):
    row = list(map(int, input().rstrip().split()))
    for j in range(n):
        if row[j] == 1:
            house.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))


# 방법1: DFS - 시간초과
def dfs(selected):
    global result
    if len(selected) == m:
        return
    for c in chicken:
        if c not in selected:
            selected.append(c)
            total_d = 0
            # 거리 구하기
            for h in house:
                min_d = sys.maxsize
                for s in selected:
                    min_d = min(abs(h[0]-s[0])+abs(h[1]-s[1]), min_d)
                total_d += min_d
            result = min(result, total_d)
            dfs(selected)
            selected.remove(c)


result = sys.maxsize
dfs([])
print(result)


# 방법2 - combinations 이용
select = list(combinations(chicken, m))
result = sys.maxsize
for s in select:
    total = 0
    for h in house:
        min_d = sys.maxsize
        for c in s:
            d = abs(h[0]-c[0])+abs(h[1]-c[1])
            min_d = min(min_d, d)
        total += min_d
    result = min(result, total)
print(result)
