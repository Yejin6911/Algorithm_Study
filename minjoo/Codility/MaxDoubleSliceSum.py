def solution(A):
    if(len(A) == 3):
        return 0
    temp = A[1:len(A)-1]
    sorttemp = sorted(temp, reverse=True)
    maxsum = 0
    for i in range(len(sorttemp)-1):
        m = maxsum + sorttemp[i]
        if(m > maxsum):
            maxsum = m
        else:
            break
    return maxsum