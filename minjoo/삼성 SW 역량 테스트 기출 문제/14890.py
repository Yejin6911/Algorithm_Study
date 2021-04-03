import sys

input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def changeboard(board):
    tempboard = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tempboard[j][i] = board[i][j]
    return tempboard

def check(board):
    global N, L
    result = 0

    for i in range(N):
        cnt = 1 # 연속되는 칸
        pre = board[i][0] # 첫 칸
        nope = 0
        caution = 0
        for j in range(1, N):
            if(caution != 0):
                if(pre == board[i][j]):
                    caution -= 1
                    if(caution == 0):
                        cnt = 0
                        continue
                else:
                    nope = 1
                    break # 경사로 놓을 수 없음

            if(pre == board[i][j]):
                cnt += 1

            elif((pre - board[i][j]) == 1): # 내려가는
                if(L-1 > 0):
                    caution = L-1
                    pre = board[i][j]
                else:
                    cnt = 0 # 연속되는 칸 초기화
                    pre = board[i][j]

            elif((board[i][j] - pre) == 1): # 올라가는
                if(cnt < L):
                    nope = 1
                    break
                else:
                    cnt = 1
                    pre = board[i][j]

            else: # 두계단 이상 차이날 때
                nope = 1
                break
        
        if(j==N-1 and nope != 1 and caution == 0):
            result += 1
    return result

ans= check(board)
ans2= check(changeboard(board))
print(ans + ans2)
