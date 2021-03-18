N = int(input())

levels = [int(input()) for _ in range(N)]
res = 0

for i in range(N-1, 0, -1):
    if levels[i] <= levels[i-1]:
        res += (levels[i-1]-levels[i]+1)
        levels[i-1] = levels[i]-1

print(res)
