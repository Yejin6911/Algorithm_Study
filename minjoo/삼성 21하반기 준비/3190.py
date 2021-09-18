n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1 # 사과

l = int(input()) # 뱀 변환 횟수
change = []
for _ in range(l):
    x, c = input().split()
    change.append([int(x), c])


