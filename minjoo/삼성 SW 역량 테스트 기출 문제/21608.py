import sys
input = sys.stdin.readline

n = int(input()) # 교실 크기
board = [[0]*n for _ in range(n)] # 어떤 번호 학생이 앉았는지
check = [[4]*n for _ in range(n)] # 인접한 칸의 개수

# 인접한 칸의 개수 초기화
for i in range(n):
    check[0][i] -= 1
for i in range(1, n):
    check[i][0] -= 1
for i in range(1, n):
    check[i][n-1] -= 1
for i in range(1, n-1):
    check[n-1][i] -= 1
check[0][0] -= 1
check[0][n-1] -= 1
check[n-1][0] -= 1
check[n-1][n-1] -= 1


students = {} # 좋아하는 학생 정보
order = [] # 자리 정하는 학생 순서

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for _ in range(n*n):
    line = list(map(int, input().split()))
    order.append(line[0])
    students[line[0]] = line[1:]

def solution(num): # 자리 선정
    global check, board
    like = students[num] # 좋아하는 학생 번호
    result = []
    for i in range(n):
        for j in range(n):
            if(board[i][j] == 0): # 비어있는 칸 중에서
                cnt = 0
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if(0<=ni<n and 0<=nj<n and board[ni][nj] in like):
                        cnt += 1
                result.append([cnt, i, j])

    result.sort(reverse = True, key = lambda x:x[0]) # 1. 좋아하는 학생이 많은 순대로 정렬
    
    result_2 = []
    if(len(result) > 1 and result[0][0] == result[1][0]): # 2. 1을 만족하는 칸이 여러개이면, 비어있는 칸이 가장 많은 칸으로
        max_cnt = result[0][0]
        cnt2 = 0 # 인접한 칸 최대값
        for i in range(len(result)):
            if(result[i][0] < max_cnt):
                break
            if(cnt2 < check[result[i][1]][result[i][2]]): # 인접한 칸의 최대 개수가 갱신될때
                cnt2 = check[result[i][1]][result[i][2]]
                result_2 = []
                result_2.append([check[result[i][1]][result[i][2]], result[i][1], result[i][2]])
            elif(cnt2 == check[result[i][1]][result[i][2]]): # 인접한 칸의 최대개수와 같을 때
                result_2.append([check[result[i][1]][result[i][2]], result[i][1], result[i][2]])
    else:
        return result[0][1], result[0][2]

    
    result_2.sort(key = lambda x:(x[1], x[2])) # 행, 열 순대로 정렬
    return result_2[0][1], result_2[0][2]

def score(): # 최종 점수 계산
    s = 0
    for i in range(n):
        for j in range(n):
            num = board[i][j]
            like = students[num]
            cnt = 0
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if(0<=ni<n and 0<=nj<n and board[ni][nj] in like):
                    cnt += 1
            if(cnt > 0):
                s += 10 ** (cnt - 1)
    return s
                    

for i in range(len(order)):
    num = order[i] # 현재 자리를 정해야하는 학생 번호
    x, y = solution(num)
    board[x][y] = num
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if(0<=nx<n and 0<=ny<n):
            check[nx][ny] -= 1

print(score())