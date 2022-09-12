from math import sqrt

g = 7 * 10 ** (-11)

x, y= list(), list()

def xytoa(x0, y0, m1, m2):
    d = sqrt(x0 ** 2+y0 ** 2)
    G = g * m1 * m2 / (d ** 2)
    Gx, Gy = G * (-x0) / d, G * (-y0) / d
    print("Gx,Gy:",Gx," ",Gy)
    
    ax, ay = Gx/m2, Gy/m2
    return ax, ay

def major(limit = 10 ** 7, x0 = 5 * 10 ** 10, y0 = 0, vx0 = 0, vy0 = 57361, m1 = 2 * 10 ** 30, m2 = 3 * 10 ** 23):
    x.append(x0)
    y.append(y0)
    vx,vy = vx0,vy0
    
    for times in range (limit):
        ax, ay = xytoa(x[-1], y[-1], m1, m2)
        print("ax, ay: ", ax, " ", ay)
      
        vx0, vy0 = vx, vy
        vx = vx + ax
        vy = vy + ay
        print("vx, vy: ", vx, " ", vy)
        
        x.append(x[-1] + vx / 2 + vx0 / 2)
        y.append(y[-1] + vy / 2 + vy0 / 2)
        print("x, y: ", x[-1], " ", y[-1])

    return x, y

def outputOctave(x, y, path = "outputOctave.m"):
    with open(path, "w") as file:
        file.write("plot(")
        file.write(str(x))
        file.write(",")
        file.write(str(y))
        file.write(")")

def output(x, y, path = "output"):
    with open(path,"w") as file:
        file.write(str(x))
        file.write(",")
        file.write(str(y))
