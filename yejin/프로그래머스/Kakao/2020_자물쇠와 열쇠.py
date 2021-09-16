def rotate90(key):
    n = len(key)
    result = [[0]*n for _ in range(n)]  # 결과 리스트
    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = key[i][j]
    return result


# 자물쇠의 중간 부분이 모두 1인지 확인
def check(board, m, n):
    for i in range(n):
        for j in range(n):
            if(board[m+i][m+j] != 1):
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 크기를 2m+n으로 변경(좌물쇠 놓을 수 있는 곳 고려)
    new_lock = [[0]*(2*m+n) for _ in range(2*m+n)]
    # 새로운 자물쇠 가운데 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[m+i][m+j] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for _ in range(4):
        key = rotate90(key)  # 열쇠 회전
        for x in range(1, m+n):
            for y in range(1, m+n):
                # 자물쇠에 열쇠 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
            # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock, m, n) == True:
                    return True
                # 자물쇠에서 열쇠 다시 뺴기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
