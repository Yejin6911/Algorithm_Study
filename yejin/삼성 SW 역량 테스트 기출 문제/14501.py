from sys import stdin
n = int(stdin.readline().rstrip())
data = []

for i in range(n):
    t, p = map(int, stdin.readline().rstrip().split())
    data.append((t, p))

# 방법 1
price = [0]*(n+1)
for i in range(n-1, -1, -1):  # 뒤에서부터  탐색(dp)
    day = data[i][0]
    pay = data[i][1]
    if day + i > n:
        price[i] = price[i + 1]
    else:
        price[i] = max(price[i + 1], pay + price[i + day])

# 방법 2
# price = [0]*n
# for i in range(n):
#     t, p = map(int, stdin.readline().rstrip().split())
#     data.append((t, p))

# for i in range(n-1, -1, -1):  # 뒤에서부터  다이나믹 프로그래밍
#     day = data[i][0]
#     pay = data[i][1]

#     if day > n - i:  # 남은 기간보다 상담일이 길 경우
#         if i != n-1:
#             price[i] = price[i+1]  # 이전 최댓값 저장
#         continue
#     if i == n-1:  # 마지막 날 하루짜리 상담
#         price[i] = pay
#     elif i + day == n:  # 현재 일을 시작하면 정확히 마지막에 끝나는 경우
#         price[i] = max(pay, price[i+1])
#     else:
#         # 현재 일을 맡을 경우 or 맡지 않을 경우
#         price[i] = max(pay + price[i + day], price[i+1])

print(price[0])

# 틀린 코드
# for i in range(n):
#     t, p = map(int, stdin.readline().rstrip().split())
#     start = i
#     end = i+t-1
#     if end < n:
#         data.append((start, end, p))


# def find(start, price, pick):
#     global result
#     if start >= len(data) or len(data[start:]) == 0:
#         result = max(price, result)
#         #print(pick, result)
#         return
#     for d in data[start:]:
#         find(d[1]+1, price+d[2], pick+[d])


# result = 0
# for d in data:
#     pick = [d]
#     find(d[1]+1, d[2], pick)

# print(result)
