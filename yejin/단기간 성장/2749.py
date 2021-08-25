import sys
input = sys.stdin.readline

# https://www.acmicpc.net/blog/view/28
# 피보나치수를 M으로 나눈 나머지는 항상 주기를 가진다.
# N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같다.

# M 이 10의 k제곱일 때, k>2이면, 주기는 15*10**(k-1)

n = int(input())
mod = 1000000
# 주기
p = mod//10*15

fibo = [0, 1]
for i in range(2, p):
    fibo.append(fibo[i-1]+fibo[i-2])
    fibo[i] %= mod

print(fibo[n % p])
