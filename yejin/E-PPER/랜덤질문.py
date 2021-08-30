board = [list(map(int, input().split())) for _ in range(10)]
cache = [[50]*10 for _ in range(10)]
result = [[2]*10 for _ in range(10)]


# (i,j)가 질문을 맞췄을 떄
for i in range(10):
    for j in range(10):
        total = 0
        for k in range(10):
            total += (board[i][k]+board[k][j])
        total -= board[i][j]
        if total % 2:
            result[i][j] = 3
            for k in range(10):
                cache[i][k] += 1
                cache[k][j] += 1
            cache[i][j] -= 1

# 틀린 경우
for i in range(10):
    for j in range(10):
        total = 0
        for k in range(10):
            total += (board[i][k]+board[k][j])
        total -= board[i][j]

        cache_total = 0
        for k in range(10):
            cache_total += (cache[i][k]+cache[k][j])
        cache_total -= cache[i][j]
        # (i,j)가 정답을 틀린거였는데 맞춘걸로 cache에 반영한 경우
        # n*n 보드에서 total과 cache값의 차이는 2*(2n-1) => 4로 나눈 나머지가 2
        if (total-cache_total) % 4 == 2:
            result[i][j] = 1

for row in result:
    print(*row)
