import sys
input = sys.stdin.readline

n, length = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def check(arr):
    cnt = 0
    cnt2 = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if(i == 0):
            h = arr[i]
            cnt2 += 1
            continue
        
        # 내려가는 경사로 확인
        if(cnt > 0):
            if(arr[i] == h and visited[i] == 0):
                h = arr[i]
                visited[i] = 1
                cnt -= 1
                cnt2 = 0
                continue
            else:
                return 0

        # 이전 칸이랑 같은 높이인 경우
        if(h == arr[i]):
            cnt2 += 1

        else:
            # 1 낮아지는 경우 + 경사로 아직 없는 경우
            if((h - arr[i]) == 1 and visited[i] == 0):
                cnt = length - 1
                h = arr[i]
                visited[i] = 1
                cnt2 = 1

            # 1 높아지는 경우
            elif((arr[i] - h) == 1 and visited[i-1] == 0):
                # 1작은 높이의 칸 개수가 length개 이상인 경우
                if(cnt2 >= length):
                    h = arr[i]
                    cnt2 = 1
                else:
                    return 0
            # 높이 차이가 1 이상인 경우
            else:
                return 0
    if(cnt):
        return 0

    return 1

# 90도 회전
def rotate(board):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n-i-1] = board[i][j]
    return temp

ans = 0
for i in range(n):
    ans += check(board[i])
    
temp = rotate(board)
for i in range(n):
    ans += check(temp[i])

print(ans)