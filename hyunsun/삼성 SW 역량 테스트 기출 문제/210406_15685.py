#새로운 점의 위치를 방향으로 접근
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

#1. 드래콘커브 그리기
n = int(input())
s = [[0] * 101 for i in range(101)]
for i in range(n):
    y, x, d, g = map(int, input().split())
    s[x][y] = 1 #시작점 찍기
    temp = [d] #시작 방향 입력
    q = [d] #큐 - 선입선출
    for _ in range(g + 1):
        for k in q:
            x += dx[k]
            y += dy[k]
            s[x][y] = 1
        q = [(i + 1) % 4 for i in temp]
        q.reverse()
        temp = temp + q
result = 0

#2. 정사각형 개수 세기
for i in range(100):
        for j in range(100):
            if s[i][j] and s[i][j + 1] and s[i + 1][j] and s[i + 1][j + 1]:
                result += 1
print(result)
