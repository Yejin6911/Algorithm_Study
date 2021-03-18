N, L = map(int,input().split())
leaks = list(map(int,input().split()))

leaks.sort()
end = leaks[0] + L

res = 1

for i in range(N):
    if leaks[i] < end:
        continue
    else:
        end = leaks[i] + L
        res += 1


print(res)
