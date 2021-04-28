import sys
input = sys.stdin.readline

n = int(input()) # 재현시의 크기
board = [[0]*(n+1)]
for i in range(n):
    line = list(map(int, input().split()))
    line.insert(0, 0)
    board.append(line)

# print(board)
def solution(x, y, d1, d2):
    global n, board
    check = [[0]*(n+1) for _ in range(n+1)]
    nums = [0, 0, 0, 0, 0, 0] # 1, 2, 3, 4, 5번 지역구

    # 5번 지역구
    for i in range(d1+1):
        check[x+i][y-i] = 5
        check[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        check[x+i][y+i] = 5
        check[x+d1+i][y-d1+i] = 5

    for i in range(x+1, x+d1+d2):
        flag = 0
        for j in range(n):
            if(flag == 1 and check[i][j] != 5):
                check[i][j] = 5
            elif(flag == 0 and check[i][j] == 5):
                flag = 1
            elif(flag == 1 and check[i][j] == 5):
                break


    # print(check)
    # 1번 지역구
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if (r < x + d1 and c <= y and check[r][c] == 0):
                nums[1] += board[r][c]
            elif (r <= x + d2 and y < c and check[r][c] == 0):
                nums[2] += board[r][c]
            elif (x + d1 <= r and c < y - d1 + d2 and check[r][c] == 0):
                nums[3] += board[r][c]
            elif (x + d2 < r and y - d1 + d2 <= c and check[r][c] == 0):
                nums[4] += board[r][c]
            else:
                nums[5] += board[r][c]


    max_p = max(nums[1:])
    min_p = min(nums[1:])
    # print(nums)

    return max_p - min_p

min_result = sys.maxsize
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if(1 <= x < x+d1+d2 <= n and 1 <= y-d1 < y < y+d2 <= n):
                    min_result = min(solution(x, y, d1, d2), min_result)

print(min_result)

