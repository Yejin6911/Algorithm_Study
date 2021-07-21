import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10*6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# record를 리스트로 처리하니 시간초과 나서 문자열로 바꿔서 처리
def dfs(x, y, record):
    global result
    check = False
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in record:
            dfs(nx, ny, record+board[nx][ny])
    if not check:
        result = max(result, len(record))
        return


r, c = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(r)]
result = 0
dfs(0, 0, board[0][0])

print(result)
