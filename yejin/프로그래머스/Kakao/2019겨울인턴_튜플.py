def solution(s):
    answer = []
    s = s[1:-1]
    temp = ''
    new_s = []
    i = 0
    while i < len(s):
        if s[i] == '{':
            i += 1
        elif s[i].isdigit() or s[i] == ',':
            temp += s[i]
            i += 1
        elif s[i] == '}':
            new_s.append(temp)
            temp = ''
            i += 2
    new_s.sort(key=len)
    for set in new_s:
        set = set.split(',')
        for n in set:
            if int(n) not in answer:
                answer.append(int(n))
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
