def dfs(queens, row):
    cnt = 0
    if n == row:
        return 1

    for col in range(n):
        queens[row] = col
        if check(queens, row):
            cnt += dfs(queens, row+1)
    return cnt


def check(queens, row):
    # 놓을 수 없는 위치인 경우
    if (row, queens[row]) in data:
        return False
    for i in range(row):
        # 같은 열또는 대각선인지 확인
        if queens[i] == queens[row] or abs(queens[i]-queens[row]) == (row-i):
            return False
    return True


n = int(input())
k = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
data = []
for i in range(k):
    data.append((x[i]-1, y[i]-1))

# 각 행 별 퀸이 위치하는 열의 정보 저장
queens = [0]*n
result = dfs(queens, 0)
print(result)
