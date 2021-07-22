def solution(A):
    if(len(A) == 3):
        return A[0] * A[1] * A[2]
        
    A = sorted(A)
    minus = []
    plus = []
    zero = 0

    for i in range(len(A)):
        if(A[i] < 0):
            minus.append(A[i])
        elif(A[i] == 0):
            zero = 1
        else:
            plus.append(A[i])

    if(len(minus) == 0 or len(minus) == 1): # 모두 양수
        return plus[-1] * plus[-2] * plus[-3]
    elif(len(plus) == 0): # 모두 음수
        if(zero == 1):
            return 0
        else:
            return minus[-1] * minus[-2] * minus[-3]
    elif(len(minus) >= 2 and len(plus) < 3):
        return minus[0] * minus[1] * plus[-1]
    elif(len(minus) >= 2 and len(plus) >= 3):
        tempminus = minus[0] * minus[1]
        maxplus = plus[-1] * plus[-2] * plus[-3]
        if(maxplus < tempminus * plus[-1]):
            maxplus = tempminus * plus[-1]
        return maxplus