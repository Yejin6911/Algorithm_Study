import sys
import copy


def move(board, d):
    # 상
    if d == 0:
        for j in range(N):
            idx = 0
            for i in range(1, N):
                # 해당 칸에 블록이 있는 경우
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    # 앞 칸이 비어있으므로 옮겨준다.
                    if board[idx][j] == 0:
                        board[idx][j] = temp
                    # 앞칸이랑 블록 숫자 같은 경우
                    elif board[idx][j] == temp:
                        board[idx][j] = temp * 2
                        idx += 1
                    # 숫자 다른 경우
                    else:
                        idx += 1
                        board[idx][j] = temp
    # 하
    elif d == 1:
        for j in range(N):
            idx = N-1
            for i in range(N - 2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[idx][j] == 0:
                        board[idx][j] = temp
                    elif board[idx][j] == temp:
                        board[idx][j] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[idx][j] = temp
    # 좌
    elif d == 2:
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = temp
                    elif board[i][idx] == temp:
                        board[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[i][idx] = temp
    # 우
    else:
        for i in range(N):
            idx = N-1
            for j in range(N - 2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = temp
                    elif board[i][idx] == temp:
                        board[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[i][idx] = temp


def dfs(board, cnt):
    global result
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                result = max(result, board[i][j])
        return

    # 이부분 주의! 방향별로 움직인다음 다음 방향을 적용하기 위해서는 보드 원상복귀 시켜야 하므로 미리 복사해놓는다.
    temp_board = copy.deepcopy(board)
    for i in range(4):
        move(board, i)
        dfs(board, cnt + 1)
        # 보드 초기화
        board = copy.deepcopy(temp_board)


N = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().rstrip().split()))
         for _ in range(N)]
result = 0
dfs(board, 0)
print(result)
