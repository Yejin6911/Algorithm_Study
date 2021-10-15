import sys
input = sys.stdin.readline


def divide(x, y, d1, d2):
    check = [[0]*(n+1) for _ in range(n+1)]
    for i in range(d1+1):
        if 0 < x+i <= n and 0 < y-i <= n:
            check[x+i][y-i] = 5
        if 0 < x+d2+i <= n and 0 < y+d2-i <= n:
            check[x+d2+i][y+d2-i] = 5
    for i in range(1, d2+1):
        if 0 < x+i <= n and 0 < y+i <= n:
            check[x+i][y+i] = 5
        if 0 < x+d1+i <= n and 0 < y-d1+i <= n:
            check[x+d1+i][y-d1+i] = 5
    # 5번 선거구 안쪽 채우기
    for i in range(x+1, x+d1+d2):
        j = y-d1
        while j <= n:
            if check[i][j] == 5:
                j += 1
                while j <= n and check[i][j] != 5:
                    check[i][j] = 5
                    j += 1
                break
            j += 1
    # 1번 선거구
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if not check[r][c]:
                check[r][c] = 1
    # 2번 선거구
    for r in range(1, x+d2+1):
        for c in range(y+1, n+1):
            if not check[r][c]:
                check[r][c] = 2
    # 3번 선거구
    for r in range(x+d1, n+1):
        for c in range(1, y-d1+d2):
            if not check[r][c]:
                check[r][c] = 3
    # 4번 선거구
    for r in range(x+d2+1, n+1):
        for c in range(y-d1+d2, n+1):
            if not check[r][c]:
                check[r][c] = 4
    return check


n = int(input())
board = [[0]*(n+1) for _ in range(n+1)]
answer = sys.maxsize
for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(n):
        board[i][j+1] = row[j]

for x in range(2, n+1):
    for y in range(2, n+1):
        for d1 in range(1, y):
            for d2 in range(1, n-y+1):
                if (1 <= x < x+d1+d2 <= n and 1 <= y-d1 < y < y+d2 <= n):
                    check = divide(x, y, d1, d2)
                    cnt = [0]*5
                    for i in range(1, n+1):
                        for j in range(1, n+1):
                            cnt[check[i][j]-1] += board[i][j]
                    answer = min(answer, max(cnt)-min(cnt))
print(answer)
