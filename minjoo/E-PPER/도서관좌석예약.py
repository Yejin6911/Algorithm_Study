n = int(input())
s = list(map(int, input().split()))
e = list(map(int, input().split()))

time = []
for i in range(n):
    time.append([s[i], e[i]])

time.sort(key=lambda x:(x[0], x[1]))

print(time)
maxcnt = 0
maxidx = []
for i in range(n):
    start, end = time[i][0], time[i][1]
    temp = 1
    idx = [i]
    for j in range(i+1, n):
        if(time[j][0] >= end):
            temp += 1
            end = time[j][1]
            idx.append(j)
    if(maxcnt < temp):
        maxcnt = temp
        maxidx = idx

maxidx.sort(reverse=True)
for i in range(len(maxidx)):
    time.pop(maxidx[i])

print(maxcnt)
print(maxidx)
print(time)

maxcnt2 = 0
for i in range(len(time)):
    start, end = time[i][0], time[i][1]
    temp = 1
    for j in range(i+1, len(time)):
        if(time[j][0] >= end):
            temp += 1
            end = time[j][1]
    if(maxcnt2 < temp):
        maxcnt2 = temp

print(maxcnt + maxcnt2)