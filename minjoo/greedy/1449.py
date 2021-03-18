n, length = map(int, input().split()) # 물이 새는 곳의 개수, 테이프의 길이
location = list(map(int, input().split())) # 물이 새는 곳의 위치

location.sort()

answer = 0
temp = -1
for i in range(n):
    if(temp == -1):
        temp = location[i]
        limit = location[i] + (length - 1) # 테이프를 붙일 수 있는 최대 먼 곳
    else:
        if(location[i] < limit): # 최대 먼 곳보다 가까우면
            continue
        elif(location[i] == limit): # 최대 먼 곳이면
            temp = -1
            answer += 1
        else: # 최대 먼 곳을 벗어나면
            temp = location[i]
            limit = location[i] + (length - 1)
            answer += 1

if(temp != -1):
    answer += 1

print(answer)
