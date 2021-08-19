import sys
input = sys.stdin.readline


def power(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return (power(a, b//2)**2) % p
    else:
        return (power(a, b//2)**2*a % p)


n, k = map(int, input().split())
p = 1000000007
# N!
temp1 = 1
for i in range(1, n+1):
    temp1 *= i
    temp1 %= p

temp2 = 1
# K!(N-K)!
for i in range(1, k+1):
    temp2 *= i
    temp2 %= p
for i in range(1, n-k+1):
    temp2 *= i
    temp2 %= p

# 페리마의 소정리 a^(p-1) ≡ 1(mod p) 에 의해서
# 1/(k!(n-k)!) ≡(k!(n-k)!)^(-1) ≡ (k!(n-k)!)^(p-1) * (k!(n-k)!)^(-1) ≡ (k!(n-k)!)^(p-2) (mod p)
temp3 = power(temp2, p-2) % p
print((temp1*temp3) % p)
