n = int(input())

ans = 0

def dfs(acnt, bcnt, t):
    global ans
    if(len(t) == 2*n-1):
        ans += 1
        return

    if(acnt == bcnt and acnt < n):
        at = t + 'a'
        acnt += 1
        dfs(acnt, bcnt, at)
        return 

    # b개수가 더 적음
    if(acnt < n):
        at = t + 'a'
        acnt += 1
        dfs(acnt, bcnt, at)
        acnt -= 1
    
    bt = t + 'b'
    bcnt += 1
    dfs(acnt, bcnt, bt)
    bcnt -= 1

dfs(1, 0, 'a')
print(ans)