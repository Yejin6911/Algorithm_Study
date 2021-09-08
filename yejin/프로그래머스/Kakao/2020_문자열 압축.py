def solution(s):
    answer = len(s)
    # i: 자를 문자열의 길이
    for i in range(1, len(s)+1):
        result = ""
        temp = s[:i]
        cnt = 1
        idx = i
        while idx <= len(s):
            if temp == s[idx:idx+i]:
                cnt += 1
                idx += i
            else:
                if cnt > 1:
                    result += (str(cnt)+temp)
                else:
                    result += temp
                temp = s[idx:idx+i]
                cnt = 1
                idx += i
        if len(temp):
            result += temp
        answer = min(answer, len(result))
    return answer


print(solution("aabbaccc"))
