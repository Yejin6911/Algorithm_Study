import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

ans = [0 for _ in range(n)]
ans[0] = nums[0]

for i in range(1, n):
    ans[i] = max(ans[i-1]+nums[i], nums[i])

print(max(ans))