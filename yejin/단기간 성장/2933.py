from collections import deque
from sys import stdin
input = stdin.readline

# https://chelseashin.tistory.com/88

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 땅에 붙어있는 미네랄 체크
def check():
    visited = [[0] * C for _ in range(R)]
    for ly in range(C):
        # 미네랄이면서 첫 방문
        if cave[R-1][ly] == "x" and not visited[R-1][ly]:
            visited[R-1][ly] = 1
            queue = deque([(R-1, ly)])
            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 미네랄이거나 방문한 적 없으면
                    if (0 <= nx < R and 0 <= ny < C) and cave[nx][ny] == "x" and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
    return visited


# 떨어질 칸의 수 계산 함수
def countMove(fallLst, visited):
    cnt, flag = 1, 0
    while True:
        for x, y in fallLst:
            # 땅을 만나는 경우
            if x+cnt == R-1:
                flag = 1
                break
            if cave[x+cnt+1][y] == 'x' and visited[x+cnt+1][y]:   # 다른 미네랄 만나면
                flag = 1
                break
        # 떨어질 수 있는 최대 cnt 값
        if flag:
            break
        cnt += 1
    return cnt


def update(bx, by):
    # 땅에 붙어 있는 미네랄 1로 표시
    visited = check()

    # 공중에 떠있는 미네랄 2로 표시, 동굴에서 지우기
    minerals = []    # 공중에 떠있는 미네랄 리스트
    fallLst = []     # 공중에 있는 클러스터의 아랫부분
    for nd in range(4):
        x = bx + dx[nd]
        y = by + dy[nd]

        # 미네랄인데 땅에 붙어 있지 않다면 2로 표시
        if (0 <= x < R and 0 <= y < C) and cave[x][y] == "x" and not visited[x][y]:
            queue = deque([(x, y)])
            visited[x][y] = 2
            minerals.append((x, y))
            cave[x][y] = "."
            while queue:
                x, y = queue.popleft()
                if cave[x+1][y] == ".":     # 바로 밑이 빈 공간인 미네랄
                    fallLst.append((x, y))
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if not (0 <= nx < R and 0 <= ny < C):
                        continue
                    if cave[nx][ny] == "x" and not visited[nx][ny]:
                        visited[nx][ny] = 2           # 공중에 떠있는 미네랄
                        queue.append((nx, ny))
                        minerals.append((nx, ny))
                        cave[nx][ny] = "."

    if fallLst:    # 공중에 떠있는 미네랄이 있다면
        # 떨어질 최대 칸의 수
        downCnt = countMove(fallLst, visited)

        # 미네랄 떨어질 위치로 update
        for mx, my in minerals:
            cave[mx+downCnt][my] = "x"


R, C = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().split()))

for i in range(N):
    bx = R - heights[i]
    if not i % 2:  # 왼쪽
        for by in range(C):
            if cave[bx][by] == "x":
                cave[bx][by] = "."
                update(bx, by)   # 깨진 위치 인자로 넘겨 미네랄 깨기
                break
    else:  # 오른쪽
        for by in range(C-1, -1, -1):
            if cave[bx][by] == "x":
                cave[bx][by] = "."
                update(bx, by)
                break

# 형식에 맞게 출력
for row in cave:
    print(''.join(row))
