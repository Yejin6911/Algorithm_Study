N = int(input())
N = 1000 - N
sum = 0

while (N - 500) >= 0 :
    sum += 1
    N -= 500

while (N - 100) >= 0 :
    sum += 1
    N -= 100

while (N - 50) >= 0 :
    sum += 1
    N -= 50 


while (N - 10) >= 0 :
    sum += 1
    N -= 10

while (N - 5) >= 0 :
    sum += 1
    N -= 5

while (N - 1) >= 0 :
    sum += 1
    N -= 1

print(sum)
