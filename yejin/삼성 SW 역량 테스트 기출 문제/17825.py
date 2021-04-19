import sys
input = sys.stdin.readline


def score():
    global result
    # 말들의 현재 위치
    now = [[0, 0] for i in range(5)]
    num = 0
    # 주사위 순서 반복
    for i in range(1, 11):
        pi = piece[i]
        x, y = now[pi]
        # 이미 도착한 말인 경우
        if x == -1:
            return
        else:
            # 새로운 좌표
            y += data[i]
            if x == 0:
                # 도착
                if 20 < y:
                    now[pi] = [-1, -1]
                # 10
                elif y == 5:
                    now[pi] = [1, 0]
                # 20
                elif y == 10:
                    now[pi] = [3, 0]
                # 30
                elif y == 15:
                    now[pi] = [2, 0]
                # 40
                else:
                    now[pi] = [x, y]
            elif x == 1:
                # 도착
                if y >= 8:
                    now[pi] = [-1, -1]
                elif y >= 4:
                    # 25 이전까지의 개수가 1개 차이나므로 1 빼준다
                    now[pi] = [3, y - 1]
                else:
                    now[pi] = [x, y]
            elif x == 2:
                if y >= 8:
                    now[pi] = [-1, -1]
                elif y >= 4:
                    now[pi] = [3, y - 1]
                else:
                    now[pi] = [x, y]
            elif x == 3:
                if y > 6:
                    now[pi] = [-1, -1]
                else:
                    now[pi] = [x, y]
            # 새로운 위치
            nx, ny = now[pi]
            # 도착하지 않았을 경우
            if nx != -1:
                for k in range(1, 5):
                    if pi == k:
                        continue
                    a, b = now[k]
                    if a == -1:
                        continue
                    # 해당위치에 이미 말이 있으면 return
                    if position[a][b] == position[nx][ny]:
                        return
                # 합계 update
                num += board[nx][ny]
    result = max(result, num)


def dfs():
    global depth
    if depth == 10:
        score()
        return
    for i in range(1, 5):
        depth += 1
        piece[depth] = i
        dfs()
        depth -= 1


# 이동할 말 리스트
piece = [0 for i in range(11)]

# 판 숫자 정보
board = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
         [10, 13, 16, 19], [30, 28, 27, 26], [20, 22, 24, 25, 30, 35, 40]]
# 위치 정보
position = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [5, 21, 22, 23], [15, 24, 25, 26], [10, 27, 28, 29, 30, 31, 20]]

# 주사위 나올 수
data = [0] + list(map(int, input().split()))
result = 0
depth = 0
dfs()
print(result)
