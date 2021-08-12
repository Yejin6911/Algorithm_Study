import sys
input = sys.stdin.readline

n, k = map(int, input().split())
item = [[0, 0]]
for i in range(1, n+1):
    item.append(list(map(int, input().split())))
dp = [[0]*(k+1) for _ in range(n+1)] # (n+1) x (k+1) 배열

for i in range(1, n+1):
    for j in range(1, k+1):
        w = item[i][0]
        v = item[i][1]

        # 배낭의 허용 무게(j)보다 넣을 물건의 무게(w)가 더 크면 넣지 않는다.
        if(j < w): 
            dp[i][j] = dp[i-1][j]

        # 이전 배낭의 가치와
        # 현재 넣을 물건의 무게만큼 배낭에서 빼고 현재 물건을 넣은 가치 중 더 큰 값을 선택
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])