n = int(input())
a = list(map(int, input().split()))

cnt = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if(a[i] > a[j]):
            cnt[i] = max(cnt[j] + 1, cnt[i])
print(max(cnt))

