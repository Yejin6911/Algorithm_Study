import math

def solution(A, B, K):
    aq = A / K
    bq = B / K
    a = math.ceil(aq)
    b = math.floor(bq)
    return b - a + 1