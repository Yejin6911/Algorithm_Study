import sys
input = sys.stdin.readline


def divide(x, y):
    diff = sys.maxsize
    for d1 in range(1, y):
        for d2 in range(1, n-y):
            total = [0, 0, 0, 0, 0]
            if x+d1+d2 >= n:
                break
            board = [[0]*n for _ in range(n)]
            boundary = []
            # 경계선 표시
            for i in range(d1+1):
                board[x+i][y-i] = 5
                board[x+d2+i][y+d2-i] = 5
                boundary.append((x+i, y-i))
                boundary.append((x+d2+i, y+d2-i))
            for i in range(d2+1):
                board[x+i][y+i] = 5
                board[x+d1+i][y-d1+i] = 5
                boundary.append((x+i, y+i))
                boundary.append((x+d1+i, y-d1+i))
            # 중복 제거 후 행 순서대로 정렬
            boundary = sorted(list(set(boundary)))
            start = 1
            # 5번 선거구 표시
            while start < len(boundary)-1:
                for i in range(boundary[start][1]+1, boundary[start+1][1]):
                    board[boundary[start][0]][i] = 5
                start += 2
            for r in range(n):
                for c in range(n):
                    # 5번 선거구
                    if board[r][c] == 5:
                        total[4] += A[r][c]
                    else:
                        # 1번 선거구
                        if 0 <= r < x+d1 and 0 <= c <= y:
                            board[r][c] = 1
                            total[0] += A[r][c]
                        # 2번 선거구
                        elif 0 <= r <= x+d2 and y < c < n:
                            board[r][c] = 2
                            total[1] += A[r][c]
                        # 3번 선거구
                        elif x+d1 <= r < n and 0 <= c < y-d1+d2:
                            board[r][c] = 3
                            total[2] += A[r][c]
                        # 4번 선거구
                        elif x+d2 < r < n and y-d1+d2 <= c < n:
                            board[r][c] = 4
                            total[3] += A[r][c]
            if max(total)-min(total) < diff:
                diff = max(total)-min(total)
    return diff


n = int(input().rstrip())
A = [list(map(int, input().rstrip().split())) for _ in range(n)]

result = sys.maxsize
for x in range(n):
    for y in range(1, n):
        diff = divide(x, y)
        if diff <= result:
            result = diff
print(result)
