dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 놓을 수 있는 위치 반환
def find(like):
    candidates = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                blank = 0
                friend = 0
                for i in range(4):
                    nx = x+dir[i][0]
                    ny = y+dir[i][1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 0:
                            blank += 1
                        elif board[nx][ny] in like:
                            friend += 1
                candidates.append((x, y, friend, blank))
    if len(candidates) > 1:
        candidates.sort(key=lambda x: (-x[2], -x[3]))
    return candidates

# 인접한 좋아하는 학생수


def count(x, y, like):
    cnt = 0
    for i in range(4):
        nx = x+dir[i][0]
        ny = y+dir[i][1]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in like:
            cnt += 1
    return cnt


n = int(input())
students = {}
for _ in range(n**2):
    data = list(map(int, input().split()))
    students[data[0]] = data[1:]


board = [[0]*n for _ in range(n)]
for s in students.keys():
    like = students[s]
    candidates = find(like)
    x, y = candidates[0][0], candidates[0][1]
    board[x][y] = s

total = 0
for x in range(n):
    for y in range(n):
        s = board[x][y]
        like = students[s]
        cnt = count(x, y, like)
        if cnt != 0:
            total += (10**(cnt-1))

print(total)
