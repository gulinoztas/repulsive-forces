import numpy as np
def Find_brentroot(Var,a,b,eps,Err):   #Str, VarInterval(k, 0), VarInterval(k, 1), 0.0001, 0
    Err = 0
    steps = 0
    MaxValue = 1.7976931348623157E+308
    """
    num_var = 5
    num_constraints = 10
    constraints = np.array(())
    constraints = np. array ( [["x1 <= 8"], ["x1 >= -8"], ["x2 <= 8"], ["x2 >= -8"], ["x3 <= 8"], ["x3 >= -8"], ["x4 <= 8"], ["x4 >= -8"], ["x5 <= 8"], ["x5 >= -8"]] ) .reshape( 10, 1 )
    
    VarInterval = np.array((num_var + 1, 2))
    
    for i in range(0, num_var):
        VarInterval[i, 0] = 0
        VarInterval[i, 1] = 2147483647
    

    for j in range(0, num_constraints):
        st = constraints[j, 0].split(" ", -1)  # constraintlerin boyutlandılmış hali
        Var = st[0]  # yalnızca değişkenler
        splitVar = Var.split("-", -1)  # eksi işaretli değişkenleri ayrıştırır.
        Vars = Var + "-" + str(abs(float(st[2])))  # Str = Str + "-" + System.Math.Abs(CDbl(Constraint(j)(2))).ToString
    """
    #Var = "(x+3)*(x-1)**2"
    #a = -4
    #b = 4 / 3
    #a = 0  #VarInterval[i, 0]   -4    bunlar nereden gelecek ???
    #b = 2147483647 #VarInterval[i, 1]   4 / 3
    ya = float(eval(Var.replace("x", str(a+1.0E-50))))
    yb = float(eval(Var.replace("x", str(b))))
    c=float()
    d=float()
    s=float()
    #print(ya)
    #print(yb)

    if abs(ya) <= abs(yb):
        a, b = b, a
        ya, yb = yb, ya

    c = a
    yc = ya

    mflag = True

    while yb > 0 or abs(b - a) >= 0:  # EPS NE OLA Kİ?
        if ya == 0:
            ya = 0.000000000000001
        elif yb == 0:
            yb = 0.0000000000000001
        elif yc == 0:
            yc = 1.0E-17
        elif ya != yc and yb != yc:
            s = (a * yb * yc) / (ya - yb) * (ya - yc) + (b * ya * yc) / ((yb - ya) * (yb - yc)) + (c * ya * yb) / ((yc - ya) * (yc - yb))
        else:
            s = b - (yb * (b - a)) / (yb - ya)

        if (not (((3 * a + b) / 4 <= s) & (s <= b))) | ((mflag == True) & (abs(s - b) >= (abs(b - c) / 2))) | ((mflag == False) & (abs(s - b) >= ((c -d) / 2))):
            s = (a + b) / 2
            mflag = True
        else:
            mflag = False

        ys = eval(Var.replace("x",str(s)))  # j indisledim çünkü her kısıttaki değişken için yapmalı..
        d = c
        c = b
        yc = yb


        if ya * ys < 0:
            b = s
            yb = ys
        else:
            a = s
            ya = ys

        if abs(ya) < abs(yb):
            a, b = b, a
            ya, yb = yb, ya

        steps += 1

        if steps == 1000:
            MaxValue
        break

    #print(b)
        tempResult = b

