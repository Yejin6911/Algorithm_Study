alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

data = list(input())

pre = data[0]
ans = ""
cnt = 1

if(data[0] == "1"):
    ans += "1"

for i in range(1, len(data)):
    if(data[i] == pre):
        cnt += 1
    else:
        ans += alpha[cnt-1]
        pre = data[i]
        cnt = 1

if(cnt > 0):
    ans += alpha[cnt-1]
    
print(ans)
