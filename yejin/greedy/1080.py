import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
array = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

# 두변째 배열 입력받을 떄 바로 처음 입력받은 배열이랑 비교해서 다르면 기존 배열을 1, 같으면 0으로 update 해서 배열 한개만 사용해주었다.
for i in range(N):
    now = list(map(int, list(sys.stdin.readline().rstrip())))
    for j in range(M):
        if array[i][j] != now[j]:
            array[i][j] = 1
        else:
            array[i][j] = 0


# 두 배열이 다른 서로 다른 원소가 존재하는지 확인
def check():
    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                return False
    return True


# 3*3부분을 뒤집어주는 함수
def change(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            array[i][j] = 1-array[i][j]


cnt = 0
# (0,0)부터 시작해서 해당 지점을 기준으로 3*3크기부분을 비교 후 변경해주면
# 해당 지점은 변경이 완료되었기 때문에 다시 돌아와서 바꿔 줄 필요가 없다.
for i in range(N-2):
    for j in range(M-2):
        if array[i][j] == 1:
            cnt += 1
            change(i, j)

# 서로다른 부분이 존재할 경우 -1, 모두같을 경우 0 출력
if check():
    print(cnt)
else:
    print(-1)
