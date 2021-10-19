n, k = map(int, input().split())
board = [0 for _ in range(n*2)]
A = list(map(int, input().split()))

step = 1
robot = 1
while True:
    board = [board.pop()]+board
    A = [A.pop()]+A
    if board[n-1]:
        board[n-1] = 0

    # 로봇 이동
    for i in range(n-2, -1, -1):
        if board[i] != 0 and board[i+1] == 0 and A[i+1] >= 1:
            board[i], board[i+1] = 0, board[i]
            A[i+1] -= 1

    if board[n-1]:
        board[n-1] = 0

    if A[0] > 0:
        # 로봇 올리기
        board[0] = robot
        robot += 1
        A[0] -= 1

    if A.count(0) >= k:
        print(step)
        break
    step += 1
