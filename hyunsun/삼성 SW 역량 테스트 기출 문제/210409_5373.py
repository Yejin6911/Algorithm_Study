def rotate(color, ro): #회전한 면 회전
    if ro == "-":
        temp = [[0] * 3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                temp[2 - j][i] = color[i][j]
        return temp
    else:
        temp = [[0] * 3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                temp[j][2 - i] = color[i][j]
        return temp

def rotation(p, ro):면 #회전한 옆면 회전
    global w, y, r, o, g, b
    if p == "U" or p == "D":
        if p == "U" and ro == "-" or p == "D" and ro == "+": 
            if p == "U":
                i = 0
                w = rotate(w, ro)

            else:
                i = 2
                y = rotate(y, ro)
                
            r1, r2, r3, b1, b2, b3 = r[i][0], r[i][1], r[i][2], b[i][0], b[i][1], b[i][2]
            o1, o2, o3, g1, g2, g3 = o[i][0], o[i][1], o[i][2], g[i][0], g[i][1], g[i][2]
            r[i][0], r[i][1], r[i][2], b[i][0], b[i][1], b[i][2] = g1, g2, g3, r1, r2, r3
            o[i][0], o[i][1], o[i][2], g[i][0], g[i][1], g[i][2] = b1, b2, b3, o1, o2, o3
            
        else:
            if p == "U":
                i = 0
                w = rotate(w, ro)

            else:
                i = 2
                y = rotate(y, ro)
                
            r1, r2, r3, b1, b2, b3 = r[i][0], r[i][1], r[i][2], b[i][0], b[i][1], b[i][2]
            o1, o2, o3, g1, g2, g3 = o[i][0], o[i][1], o[i][2], g[i][0], g[i][1], g[i][2]
            r[i][0], r[i][1], r[i][2], b[i][0], b[i][1], b[i][2] = b1, b2, b3, o1, o2, o3
            o[i][0], o[i][1], o[i][2], g[i][0], g[i][1], g[i][2] = g1, g2, g3, r1, r2, r3  
            
    elif p == "F" or p == "B":
        if p == "F" and ro == "-" or p == "B" and ro == "+":
            if p == "F":
                i = 0
                r = rotate(r, ro)

            else:
                i = 2
                o = rotate(o, ro)
            y1, y2, y3, w1, w2, w3 = y[i][0], y[i][1], y[i][2], w[2-i][0], w[2-i][1], w[2-i][2]
            b1, b2, b3, g1, g2, g3 = b[0][i], b[1][i], b[2][i], g[0][2-i], g[1][2-i], g[2][2-i]
            y[i][0], y[i][1], y[i][2], w[2-i][0], w[2-i][1], w[2-i][2]= g1, g2, g3, b1, b2, b3
            b[0][i], b[1][i], b[2][i], g[0][2-i], g[1][2-i], g[2][2-i] = y3, y2, y1, w3, w2, w1
   
        else:
            if p == "F":
                i = 0
                r = rotate(r, ro)

            else:
                i = 2
                o = rotate(o, ro)
            y1, y2, y3, w1, w2, w3 = y[i][0], y[i][1], y[i][2], w[2-i][0], w[2-i][1], w[2-i][2]
            b1, b2, b3, g1, g2, g3 = b[0][i], b[1][i], b[2][i], g[0][2-i], g[1][2-i], g[2][2-i]
            y[i][0], y[i][1], y[i][2], w[2-i][0], w[2-i][1], w[2-i][2] = b3, b2, b1, g3, g2, g1
            b[0][i], b[1][i], b[2][i], g[0][2-i], g[1][2-i], g[2][2-i] = w1, w2, w3, y1, y2, y3

    elif p == "L" or p == "R":
        if p == "L" and ro == "-" or p == "R" and ro == "+":
            if p == "L":
                i = 0
                g = rotate(g, ro)
            else:
                i = 2
                b = rotate(b, ro)
                
            w1, w2, w3, r1, r2, r3 = w[0][i], w[1][i], w[2][i], r[0][i], r[1][i], r[2][i]
            y1, y2, y3, o1, o2, o3 = y[0][i], y[1][i], y[2][i], o[0][2-i], o[1][2-i], o[2][2-i]
            w[0][i], w[1][i], w[2][i], r[0][i], r[1][i], r[2][i] = r1, r2, r3, y1, y2, y3
            y[0][i], y[1][i], y[2][i], o[0][2-i], o[1][2-i], o[2][2-i] = o3, o2, o1, w3, w2, w1

        else:
            if p == "L":
                i = 0
                g = rotate(g, ro)
            else:
                i = 2
                b = rotate(b, ro)
            
            w1, w2, w3, r1, r2, r3 = w[0][i], w[1][i], w[2][i], r[0][i], r[1][i], r[2][i]
            y1, y2, y3, o1, o2, o3 = y[0][i], y[1][i], y[2][i], o[0][2-i], o[1][2-i], o[2][2-i]
            w[0][i], w[1][i], w[2][i], r[0][i], r[1][i], r[2][i] = o3, o2, o1, w1, w2, w3
            y[0][i], y[1][i], y[2][i], o[0][2-i], o[1][2-i], o[2][2-i] = r1, r2, r3, y3, y2, y1

N = int(input())
for i in range(N):
    #큰 N마다 리셋인 점
    w = [["w"] * 3 for i in range(3)]
    y = [["y"] * 3 for i in range(3)]
    r = [["r"] * 3 for i in range(3)]
    o = [["o"] * 3 for i in range(3)]
    g = [["g"] * 3 for i in range(3)]
    b = [["b"] * 3 for i in range(3)]
    
    n = int(input())
    orders = input().split()
    
    for order in orders:
        #rotation(order)
        #p, di = list(order)
        #rotate(p, di)
        p, di = list(order)
        rotation(p, di)
    for i in range(3):
        print(''.join(w[i]))
