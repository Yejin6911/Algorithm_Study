def divide(p):
    l, r = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            return p[:i+1], p[i+1:]

# 균형잡힌 괄호 문자열이 올바른 괄호 문자열인지 확인


def check(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if not len(stack):
                return False
            stack.pop()
    if not len(stack):
        return True
    else:
        return False


def changeU(u):
    u = u[1:len(u)-1]
    new_u = ''
    for i in u:
        if i == '(':
            new_u += ')'
        else:
            new_u += '('
    return new_u


def solution(p):
    # 1. 빈 문자열인 경우
    if not len(p):
        return ''
    u, v = divide(p)
    if check(u):
        new_v = solution(v)
        return u+new_v
    else:
        new_v = solution(v)
        return '('+new_v+')'+changeU(u)


print(solution("(()())()"))
