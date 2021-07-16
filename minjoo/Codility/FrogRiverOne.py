def solution(X, A):
    visited = [0 for _ in range(X+1)]
    checksum = 0
    for i in range(len(A)):
        if(0 <= A[i] <= X and visited[A[i]] == 0):
            visited[A[i]] = 1
            checksum += 1
        if(checksum == X):
            return i
       
    return -1
