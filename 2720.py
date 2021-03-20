import sys

T = int(sys.stdin.readline().rstrip())
coins = [25, 10, 5, 1]

for _ in range(T):
    C = int(sys.stdin.readline().rstrip())
    for coin in coins:
        if C//coin > 0:
            print(C//coin, end=' ')
            C -= (C//coin)*coin
        else:
            print(0, end=' ')
    print()
