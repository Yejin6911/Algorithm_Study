def solution(X, Y, D):
    N = (Y - X) // D
    if((Y - X) % D != 0):
        return N+1
    else:
        return N