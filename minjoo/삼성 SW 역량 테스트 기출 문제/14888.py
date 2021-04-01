import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input()) # 수의 개수
nums = list(map(int, input().split())) # 숫자들
ops = list(map(int, input().split())) # + - x //

min_result = 1000000001
max_result = -1000000001

def dfs(cnt, result, p, m, mul, div):
    global max_result
    global min_result
    if(cnt == n):
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if(p):
        dfs(cnt+1, result+nums[cnt], p-1, m, mul, div)
    if(m):
        dfs(cnt+1, result-nums[cnt], p, m-1, mul, div)
    if(mul):
        dfs(cnt+1, result*nums[cnt], p, m, mul-1, div)
    if(div):
        dfs(cnt+1, -(-result//nums[cnt]) if result<0 else result//nums[cnt], p, m, mul, div-1)

dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])
print(max_result)
print(min_result)

