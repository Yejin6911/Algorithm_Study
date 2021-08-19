import sys
input = sys.stdin.readline

# 거듭제곱의 분할정복 계산법 참고
# https://jjangsungwon.tistory.com/10


# 행렬의 곱셈 계산
def multiple(m1, m2):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (m1[i][k]*m2[k][j])

    for i in range(n):
        for j in range(n):
            result[i][j] %= 1000
    return result


# 거듭제곱 계산
def power(m, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                m[i][j] %= 1000
        return m
    else:
        temp = power(m, b//2)
        if b % 2 == 0:
            return multiple(temp, temp)
        else:
            return multiple(multiple(temp, temp), m)


n, b = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(n)]

result = power(m, b)
for row in result:
    print(*row)
