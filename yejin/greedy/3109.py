import sys

R, C = map(int, sys.stdin.readline().rstrip().split())

array = []
visited = [[False]*C for _ in range(R)]
array = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

direction = [-1, 0, +1]
cnt = 0


def check(row, col):
    if col == C-1:
        return True

    for d in direction:
        if 0 <= row+d < R and array[row+d][col+1] == '.' and not visited[row+d][col+1]:
            visited[row+d][col+1] = True
            if check(row+d, col+1):
                return True
    return False


for r in range(R):
    if check(r, 0):
        cnt += 1
print(cnt)


# 왜 틀리즌지 모르겠음ㅠㅠㅠ
# for r in range(R):
#     col = 0
#     row = r
#     check = False
#     while True:
#         if col == C-1:
#             cnt += 1
#             break
#         for d in direction:
#             if 0 <= row+d < R and array[row+d][col+1] == '.' and not visited[row+d][col+1]:
#                 visited[row+d][col+1] = True
#                 check = True
#                 row += d
#                 col += 1
#                 break
#         if not check:
#             break
#         check = False
# print(cnt)
