n = int(input())
s = list(map(int, input().split()))
e = list(map(int, input().split()))

time = []
for i in range(n):
    time.append([s[i], e[i]])

time.sort(key=lambda x:(x[1], x[0]))

cnt = 1
end1 = time[0][1]
end2 = 0

for i in range(1, n):

    # 첫번째 자리에 넣을 수 있는 경우
    if(time[i][0] >= end1 and time[i][0] < end2):
        cnt += 1
        end1 = time[i][1]

    # 두번째 자리에 넣을 수 있는 경우
    elif(time[i][0] >= end2 and time[i][0] < end1):
        cnt += 1
        end2 = time[i][1]

    # 두 자리 모두 넣을 수 있는 경우 -> 시간 차이가 더 작은 곳으로 넣어줌
    elif(time[i][0] >= end1 and time[i][0] >= end2):
        one = time[i][0] - end1
        two = time[i][0] - end2
        if(one <= two):
            end1 = time[i][1]
        else:
            end2 = time[i][1]
        cnt += 1

print(cnt)