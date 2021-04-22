import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input()) # 사람 수
s = [list(map(int, input().split())) for _ in range(n)]

num = [i for i in range(n)]

start = list(combinations(num, n//2))
start = list(set(start))

min_result = sys.maxsize
for i in range(len(start)):
    start_score = 0
    link_score = 0
    link = list(set(num) - set(start[i]))
    start_2 = list(combinations(start[i], 2))
    link_2 = list(combinations(link, 2))

    for i in range(len(start_2)):
        x, y = start_2[i]
        start_score += s[x][y]
        start_score += s[y][x]
    for i in range(len(link_2)):
        x, y = link_2[i]
        link_score += s[x][y]
        link_score += s[y][x]

    # link_score = sum_s - start_score
    # print(link_score, start_score)
    min_result = min(abs(link_score - start_score), min_result)

print(min_result)
