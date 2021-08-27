n = int(input())
start = list(map(int, input().split()))
end = list(map(int, input().split()))
data = []
for i in range(n):
    data.append((start[i], end[i]))

# 종료시간 기준으로 정렬
data.sort(key=lambda x: x[1])

seat1 = (0, 0)
seat2 = (0, 0)
cnt = 0

while True:
    check = False
    for i in range(len(data)):
        # 두자리 종료시간들보다 늦게 시작하는 경우 더 늦게 끝나는 자리 다음에 배치
        if data[i][0] >= seat1[1] and data[i][0] >= seat2[1]:
            if seat1[1] < seat2[1]:
                seat2 = data.pop(i)
                cnt += 1
            else:
                seat1 = data.pop(i)
                cnt += 1
            check = True
        # 1번 자리 종료 시간보다 늦게 시작하는 경우
        elif data[i][0] >= seat1[1]:
            seat1 = data.pop(i)
            cnt += 1
            check = True
        # 2번 자리 종료 시간보다 늦게 시작하는 경우
        elif data[i][0] >= seat2[1]:
            seat2 = data.pop(i)
            cnt += 1
            check = True
        if check:
            break
    if not check:
        break

print(cnt)
