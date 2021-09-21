import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

num = [i for i in range(n)]
_min = sys.maxsize

start = list(combinations(range(n), n//2))
for i in range(len(start)):
    link = list(set(num) - set(start[i]))
    
    start_sum, link_sum = 0, 0
    
    start_combi = list(combinations(start[i], 2))
    link_combi = list(combinations(link, 2))
    
    for idx in range(len(start_combi)):
        x, y = start_combi[idx]
        start_sum += s[x][y]
        start_sum += s[y][x]
    
    for idx in range(len(link_combi)):
        x, y = link_combi[idx]
        link_sum += s[x][y]
        link_sum += s[y][x]

    _min = min(_min, abs(start_sum - link_sum))

print(_min)