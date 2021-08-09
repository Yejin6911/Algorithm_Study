import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(n)]
cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(m):
    d, s = map(int, input().rstrip().split())
    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + dx[d]*s) % n
        cloud[i][1] = (cloud[i][1] + dy[d]*s) % n
        A[cloud[i][0]][cloud[i][1]] += 1
    # 물 복사 버그
    for x, y in cloud:
        for d in [2, 4, 6, 8]:
            nx = x+dx[d]
            ny = y+dy[d]
            if 0 <= nx < n and 0 <= ny < n and A[nx][ny]:
                A[x][y] += 1
    # 구름 생성
    new_cloud = []
    for x in range(n):
        for y in range(n):
            if A[x][y] >= 2 and [x, y] not in cloud:
                new_cloud.append([x, y])
                A[x][y] -= 2
    cloud = new_cloud

result = 0
for x in range(n):
    for y in range(n):
        result += A[x][y]
print(result)
