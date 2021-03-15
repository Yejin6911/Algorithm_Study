n = int(input()) # 수열의 크기

plus = []
minus = []

for _ in range(n):
    num = int(input())
    if(num > 0):
        plus.append(num)
    else:
        minus.append(num)

plus.sort(reverse=True) # 큰수부터 정렬
minus.sort() # 작은수부터 정렬

answer = 0
temp = 0
for i in range(len(plus)):
    if(plus[i] == 1): # 1이면 곱하지 않고 바로 더해줌
        answer += plus[i]
        continue
    if(temp == 0):
        temp = plus[i]
    else:
        temp *= plus[i] # 이전 수랑 곱해서
        answer += temp # 더해줌
        temp = 0
if(temp != 0):
    answer += temp

temp = 10001
for i in range(len(minus)):
    if(temp == 10001):
        temp = minus[i]
    else:
        temp *= minus[i] # 이전 수랑 곱해서
        answer += temp # 더해줌
        temp = 10001
if(temp != 10001):
    answer += temp

print(answer)