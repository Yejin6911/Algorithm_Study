def solution(A):
    front = sum(A[:1])
    back = sum(A[1:])
    ans = max(back - front, front - back)
  
    for i in range(1, len(A)-1):
        front += A[i]
        back -= A[i]
        temp = max(back - front, front - back)
        if(ans > temp):
            ans = temp

    return ans