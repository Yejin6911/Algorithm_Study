def count(s, length):
    answer = ''
    cnt_list = []
    i = 0
    flag = 0
    while(i < len(s)-2*length+1):
        temp = s[i:i+length]
    
        cnt = 0
        start = i + length
        while(1):
            next_temp = s[start:start+length]
            if(temp == next_temp):
                cnt += 1
                start = start + length
                flag = 1
            else:
                cnt_list.append([i, cnt])
                break
        i = start
    # print(cnt_list)
    if(flag == 1):
        for i in range(len(cnt_list)):
            if(cnt_list[i][1] == 0):
                answer += s[cnt_list[i][0]:cnt_list[i][0]+length]
            else:
                answer += str(cnt_list[i][1]+1)
                answer += s[cnt_list[i][0]:cnt_list[i][0]+length]
        if(cnt_list[-1][0] + (cnt_list[-1][1]+1)*length < len(s)):
            answer += s[cnt_list[-1][0] + (cnt_list[-1][1]+1)*length:]
    else:
        answer = s
    return answer

def solution(s):
    answer_list = []
    for i in range(1, len(s)//2 + 1):
        answer_list.append(count(s, i))
    # print("answer_list", answer_list)
    min_length = len(s)
    for answer in answer_list:
        if(len(answer) < min_length):
            min_length = len(answer)

    return min_length


s = "abcabcabcabcdededededede"
solution(s)