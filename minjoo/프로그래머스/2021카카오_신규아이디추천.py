x = list(input())

# 1단계: 소문자로 치환
for i in range(len(x)):
    if(x[i].isalpha()):
        x[i] = x[i].lower()

# 2단계: 문자 제거
pos = ['-', '_', '.']
idx = []
for i in range(len(x)):
    if(x[i].isalnum() or x[i] in pos):
        pass
    else:
        idx.append(i)
idx.sort(reverse=True)
for i in range(len(idx)):
    x.pop(idx[i])

# 3단계: 마침표 하나로 치환
idx = []
for i in range(1, len(x)):
    if(x[i] == '.' and x[i-1] == '.'):
        idx.append(i-1)
idx.sort(reverse=True)
for i in range(len(idx)):
    x.pop(idx[i])

# 4단계: 마침표 처음, 끝 제거
if(len(x)>0 and x[0] == '.'):
    x.pop(0)
if(len(x)>0 and x[-1] == '.'):
    x.pop(-1)

# 5단계: 빈 문자열일 경우, 'a' 대입
if(len(x) == 0):
    x = ['a']

# 6단계: 길이가 16 이상이면, 첫 15개 문자 뺀 나머지 제거
if(len(x) >= 16):
    x = x[:15]
if(x[-1] == '.'):
    x.pop(-1)

# 7단계: 길이가 2 이하이면, 마지막 문자 반복
if(len(x) <= 2):
    alpha = x[-1]
while(len(x) < 3):
    x.append(alpha)

for i in range(len(x)):
    print(x[i], end='')