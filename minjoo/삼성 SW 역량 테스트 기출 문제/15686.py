import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
house = [] # 집
chicken = [] # 치킨집
for i in range(n):
    for j in range(n):
        if(board[i][j] == 1):
            house.append([i, j])
        elif(board[i][j] == 2):
            chicken.append([i, j])


def cal(house, chicken): # 최소거리 계산
    min_list = []
    for i in range(len(house)):
        min_distance = sys.maxsize
        for j in range(len(chicken)):
            distance = abs(chicken[j][0]-house[i][0]) + abs(chicken[j][1]-house[i][1])
            min_distance = min(min_distance, distance)
        min_list.append(min_distance)
    return sum(min_list)

def close(m, chicken): # 폐업하지 않을 치킨집 m개 고르기
    res = sys.maxsize
    comb = list(combinations(chicken, m))
    for c in comb: # 조합의 각 경우의 수의 최소거리 계산
        ans = cal(house, c)
        res = min(res, ans) # 최솟값 갱신
    return res
    

print(close(m, chicken))
