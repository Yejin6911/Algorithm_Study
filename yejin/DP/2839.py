import sys
input = sys.stdin.readline

n = int(input())
ans = 0
while True:
    if n % 5 == 0:
        ans += n//5
        break
    n -= 3
    ans += 1
    if n < 0:
        ans = -1
        break

print(ans)
