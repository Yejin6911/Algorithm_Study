n = int(input()) # 도시의 개수

d = list(map(int, input().split())) # 도로의 길이
price = list(map(int, input().split())) # 리터당 가격

pre = price[0]
answer = pre * d[0]
for i in range(1, n-1):
    if(price[i] < pre): # 더 가격이 싸면 가격 갱신
        pre = price[i]
    answer += (pre*d[i])

print(answer)
