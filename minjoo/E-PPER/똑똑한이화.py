num = int(input())

cnt = 0
if(num // 3600):
    cnt += num // 3600
    num = num % 3600
if(num // 60):
    cnt += num // 60
    num = num % 60
cnt += num

print(cnt)