coin = [500, 100, 50, 10, 5, 1]
answer = 0

change = 1000 - int(input()) # 거스름돈

for i in range(len(coin)):
    if(change == 0):
        break
    q = change // coin[i]
    if(q > 0):
        answer += q
        change = change % coin[i]

print(answer)