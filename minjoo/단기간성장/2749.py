# https://getchan.github.io/algorithm/acmicpc_2749/
# 파사노 주기: 피보나치 수를 나눌 수를 k라고 할 때, 
# k = 10^n 이면, 파사노 주기는 15*10^(n-1)이다.

n = int(input())

def fibo3(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b%1000000, (a+b)%1000000

    return a 

print(fibo3(n % (15*(10**5))))