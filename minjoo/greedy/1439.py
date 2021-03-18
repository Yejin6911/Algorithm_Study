s = input()
zero = list(s.split('0'))
one = list(s.split('1'))
zero = [i for i in zero if i != '']
one = [i for i in one if i != '']

a = len(zero)
b = len(one)

if(a < b):
    print(a)
else:
    print(b)
    
# zeroidx = [i for i, value in enumerate(s) if value == '0']
# oneidx = [i for i, value in enumerate(s) if value == '1']
# # print(zeroidx, oneidx)
# def cal(idxlist):
#     answer = 1
#     pre = idxlist[0]
#     for i in range(1, len(idxlist)):
#         if(pre + 1 == idxlist[i]):
#             pass
#         else:
#             answer += 1
#         pre = idxlist[i]
#     return answer
    

# zero = cal(zeroidx)
# one = cal(oneidx)
# # print(zero, one)
# if(zero < one):
#     print(zero)
# else:
#     print(one)
