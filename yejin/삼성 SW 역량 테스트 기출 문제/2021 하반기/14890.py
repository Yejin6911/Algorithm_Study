from itertools import filterfalse
import sys
input = sys.stdin.readline


def checkRow(n):
    # 앞 경사로 설치 확인을 위한 배열
    build = [0]*N
    h = board[n][0]
    idx = 1
    while True:
        if idx == N:
            return True
        if board[n][idx] == h:
            idx += 1
        else:
            if abs(h-board[n][idx]) > 1:
                return False
            else:
                next_h = board[n][idx]
                # 다음 높이가 더 낮은 경우
                if next_h < h:
                    for i in range(1, L):
                        if idx+i >= N or next_h != board[n][idx+i]:
                            return False
                    # L만큼 길이 일정한 경우
                    build[idx:idx+L] = [1]*L
                    h = next_h
                    idx += L
                # 다음 높이가 더 높은 경우
                else:
                    for i in range(1, L+1):
                        if idx-i < 0 or h != board[n][idx-i] or build[idx-i]:
                            return False
                    # L만큼 길이 일정한 경우
                    h = next_h
                    idx += 1


def checkCol(n):
    # 앞 경사로 설치 확인을 위한 배열
    build = [0]*N
    h = board[0][n]
    idx = 1
    while True:
        if idx == N:
            return True
        if board[idx][n] == h:
            idx += 1
        else:
            if abs(h-board[idx][n]) > 1:
                return False
            else:
                next_h = board[idx][n]
                # 다음 높이가 더 낮은 경우
                if next_h < h:
                    for i in range(1, L):
                        if idx+i >= N or next_h != board[idx+i][n]:
                            return False
                    # L만큼 길이 일정한 경우
                    build[idx:idx+L] = [1]*L
                    h = next_h
                    idx += L
                # 다음 높이가 더 높은 경우
                else:
                    for i in range(1, L+1):
                        if idx-i < 0 or h != board[idx-i][n] or build[idx-i]:
                            return False
                    # L만큼 길이 일정한 경우
                    h = next_h
                    idx += 1


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    if checkRow(i):
        cnt += 1
    if checkCol(i):
        cnt += 1
print(cnt)
