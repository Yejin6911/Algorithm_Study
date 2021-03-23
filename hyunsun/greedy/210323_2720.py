N = int(input())

for _ in range(N):
    money = int(input())        
    coin = {25: 0, 10: 0, 5: 0, 1: 0}
    
    while money:
        for num in [25, 10, 5, 1]:
            while money >= num:
                money -= num
                coin[num] += 1
                
    print(coin[25], coin[10], coin[5], coin[1])
    
#for _ in range(N):
#    money = int(input())        
#    coin = [25, 1, 5, 1]
#    
#    answer = []
#    for i in range(len(coin)):
#        if(money == 0):
#            break
#        q = money // coin[i]
#        if(q > 0):
#            answer.append(q)
#            money = money % coin[i]

#   print(answer)
