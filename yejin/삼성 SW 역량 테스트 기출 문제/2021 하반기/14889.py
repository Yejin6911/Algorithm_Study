from itertools import combinations
import sys
input = sys.stdin.readline


def getTotal(team):
    total = 0
    for x, y in list(combinations(team, 2)):
        total += (data[x][y] + data[y][x])
    return total


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

candidates = list(combinations(range(n), int(n/2)))

answer = sys.maxsize
for i in range(len(candidates)):
    start = candidates[i]
    link = candidates[len(candidates)-1-i]
    answer = min(answer, abs(getTotal(start)-getTotal(link)))

print(answer)
