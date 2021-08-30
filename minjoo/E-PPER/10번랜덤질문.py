board = [list(map(int, input().split())) for _ in range(10)]

cache = [[50 for _ in range(10)] for _ in range(10)]
result = [[2 for _ in range(10)] for _ in range(10)]

# 질문을 맞춘 경우
for i in range(10):
    for j in range(10):
        ret, gap = 0, 0
        for k in range(10):
            # ret 값에 i 열과 i 행의 합 저장
            ret += board[i][k]
            ret += board[k][j]

        gap = ret - board[i][j]
        if(gap % 2 == 1):
            result[i][j] = 3 # board[i][j] 위치의 학생이 질문을 맞춤
            for h in range(10):
                # cache 배열에도 해당 결과 반영
                cache[i][h] += 1
                cache[h][j] += 1

            # 두번 더해진 값이므로 -1
            cache[i][j] -= 1

# 질문을 틀린 경우
for i in range(10):
    for j in range(10):
        ret, gap = 0, 0
        for k in range(10):
            ret += board[i][k]
            ret += board[k][j]
        # 위와 동일한 연산을 수행하여 gap값 도출
        gap = ret - board[i][j]

        ret = 0
        for k in range(10):
            ret += cache[i][k]
            ret += cache[k][j]

        gap2 = ret - cache[i][j]

        gap -= gap2
        if(gap % 4 < 0):
            gap = gap % 4 + 4
        else:
            gap = gap % 4
            
        if(gap == 2):
            result[i][j] = 1

for i in range(10):
    for j in range(10):
        print(result[i][j], end = ' ')
    print()
            
