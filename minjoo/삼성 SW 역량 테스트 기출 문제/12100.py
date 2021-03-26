import sys
import copy

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
cnt = 0

def convert(board):
    temp_board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp_board[j][i] = board[i][j]
    return temp_board

def righttoleft():
    temp_board = copy.deepcopy(board)
    max_seq = []
    for i in range(n):
        temp = 0
        skip = 0
        for j in range(n-1):
            if(skip == 1):
                skip = 0
                continue
            if(temp_board[i][j] == temp_board[i][j+1]):
                temp += 1
                temp_board[i][j] *= 2
                temp_board[i].pop(j+1)
                temp_board[i].append(0)
                skip = 1
        max_seq.append(temp)
    return max_seq, temp_board

def lefttoright():
    temp_board = copy.deepcopy(board)
    max_seq = []
    for i in range(n):
        temp = 0
        skip = 0
        for j in range(n-2, -1, -1):
            if(skip == 1):
                skip = 0
                continue
            if(temp_board[i][j+1] == temp_board[i][j]):
                temp += 1
                temp_board[i][j+1] *= 2
                temp_board[i].pop(j)
                temp_board[i].insert(0, 0)
                skip = 1
        max_seq.append(temp)
    return max_seq, temp_board

def downtoup():
    temp_board = convert(board)
    max_seq = []
    for i in range(n):
        temp = 0
        skip = 0
        for j in range(n-1):
            if(skip == 1):
                skip = 0
                continue
            if(temp_board[i][j] == temp_board[i][j+1]):
                temp += 1
                temp_board[i][j] *= 2
                temp_board[i].pop(j+1)
                temp_board[i].append(0)
                skip = 1
        max_seq.append(temp)
    temp_board = convert(temp_board)
    return max_seq, temp_board

def uptodown():
    temp_board = convert(board)
    max_seq = []
    for i in range(n):
        temp = 0
        skip = 0
        for j in range(n-2, -1, -1):
            if(skip == 1):
                skip = 0
                continue
            if(temp_board[i][j+1] == temp_board[i][j]):
                temp += 1
                temp_board[i][j+1] *= 2
                temp_board[i].pop(j)
                temp_board[i].insert(0, 0)
                skip = 1
        max_seq.append(temp)
    temp_board = convert(temp_board)
    return max_seq, temp_board

while(cnt < 5):
    result = []
    count, x = righttoleft()
    result.append([sum(count), x])
    count, x = lefttoright()
    result.append([sum(count), x])
    count, x = downtoup()
    result.append([sum(count), x])
    count, x = uptodown()
    result.append([sum(count), x])
    
    result.sort(key = lambda x:x[0],reverse=True)
    board = result[0][1]
    cnt += 1

maxnum = max(map(max, board))
print(maxnum)
