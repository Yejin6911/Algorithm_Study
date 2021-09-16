from collections import deque


def find(r1, r2, new_board):
    candidates = []
    # 평행이동
    DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dy, dx in DELTAS:
        nxt1 = (r1[0] + dy, r1[1] + dx)
        nxt2 = (r2[0] + dy, r2[1] + dx)
        if new_board[nxt1[0]][nxt1[1]] == 0 and new_board[nxt2[0]][nxt2[1]] == 0:
            candidates.append((nxt1, nxt2))
    # 회전
    if r1[0] == r2[0]:  # 가로방향 일 때
        for d in [-1, 1]:
            if new_board[r1[0]+d][r1[1]] == 0 and new_board[r2[0]+d][r2[1]] == 0:
                candidates.append((r1, (r1[0]+d, r1[1])))
                candidates.append((r2, (r2[0]+d, r2[1])))
    else:  # 세로 방향 일 때
        for d in [-1, 1]:
            if new_board[r1[0]][r1[1]+d] == 0 and new_board[r2[0]][r2[1]+d] == 0:
                candidates.append(((r1[0], r1[1]+d), r1))
                candidates.append(((r2[0], r2[1]+d), r2))

    return candidates


def solution(board):
    # board 외벽 둘러싸기
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    # 현재 좌표 위치 큐 삽입, 확인용 set
    que = deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])

    while que:
        r1, r2, cnt = que.popleft()
        if r1 == (n, n) or r2 == (n, n):
            return cnt
        for next in find(r1, r2, new_board):
            if next not in confirm:
                que.append((*next, cnt+1))
                confirm.add(next)
