import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if(board[i][j] == 1):
            house.append([i, j])
        elif(board[i][j] == 2):
            chicken.append([i, j])


def cal(house, chicken):
    min_list = []
    for i in range(len(house)):
        min_distance = sys.maxsize
        for j in range(len(chicken)):
            distance = abs(chicken[j][0]-house[i][0]) + abs(chicken[j][1]-house[i][1])
            min_distance = min(min_distance, distance)
        min_list.append(min_distance)
    return sum(min_list)

def close(m, chicken):
    res = sys.maxsize
    comb = list(combinations(chicken, m))
    for c in comb:
        ans = cal(house, c)
        res = min(res, ans)
    return res
    

print(close(m, chicken))