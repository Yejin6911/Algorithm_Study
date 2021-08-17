import sys
input = sys.stdin.readline

n = int(input())

answer = 0
while(1):
    if(n < 0):
        answer = -1
        break

    if(n % 5 == 0):
        answer += n // 5
        break
    else:
        answer += 1
        n -= 3

print(answer)