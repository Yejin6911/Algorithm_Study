def impossible(result):
    col, row = 0, 1
    for x, y, a in result:
        if(a == col): # 기둥일 때
            if(y != 0 and (x, y-1, col) not in result and (x-1, y, row) not in result and (x, y, row) not in result):
                return True
        else: # 보일 때
            if((x, y-1, col) not in result and (x+1, y-1, col) not in result and not ((x-1, y, row) in result and (x+1, y, row) in result)):
                return True
    return False
 
 
def solution(n, build_frame):
    result = set()

    for x, y, a, build in build_frame:
        item = (x, y, a)

        if(build): # 추가일 때
            result.add(item)
            if(impossible(result)):
                result.remove(item)
        elif(item in result): # 삭제일 때
            result.remove(item)
            if(impossible(result)):
                result.add(item)
    answer = map(list, result)

    return sorted(answer, key=lambda x:(x[0], x[1], x[2]))

# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

# solution(n, build_frame)