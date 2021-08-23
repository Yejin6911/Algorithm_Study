def make_matrix(A, matrix):
    # [[0]*2]*2 로 하면 리스트가 공유되서 다른 결과가 나옴
    dummy_matrix = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                dummy_matrix[i][j] += (matrix[i][k] * A[k][j])
            dummy_matrix[i][j] %= 1000

    return dummy_matrix

def matmul(A, B):
    if(B == 1):
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
       
        return A
    
    # 홀수인 경우엔, A를 마지막에 곱해주어야 합니다.
    # ex) AAAAA -> (A^2)^2 * A
    elif((B%2) == 1):
        matrix = matmul(A, B-1)
        new_matrix = make_matrix(A, matrix)
    
        return new_matrix
    
    # 짝수인 경우엔, 제곱수로 계속해서 곱해집니다.
    # ex) AAAA -> (A^2) = AA -> (A^2)^2 = AAAA
    else:
        matrix = matmul(A, B//2)
        new_matrix = make_matrix(matrix, matrix)
    
        return new_matrix

N, B = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

result = matmul(A, B)

for row in result:
    print(*row)