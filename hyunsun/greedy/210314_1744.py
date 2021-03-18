N=int(input())

pos_nums=[]
neg_nums=[]
z_o=[]
#pos랑 neg가 홀짝인지 알아야 풀 수 있어서 따로 저장 

for i in range(N):
  num=int(input())
  if num>1:
    pos_nums.append(num)
  elif num<0:
    neg_nums.append(num)
  else:
    z_o.append(num)

sum = 0
pos_nums.sort(reverse = True)
PN = len(pos_nums)

if PN == 1: #이면 for문 안 돌아가니까
    sum += pos_nums[0]
for i in range(0,PN//2,2):
    sum += pos_nums[i]*pos_nums[i+1]
if N%2 == 1 :
    sum += pos_nums[PN-1]
#print(sum)

NN = len(neg_nums)
neg_nums.sort()
if NN == 1:
    sum += neg_nums[0]
if 0 not in z_o:
    for i in range(0,NN//2,2):
        sum += neg_nums[i]*neg_nums[i+1]
    if N%2 == 1 :
        sum += neg_nums[NN-1]

else:
    for i in range(0,NN-1//2,2):
        sum += neg_nums[i-1]*neg_nums[i]
    if N%2 == 0 :
        sum += neg_nums[NN-1]
#print(sum)
for i in z_o:
    sum += i
print(sum)


https://velog.io/@sch804/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1744%EB%B2%88-%EC%88%98-%EB%AC%B6%EA%B8%B0
