# PyPy3제출
import sys
import copy
input = sys.stdin.readline


# i->i인지 체크
def check():
    for i in range(n):
        start = i
        height = 0
        check = False
        while True:
            # 이동할 가로선이 없는 경우
            if height == h:
                if start == i:
                    check = True
                    break
                else:
                    break
            else:
                # 오른쪽 가로선 있는 경우
                if data[height][start]:
                    start += 1
                    height += 1
                # 왼쪽 가로선이 있는 경우
                elif start > 0 and data[height][start-1]:
                    start -= 1
                    height += 1
                else:
                    height += 1
        if check:
            continue
        else:
            return False
    return True


# x:가로선위치, y: 세로선위치
def dfs(x, y, cnt):
    global answer
    if check():
        answer = min(cnt, answer)
        return
    elif cnt == 3 or answer <= cnt:
        return
    # 빈 곳에 사다리 세우기
    for i in range(x, h):
        for j in range(n-1):
            if i == x and j < y:
                continue
            if data[i][j] == 0 and data[i][j+1] == 0:
                # 사다리 설치
                data[i][j] = 1
                # i,j+1에는 설치못하므로 j+2
                dfs(i, j+2, cnt+1)
                # 사다리 해제
                data[i][j] = 0


n, m, h = map(int, input().split())
data = [[0]*n for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    data[a-1][b-1] = 1

answer = 4
dfs(0, 0, 0)
if answer > 3:
    print(-1)
else:
    print(answer)
