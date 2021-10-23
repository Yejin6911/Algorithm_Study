from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
home = []
chicken = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            home.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))
    board.append(row)

answer = sys.maxsize
candidates = list(combinations(chicken, m))

for candidate in candidates:
    total_dist = 0
    for hx, hy in home:
        dist = sys.maxsize
        for cx, cy in candidate:
            dist = min(dist, abs(hx-cx)+abs(hy-cy))
        total_dist += dist
    answer = min(total_dist, answer)

print(answer)
