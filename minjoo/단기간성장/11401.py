# N! * (N-K)!*(K!)^(p-2) 를 구하는 문제

n, k = map(int, input().split())
p = 1000000007

# x^y
def mul(x, y):
    if(y == 0):
        return 1
    elif(y == 1):
        return x
    elif(y % 2 == 1): # 홀수이면
        return mul(x, y-1)*x
    else: # 짝수이면
        d = mul(x, y//2)
        d %= p
        return d ** 2 % p

t1 = 1
t2 = 1

# n! 부분
for i in range(1, n+1):
    t1 *= i
    t1 %= p

# k! 부분
for i in range(1, k+1):
    t2 *= i
    t2 %= p

# (n-k)! 부분
for i in range(1, n-k+1):
    t2 *= i
    t2 %= p

t3 = mul(t2, (p-2)%p)

print((t1*t3)%p)