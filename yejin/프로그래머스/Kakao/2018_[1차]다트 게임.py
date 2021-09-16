area = ['S', 'D', 'T']


def solution(dartResult):
    temp = 0
    prev = 0
    answer = 0
    idx = 0
    while idx <= len(dartResult):
        if idx == len(dartResult):
            answer += temp
            return answer
        now = dartResult[idx]
        if now.isdigit():
            if idx != 0:
                answer += temp
                prev = temp
                temp = int(now)
            else:
                temp = int(now)
        elif now in area:
            temp = temp**(area.index(now)+1)
        else:
            if now == '*':
                temp *= 2
                answer += prev
            else:
                temp *= (-1)
        idx += 1


print(solution('1S2D*3T'))
