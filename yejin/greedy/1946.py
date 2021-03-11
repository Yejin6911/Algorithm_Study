import sys

t = int(sys.stdin.readline().rstrip())


#처음풀이 - 시간초과
# def solution():
#     n = int(sys.stdin.readline().rstrip())
#     data = []
#     for i in range(n):
#         first, second = map(int, sys.stdin.readline().rstrip().split())
#         data.append((first, second))
#     data.sort()
#     result = 1
#     for i in range(1, len(data)):
#         check = True
#         for j in range(0, i+1):
#             if data[i][1] > data[j][1]:
#                 check = False
#                 break
#         if check:
#             result += 1
#     return result


# 시간초과 해결 - 최속값 설정해서 반복문 없이 해당 값이랑만 비교
def solution():
    n = int(sys.stdin.readline().rstrip())
    data = []
    for i in range(n):
        first, second = map(int, sys.stdin.readline().rstrip().split())
        data.append((first, second))
    data.sort()
    result = 1
    # 1차 성적 1순위의 2차 성적 순위
    m = data[0][1]

    for i in range(1, len(data)):
        # m보다 높은 순위일 경우 결과 +1 한 후 최솟값 갱신
        if data[i][1] < m:
            result += 1
            m = data[i][1]
    return result


results = []
for i in range(t):
    results.append(solution())

for result in results:
    print(result)
