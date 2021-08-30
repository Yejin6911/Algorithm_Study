n, r = map(int, input().split())
time = list(map(int, input().split()))

relations = [[0]*n for _ in range(n)]
for _ in range(r):
    a, b = map(int, input().split())
    relations[a-1][b-1] = 1

end = int(input())-1
# 바로 다음에 끝나는 작업을 저장하는 리스트
temp = [end]
result = time[end]

while True:
    new_temp = []
    times = []
    for i in temp:
        for j in range(n):
            if relations[j][i] == 1:
                new_temp.append(j)
                times.append(time[j])
    if len(new_temp):
        result += max(times)
        temp = new_temp
    else:
        break

print(result)
