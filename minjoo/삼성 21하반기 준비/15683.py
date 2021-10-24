import sys
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
cctv = []
board = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if(line[j] != 0 and line[j] != 6):
            cctv.append([line[j], i, j]) # cctv번호, 좌표
    board.append(line)

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] #서동북남
direction = [0,[[0],[1],[2],[3]],[[0,1],[2,3]],[[1,2],[1,3],[0,2],[0,3]],[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],[[0,1,2,3]]]

min_result = sys.maxsize
def dfs(tempboard, cnt):
    global cctv, min_result
    # cctv 처리 다 했으면 0 개수 세서 최소값 갱신
    if(cnt == len(cctv)):
        result = 0
        for line in tempboard:
            result += line.count(0)
        min_result = min(min_result, result)
        return

    num, x, y = cctv[cnt]
    for di in direction[num]: # [[0, 2], [1, 3]]의 [0, 2]
        temp = deepcopy(tempboard)
        for idx in di:
            nx = x + dx[idx]
            ny = y + dy[idx]
            while(0<=nx<n and 0<=ny<m):
                if(temp[nx][ny] == 6):
                    break
                elif(temp[nx][ny] == 0):
                    temp[nx][ny] = '#'
                nx += dx[idx]
                ny += dy[idx]

        dfs(temp, cnt+1)

dfs(board, 0)
print(min_result)