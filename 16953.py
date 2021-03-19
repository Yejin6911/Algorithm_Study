import sys
A, B = map(int, sys.stdin.readline().rstrip().split())

cnt = 1
while B != A:
    if B < A:
        cnt = -1
        break
    if B % 2 == 0:
        B //= 2
        cnt += 1
    else:
        if str(B)[-1] == '1':
            B //= 10
            cnt += 1
        else:
            cnt = -1
            break

print(cnt)
