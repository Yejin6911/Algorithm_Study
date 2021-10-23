dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dir = [2, 1, 3, 0]


def destroy(d, s):
    x, y = shark
    for _ in range(s):
        x += dx[d]
        y += dy[d]
        board[x][y] = 0
    return


def save():
    total = []
    x, y = shark
    d = 0
    for c in range(1, n):
        for i in range(2):
            for _ in range(c):
                x += dx[dir[d]]
                y += dy[dir[d]]
                if board[x][y] != 0:
                    total.append(board[x][y])
            d = (d+1) % 4
    for _ in range(n-1):
        x += dx[dir[d]]
        y += dy[dir[d]]
        if board[x][y] != 0:
            total.append(board[x][y])
    return total


def explode(total):
    while True:
        if not len(total):
            break
        groups = []
        prev = total[0]
        temp = [0]
        for i in range(1, len(total)):
            if total[i] == prev:
                temp.append(i)
            else:
                if len(temp) >= 4:
                    groups.append(temp)
                temp = [i]
                prev = total[i]
        if len(temp) >= 4:
            groups.append(temp)
        if not len(groups):
            break
        for group in groups:
            # 폭발하는 개수 계산
            color = total[group[0]]
            cnt[color-1] += len(group)
            for i in range(len(group)):
                total[group[i]] = 0
        # 구슬 이동\
        idx = 0
        while True:
            if idx == len(total):
                break
            if total[idx] == 0:
                total.pop(idx)
            else:
                idx += 1
    return total


def change(total):
    if not len(total):
        return [0]*(n*n-1)

    # 구슬 변화
    groups = []
    prev = total[0]
    temp = [0]
    for i in range(1, len(total)):
        if total[i] == prev:
            temp.append(i)
        else:
            groups.append(temp)
            temp = [i]
            prev = total[i]
    groups.append(temp)
    new_total = []
    for group in groups:
        a, b = len(group), total[group[0]]
        new_total.extend([a, b])

    # 길거나 짧으면 자르거나 뒷부분에 0 추가
    if len(new_total) > n*n-1:
        new_total = new_total[:n*n-1]
    elif len(new_total) < n*n-1:
        for i in range(len(new_total), n*n-1):
            new_total.append(0)
    return new_total


def update(total):
    # 보드에 다시 적용
    new_board = [[0]*n for _ in range(n)]
    # if not len(total):
    #     return new_board
    d = 0
    x, y = shark
    idx = 0
    for c in range(1, n):
        for i in range(2):
            for _ in range(c):
                x += dx[dir[d]]
                y += dy[dir[d]]
                new_board[x][y] = total[idx]
                idx += 1
            d = (d+1) % 4
        if c == n-1:
            for _ in range(c):
                x += dx[dir[d]]
                y += dy[dir[d]]
                new_board[x][y] = total[idx]
                idx += 1
    return new_board


n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
shark = (n//2, n//2)

steps = [list(map(int, input().rstrip().split())) for _ in range(m)]
cnt = [0, 0, 0]
for step in steps:
    d, s = step
    destroy(d-1, s)
    total = save()
    total = explode(total)
    total = change(total)
    board = update(total)

print(cnt[0]+2*cnt[1]+3*cnt[2])
