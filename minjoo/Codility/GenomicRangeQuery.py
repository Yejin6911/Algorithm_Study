def solution(S, P, Q):
    result = []
    for i in range(len(P)):
        minans = 5
        
        if('A' in S[P[i]:Q[i]+1]):
            ans = 1
        elif('C' in S[P[i]:Q[i]+1]):
            ans = 2
        elif('G' in S[P[i]:Q[i]+1]):
            ans = 3
        else:
            ans = 4
        if(minans > ans):
            minans = ans
        result.append(minans)
    return result