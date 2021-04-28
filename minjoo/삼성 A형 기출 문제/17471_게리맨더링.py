import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n = int(input()) # 구역의 개수
population = list(map(int, input().split())) # 구역의 인구
population.insert(0, 0)
print(population)
board = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, len(line)):
        board[i][line[j]] = 1
        board[line[j]][i] = 1

print(board)
nums = [i for i in range(1, n+1)]
candidates = []
for i in range(1, n//2+1):
    candidates.append(list(combinations(nums, i)))

# print(candidates)
min_result = sys.maxsize
for i in range(len(candidates)):
    for j in range(len(candidates[i])):
        flag = 1
        first = deepcopy(nums)
        second = []
        case = candidates[i][j]
        for k in range(len(case)):
            second.append(case[k])
            first.remove(case[k])
        print(first, second)
        # [1, 2] [3, 4, 5, 6]
        if(len(first) > 1):
            check_list = list(combinations(first, 2))
            for z in range(len(check_list)):
                a, b = check_list[z]
                if(board[a][b] == 1 or board[b][a] == 1):
                    flag = 1
                    break
        if(flag == 1):
            if(len(second) > 1):
                check_list = list(combinations(second, 2))
                for z in range(len(check_list)):
                    a, b = check_list[z]
                    if(board[a][b] == 0 or board[b][a] == 0):
                        flag = 1
                        break
        else:
            continue

        if(flag == 0):
            continue
        else:
            first_p, second_p = 0, 0
            for k in range(len(first)):
                first_p += population[first[k]]
            for k in range(len(second)):
                second_p += population[second[k]]
            print(first_p, second_p)
            min_result = min(abs(first_p - second_p), min_result)

print(min_result)