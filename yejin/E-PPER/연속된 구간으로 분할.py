s = input().strip()

result = []
temp = []
cnt = 1
for i in range(len(s)):
    # 앞부분 비교할 인자 없는 경우
    if not len(temp):
        temp.append(s[i])
    # 앞부분과 문자가 같은 경우
    elif s[i] == temp[-1]:
        cnt += 1
        temp.append(s[i])
    # 앞부분과 문자가 다른 경우
    else:
        if cnt >= 2:
            for j in range(cnt):
                temp.pop()
            result.append("".join(temp))
            temp = []
            cnt = 1
        temp.append(s[i])
# 마지막 남은부분 처리
if cnt >= 2:
    for j in range(cnt):
        temp.pop()
    result.append("".join(temp))
    temp = []
result.append("".join(temp))

print(result)
