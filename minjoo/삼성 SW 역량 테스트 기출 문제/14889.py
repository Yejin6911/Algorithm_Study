import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input()) # 사람 수
s = [list(map(int, input().split())) for _ in range(n)]
num_list = [i for i in range(n)]
cb = combinations(num_list, n//2)

min_result = sys.maxsize

def solution():
    global min_result

    for c in cb:
        start_member = list(c)
        link_member = list(set(num_list)-set(c))
        
        start_comb = list(combinations(start_member, 2))
        link_comb = list(combinations(link_member, 2))

        start_sum = 0
        for x, y in start_comb:
            start_sum += (s[x][y] + s[y][x])
        
        link_sum = 0
        for x, y in link_comb:
            link_sum += (s[x][y] + s[y][x])

        if(min_result > abs(start_sum - link_sum)):
            min_result = abs(start_sum - link_sum)

solution()
print(min_result)
    
