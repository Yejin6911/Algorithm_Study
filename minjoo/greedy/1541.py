data = list(input().split('-'))

for i in range(len(data)):
    if('+' in data[i]): # 덧셈 먼저 계산
        num = list(map(int, data[i].split('+')))
        data[i] = sum(num)
    else:
        data[i] = int(data[i])

answer = data[0]
for i in range(1, len(data)): # 뺄셈 계산
    answer -= data[i]

print(answer)