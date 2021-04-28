import sys
import copy


def zero(box2):
    flag = 0
    while flag == 0:
        flag = 1
        for a in range(H - 1, -1, -1):  # 행
            for b in range(W):  # 열
                if box2[a][b] == 0 and box2[a - 1][b] != 0:
                    if a - 1 >= 0:
                        box2[a][b], box2[a - 1][b] = box2[a - 1][b], 0
                        flag = 0


def play(c, r, box2):  # 열 행
    q = [[c, r, box2[r][c]]]
    temp_cnt = 0

    while q:
        x, y, s = q.pop()  # 열, 행, 값
        for k in range(4):  # 4방향 탐색
            for ss in range(s):
                temp_x = x + ss * dx[k]
                temp_y = y + ss * dy[k]

                if 0 <= temp_x < W and 0 <= temp_y < H:
                    if box2[temp_y][temp_x] != 0:
                        q.append([temp_x, temp_y, box2[temp_y][temp_x]])
                        box2[temp_y][temp_x] = 0
                        temp_cnt += 1

    zero(box2)
    return temp_cnt


def comb(n):
    global ans
    if ans == total:
        return

    if n == N:
        box2 = copy.deepcopy(box)
        cnt = 0

        for i in ball:  # 공 던지는 순서, 열
            r = -1
            for j in range(H):  # 행
                if box2[j][i] != 0:
                    r = 0
                    l = j
                    break

            if r == -1:  # 벽돌이 없을 때
                if cnt >= ans:
                    ans = cnt
                return

            cnt += play(i, l, box2)  # 열, 행

        if cnt > ans:
            ans = cnt
    else:
        for i in range(W):
            ball[n] = bal[i]
            comb(n + 1)


for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(H)]
    bal = [_ for _ in range(W)]  # 공이 던져질 수 있는
    ball = [0 for _ in range(N)]  # N회의 공 던지는 순서를 담을 배열
    total = 0
    ans = 0

    for i in range(W):  # 초기 벽돌 수
        for j in range(H):
            if box[j][i] != 0:
                total += 1

    dx = [1, 0, -1, 0]  # 오른쪽부터 시계방향
    dy = [0, 1, 0, -1]
    comb(0)
    print('#{} {}'.format(tc, total - ans))