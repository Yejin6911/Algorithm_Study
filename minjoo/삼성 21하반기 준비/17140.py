import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

sec = 0

def rotation(board, r_count, c_count):
    temp = [[0 for _ in range(r_count)] for _ in range(c_count)]
    for i in range(c_count):
        for j in range(r_count):
            temp[i][j] = board[r_count-1-j][i]
    return temp

def rotation2(board, r_count, c_count):
    temp = [[0 for _ in range(r_count)] for _ in range(c_count)]
    for i in range(r_count):
        for j in range(c_count):
            temp[j][i] = board[i][j]
    return temp

def arrange(arr):
    nums = list(set(arr))
    cnt = []
    if(0 in nums):
        nums.remove(0)
    for i in range(len(nums)):
        cnt.append([nums[i], arr.count(nums[i])])

    cnt.sort(key = lambda x:(x[1], x[0]))
    res = []
    for i  in range(len(cnt)):
        res.append(cnt[i][0])
        res.append(cnt[i][1])
    return res

def padding(board):
    if(len(board) > 100):
        board = board[:100] # 행 정리

    max_count = 0
    for i in range(len(board)):
        max_count = max(len(board[i]), max_count)
    if(max_count > 100):
        max_count = 100

    for i in range(len(board)):
        if(len(board[i]) < max_count):
            for _ in range(max_count - len(board[i])):
                board[i].append(0)
        elif(len(board[i]) > 100):
            board[i] = board[i][:100]
    return board
    
while(1):
    r_count = len(board) # 행의 개수
    c_count = len(board[0]) # 열의 개수

    if(r_count > r-1 and c_count > c-1):
        if(board[r-1][c-1] == k):
            print(sec)
            break
    if(sec == 100):
        print(-1)
        break
    
    if(r_count >= c_count): # R연산
        for i in range(r_count):
            board[i] = arrange(board[i])
        board = padding(board)

    else: # C연산
        temp = rotation(board, r_count, c_count)
        for i in range(c_count):
            temp[i] = arrange(temp[i])
        temp = padding(temp)
        rc = len(temp)
        cc = len(temp[0])
        board = rotation2(temp, rc, cc)


    sec += 1