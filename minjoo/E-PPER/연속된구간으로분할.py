s = list(input())

ans = []

pre = ''
p = ''
for i in range(len(s)):
    if(s[i] == p):
        continue

    if(pre == ''):
        pre = s[i]
        p = ''
        continue

    if(pre[-1] != s[i]):
        pre += s[i]
    else:
        p = pre[-1]
        ans.append(pre[:-1])
        pre = ''

if(pre != '' or p != ''):
    ans.append(pre)
print(ans)