def solution(A):
    if(len(A) == 0):
        return 1
    
    A = sorted(A)
    for i in range(len(A)):
        if((i+1) != A[i]):
            return i+1
    
    return len(A)+1