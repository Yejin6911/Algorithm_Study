import sys, math

input = sys.stdin.readline

n = int(input()) # 시험장 수
a = list(map(int, input().split()))
b, c = map(int, input().split()) # 총감독관 감시가능수, 부감독관 감시가능수

answer = n

for i in range(n):
    a[i] -= b # 총감독관이 감시하는 학생
    if(a[i] < 0):
        a[i] = 0
    q = math.ceil(a[i] / c) # 부감독관
    answer += q

print(answer)