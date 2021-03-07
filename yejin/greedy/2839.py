import sys

n = int(sys.stdin.readline().rstrip())


def check(n, k):
    pass


result = 0
num_5 = n//5

while num_5 >= 0:
    # 봉지 5 를 최대 사용했을 때 나누어 떨어지는지 확인
    if (n - 5*num_5) % 3 == 0:
        num_3 = (n-5*num_5)//3
        result = num_5+num_3
        break
    # 아닌 경우 봉지 5의 갯수 한개씩 줄임
    else:
        num_5 -= 1

# 만들 수 없는 무게인 경우
if num_5 < 0:
    print(-1)
else:
    print(result)
