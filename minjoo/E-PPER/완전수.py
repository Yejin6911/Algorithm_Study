k = int(input())
nums = list(map(int, input().split()))
ans = []

for i in range(k):
    t = []
    for j in range(1, nums[i]//2+1):
        if(nums[i] % j == 0):
            t.append(j)
    if(sum(t) == nums[i]):
        ans.append("YES")
    else:
        ans.append("NO")

print(ans)
