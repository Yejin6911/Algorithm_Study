n = int(input())

cnt = 0
while True:
    if n >= 3600:
        cnt += n//3600
        n -= (n//3600)*3600
    elif n >= 60:
        cnt += n//60
        n -= (n//60)*60
    else:
        cnt += n
        break

print(cnt)
