# https://bladejun.tistory.com/130 풀이 참고
from collections import deque
from itertools import permutations
import sys
import copy


def ctrl_move(x, y, d):
    global board_c
    while True:
        nx = x + d[0]
        ny = y + d[1]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            return x, y

        else:
            if board_c[nx][ny] != 0:
                return nx, ny
            x, y = nx, ny


def bfs(sx, sy, ex, ey):
    global board_c
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if sx == ex and sy == ey:
        return 1

    q = deque([[sx, sy]])
    cnt = [[0]*4 for _ in range(4)]
    visited = [[0]*4 for _ in range(4)]
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()
        # 방향키
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
                cnt[nx][ny] = cnt[x][y] + 1
                visited[nx][ny] = 1
                if nx == ex and ny == ey:
                    return cnt[nx][ny] + 1  # enter(+1)
                q.append([nx, ny])
            # 컨트롤+방향키
            nx, ny = ctrl_move(x, y, [dx[i], dy[i]])
            if not visited[nx][ny]:
                cnt[nx][ny] = cnt[x][y] + 1
                visited[nx][ny] = 1
                if nx == ex and ny == ey:
                    return cnt[nx][ny] + 1  # enter(+1)
                q.append([nx, ny])


def remove_card(card):
    global board_c, card_position
    for x, y in card_position[card]:
        board_c[x][y] = 0


def restore_card(card):
    global board_c, card_position
    for x, y in card_position[card]:
        board_c[x][y] = card


def go(sx, sy, order, card_num, count, move):
    global answer, order_p, card_position, board_c
    # 짝을 다 맞춘 경우
    if count == card_num:
        answer = min(answer, move)
        return

    card = order_p[order][count]

    # 두개 카드 각각의 위치
    first = card_position[card][0]
    second = card_position[card][1]

    d1 = bfs(sx, sy, first[0], first[1])             # 출발 지점 -> 첫번째 카드
    d2 = bfs(first[0], first[1], second[0], second[1])  # 첫번째 카드 -> 두번째 카드
    remove_card(card)
    go(second[0], second[1], order, card_num, count+1, move+d1+d2)
    # 백트래킹
    restore_card(card)

    d1 = bfs(sx, sy, second[0], second[1])           # 출발 지점 -> 두번째 카드
    d2 = bfs(second[0], second[1], first[0], first[1])  # 두번째 카드 -> 첫번째 카드

    remove_card(card)
    go(first[0], first[1], order, card_num, count+1, move+d1+d2)
    # 백트래킹
    restore_card(card)


def solution(board, r, c):
    global answer, order_p, card_position, board_c

    answer = sys.maxsize
    board_c = copy.deepcopy(board)

    # 카드 숫자 별 위치 저장
    card_position = {}
    for i in range(4):
        for j in range(4):
            num = board[i][j]
            if num != 0:
                if num in card_position.keys():
                    card_position[num].append([i, j])
                else:
                    card_position[num] = [[i, j]]
    # 맞춰야 할 카드 숫자
    orders = [k for k, v in card_position.items()]
    # 맞출 순서 모든 경우의 수
    order_p = list(permutations(orders, len(orders)))  # 제거 순서

    for i in range(len(order_p)):
        go(r, c, i, len(card_position.keys()), 0, 0)

    return answer


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
