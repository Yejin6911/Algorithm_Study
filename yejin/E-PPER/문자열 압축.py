data = list(input().strip())
answer = ""
if data[0] == 1:
    answer += "1"

prev = data[0]
cnt = 1
for i in range(1, len(data)):
    if data[i] == data[i-1]:
        cnt += 1
    else:
        answer += chr(64+cnt)
        cnt = 1
answer += chr(64+cnt)
print(answer)
