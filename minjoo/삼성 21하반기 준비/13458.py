n = int(input()) # 시험장 수
a = list(map(int, input().split())) # 응시자 수
b, c = map(int, input().split())

cnt = 0
for i in range(len(a)):
    if(a[i] <= 0):
        continue
    cnt += 1 # 총감독관

    num = a[i] - b
    if(num > 0):
        cnt += num // c
        if(num % c > 0):
            cnt += 1

print(cnt)