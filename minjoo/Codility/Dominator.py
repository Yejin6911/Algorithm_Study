def solution(A):
    if(len(A) == 0):
        return -1
    elif(len(A) == 1):
        return 0

    s = list(set(A))
    cnt = {i : 0 for i in s}
  
    answer = ''
    for i in range(len(A)):
        cnt[A[i]] += 1
        if(cnt[A[i]] > (len(A) / 2)):
            answer = A[i]
            # answer = [s for s, x in enumerate(A) if x == A[i]]
            break

    if(answer == ''):
        return -1
    else:
        return A.index(answer)