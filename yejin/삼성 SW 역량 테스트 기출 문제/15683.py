import sys
import copy
input = sys.stdin.readline

# 동->서->남->북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 감시 가능한 곳 찾아 개수 return
def move(x, y, d):
    cnt = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or office[nx][ny] == 6:
            return cnt
        if visited[nx][ny] in [1, 2, 3, 4, 5] or visited[nx][ny] == '#':
            x, y = nx, ny
            continue
        visited[nx][ny] = '#'
        cnt += 1
        x, y = nx, ny
    return cnt


def dfs(dir):
    global visited
    global result
    # cctv 방향 다 정해진 경우
    if len(dir) == len(cctv):
        visited = copy.deepcopy(office)
        cnt = 0
        for i in range(len(cctv)):
            x = cctv[i][0]
            y = cctv[i][1]
            kind = cctv[i][2]
            if kind == 1:
                cnt += move(x, y, dir[i])
            elif kind == 2:
                cnt += move(x, y, dir[i])
                cnt += move(x, y, (dir[i]+2) % 4)
            elif kind == 3:
                cnt += move(x, y, dir[i])
                cnt += move(x, y, (dir[i] + 1) % 4)
            elif kind == 4:
                cnt += move(x, y, dir[i])
                cnt += move(x, y, (dir[i] + 1) % 4)
                cnt += move(x, y, (dir[i] + 2) % 4)
        result = min(result, area-cnt)
        return
    for i in range(4):
        dfs(dir+[i])


n, m = map(int, input().rstrip().split())
office = []
cctv = []
cctv_5 = []
area = n*m

for i in range(n):
    row = list(map(int, input().rstrip().split()))
    office.append(row)
    for j in range(len(row)):
        if row[j] != 0:
            area -= 1
            if row[j] != 6:
                if row[j] == 5:
                    cctv_5.append((i, j))
                else:
                    cctv.append((i, j, row[j]))
# 1. 5번 카메라 처리
for c in cctv_5:
    x = c[0]
    y = c[1]
    for i in range(4):
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or office[nx][ny] == 6:
                break
            if office[nx][ny] == 0:
                office[nx][ny] = '#'
                area -= 1

result = area
dfs([])
print(result)
