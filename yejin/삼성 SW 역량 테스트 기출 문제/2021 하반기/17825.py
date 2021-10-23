# 틀린 코드...
import copy
from collections import deque
dices = list(map(int, input().rstrip().split()))

board = {
    0: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22,
        24, 26, 28, 30, 32, 34, 36, 38, 40],
    10: [10, 13, 16, 19, 25, 30, 35, 40],
    20: [20, 22, 24, 25, 30, 35, 40],
    30: [30, 28, 27, 26, 25, 30, 35, 40],
    25: [25, 30, 35, 40]
}


# position 원소: [key, index]
def dfs(position, total, finish, d):
    if d == 10:
        global answer
        answer = max(total, answer)
        return
    for i in range(len(position)):
        # 도착하는 경우
        if position[i][1] + dices[d] >= len(board[position[i][0]]):
            new_position = copy.deepcopy(position)
            new_position.pop(i)
            dfs(new_position, total, finish+1, d+1)
        else:
            new = [position[i][0], position[i][1] + dices[d]]
            # 파란색 칸일 때 처리
            if new[0] == 0 and new[1] in (5, 10, 15):
                new[0] = board[new[0]][new[1]]
                new[1] = 0
            # 40위치에 있을 때 처리(통일 시켜주기)
            elif board[new[0]][new[1]] == 40:
                new = [25, 3]
            # 25위치에 있을 때 처리(통일 시켜주기)
            elif board[new[0]][new[1]] == 25:
                new = [25, 0]
            # 해당 위치에 말이 없는 경우
            if new not in position:
                new_position = copy.deepcopy(position)
                new_position[i] = new
                dfs(new_position, total + board[new[0]][new[1]], finish, d+1)
    # 아직 놓지 않은 말이 있는 경우
    if finish+len(position) < 4:
        if dices[d] == 5:
            new = [10, 0]
        else:
            new = [0, dices[d]]
        if new not in position:
            new_position = copy.deepcopy(position)
            new_position.append(new)
            dfs(new_position, total + board[new[0]][new[1]], finish, d+1)


global answer
answer = 0
dfs([], 0, 0, 0)
print(answer)
