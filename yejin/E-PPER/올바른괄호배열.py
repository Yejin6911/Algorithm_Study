from itertools import combinations


def check(x):
    stack = []
    for i in x:
        if i == '(':
            stack.append(i)
        else:
            if not len(stack):
                return False
            stack.pop()
    if len(stack):
        return False
    return True


n = int(input())
# 왼쪽 괄호가 있을 수 있는 위치의 경우의 수
candidates = list(combinations([x for x in range(2*n)], n))

result = 0
for candidate in candidates:
    now = ''
    for i in range(2*n):
        if i in candidate:
            now += '('
        else:
            now += ')'
    if check(now):
        result += 1

print(result)
