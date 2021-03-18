
p = input()

sum = 0

for i in range(1, len(p)):
    if p[i-1] != p[i]:
        sum += 1

#if sum%2 == 1: 
#   res = sum//2
#else:
#   res = (sum//2) + 1
   
#print(res)

isOdd = False
if sum%2 == 1: 
    isOdd = True
    
result = sum//2
if isOdd:
    result += 1

print(result)
