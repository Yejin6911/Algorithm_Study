n = int(input()) # 회의의 수

timetable = []
for _ in range(n):
    timetable.append(list(map(int, input().split())))

timetable.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end = timetable[0][1]
for i in range(1, n):
    if(timetable[i][0] >= end):
        cnt += 1
        end = timetable[i][1]

print(cnt)