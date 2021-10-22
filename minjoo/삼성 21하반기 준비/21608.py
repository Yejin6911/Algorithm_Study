import sys
from math import pow
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
data = {}
for i in range(n*n):
    arr = list(map(int, input().split()))
    data[arr[0]] = arr[1:]

sequence = list(data.keys())

def check(num): # 학생 번호

    like = data[num]
    candi = []
    for i in range(n):
        for j in range(n):
            if(board[i][j] == 0): # 비어있는 칸
                temp = [0, 0, i, j]
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if(0<=nx<n and 0<=ny<n):
                        if(board[nx][ny] in like):
                            temp[0] -= 1
                        elif(board[nx][ny] == 0):
                            temp[1] -= 1
                candi.append(temp)
    candi.sort(key = lambda x:(x[0], x[1], x[2], x[3]))
    return candi[0][2], candi[0][3]

for i in range(n*n):
    num = sequence[i]
    x, y = check(num)
    board[x][y] = num

score = 0
for i in range(n):
    for j in range(n):
        like = data[board[i][j]]
        cnt = 0
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if(0<=nx<n and 0<=ny<n and board[nx][ny] in like):
                cnt += 1
        score += int(pow(10, cnt-1))
print(score)