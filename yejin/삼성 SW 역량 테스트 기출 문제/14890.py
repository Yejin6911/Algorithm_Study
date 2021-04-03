import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split()))
         for _ in range(N)]


def check(now):
    start = 0
    # 가장 마지막 설치된 경사로의 끝부분
    installed = -1
    while True:
        if start == N-1:
            break
        # 높이 같은 경우
        if now[start] == now[start+1]:
            start += 1
            continue
        # 높이 차이 2 이상인 경우
        elif abs(now[start] - now[start+1]) > 1:
            return False
        else:
            # 앞 블럭이 더 높은 경우
            if now[start] > now[start+1]:
                # 경사로를 놓다가 범위를 넘어가는 경우
                if start+L >= N:
                    return False
                height = now[start+1]
                # 경사로 설치 가능여부 확인
                for i in range(2, L+1):
                    if now[start+i] != height:
                        return False
                # 경사로 설치
                installed = start+L
                start += L
            # 뒷 블럭이 더 높은 경우
            else:
                # 경사로를 놓다가 범위를 넘어가는 경우
                if start-L+1 < 0:
                    return False
                height = now[start]
                for i in range(1, L):
                    if now[start-i] != height:
                        return False
                # 경사로 설치
                if start-L+1 <= installed:
                    return False
                installed = start
                start += 1
    return True


cnt = 0

# 행 확인
for i in range(N):
    row = board[i]
    if check(row):
        cnt += 1

# 열 확인
for i in range(N):
    col = []
    for j in range(N):
        col.append(board[j][i])
    if check(col):
        cnt += 1


print(cnt)
