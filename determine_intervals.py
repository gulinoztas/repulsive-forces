import numpy as np
from pyroots import Brentq
from find_upper_limit import find_upper_limit
from find_lower_limit import find_lower_limit
from find_coefficient import find_coefficient

from f_val import f_val
import pandas as pd
from numpy.random import randn
import dataframe as df
import math

num_var = 4
#constraint = [["-5*x1+2*x2-3*x3","<=","8"], ["-3*x1+2*x2",">=","8"], ["x1+3*x2","<=","8"], ["x1+4*x2+5*x3",">=","-8"]]
#constraint = [["-x1*(-1)",">=","0.0625"]]
#constraint = ["-x1+0.0193*x2","<=","0"]
constraint = [["-x1+0.0193*x3","<=","0"], ["-x2+0.00954*x3","<=","0"],["3.14159265359*x3**2*x4+(4/3)*3.14159265359*x3**3",">=","1296000"], ["x4","<=","240"],["x1","<=","10"],["x2","<=","10"], ["x3","<=","100"],["x1",">=","0.0625"],["x2",">=","0.0625"]]
#constraint = [["x1","<=","2"],["x1","<=","8"],["x1","<=","5"]]
#print("cons", constraint[0][0])
#constraint = np.array([["x1+x2",">=","4"],["2*x1+3*x3","<=","5"]])
#strVars = ["x1","x2","x3","x4"]
strVars = ["x1","x2","x3","x4"]
#print("strvars",strVars[0])

#splitVar = np.array(5000)
VarInterval = np.zeros((num_var + 1, 2))
#print("zeros", VarInterval[0,0])
MaxValue = 1.7976931348623157E+308
num_constraints = 9

myDataTableIntervals = np.array(())
lowerlimit =np.array(())
upperlimit =np.array(())
x=str()


for i in range (0, num_var):
    VarInterval[i, 0] = 0
    VarInterval[i, 1] = 2147483647


for k in range(0, num_var):

    for j in range(0, num_constraints):
        st = constraint[j][0]  #str in vb yalnızca değişkenler
        splitVar = constraint[j][0].split("-", -1)  #eksi işaretli değişkenleri ayrıştırır.

        #print("mySplitvar",splitVar)
        #st = st + "-" + str(abs(float(constraint[j, 2])))  #değişkenlerden sağ yan değeri çıkarır.
        sign = constraint[j][1]
        rhs = constraint[j][2]
        print("my kısıt:", st)
        #print(splitVar[0]==st)


        if sign == "<=":
            if float(rhs) >= 0:
                if splitVar[0] == st:
                    """------------------FIND UPPER LIMIT FONKSİYONU-----------"""
                    #print("önce",VarInterval[k,1])
                    st=find_upper_limit(num_var, st, strVars, constraint, VarInterval, j, k)
                    #print("sonra",VarInterval[k,1])
                    print("ful_st",st)

                    """--------------------Find_BrenRoot-----------------"""

                    if "x" in st:
                        f = lambda x: eval(st)
                        brent = Brentq(epsilon=0.00000000000001)
                        tempResult = brent(f, VarInterval[k, 0], VarInterval[k, 1])
                        result = float(tempResult.x0)
                        print(tempResult)
                        print("st'de x varsa; root:ul geçici sonuç", result)
                    else:
                        result = float(eval(st))
                        print("st'de x yoksa;root: ul geçici sonuç:",result)

                    if result > 0:     #0a eşitse ne yapacak
                        if result > VarInterval[k, 0] or result < VarInterval[k, 1]:
                            VarInterval[k, 1] = result
                            print("upper limit",VarInterval[k,1])
                    result = 0

                else:
                    """------------FIND COEFFICIENT FONKSİYONU-------"""
                    find_coeff = find_coefficient(num_var, st, strVars, k, constraint, j)
                    print("coefficient:", find_coeff)
                    if find_coeff < 0:
                        """--------------SET LOWER LIMIT ZERO------------"""
                        VarInterval[k, 0] = 0
                        print("değişken ve katsayı negatif, Lower limit: ",VarInterval[k,0])

                        """-------------------------------------------------"""
                    else:
                        """--------FIND UPPER LIMIT FONKSİYONU-------------------"""

                        st=find_upper_limit(num_var, st, strVars, constraint, VarInterval, j, k)
                        print("katsayı pozitifse,ful_st", st)

                        """--------------------Find_BrenRoot-----------------"""

                        if "x" in st:
                            f = lambda x: eval(st)
                            brent = Brentq(epsilon=0.0000001)
                            tempResult = brent(f, VarInterval[k, 0], VarInterval[k, 1])
                            result = float(tempResult.x0)
                            print(tempResult)
                            print("st'de x varsa; root:ul geçici sonuç",result)
                        else:
                            result = float(eval(st))
                            print("st'de x yoksa; root:geçici sonuç",result)

                        if result > 0:
                            if result > VarInterval[k, 0] or result < VarInterval[k, 1]:
                                VarInterval[k, 1] = result
                                print("upper limit",VarInterval[k, 1])
                        result = 0
            else:
                if splitVar[0] == st:
                    """-------------SET LOWER LIMIT ZERO-----------------------"""
                    VarInterval[k, 0] = 0
                    print("rhs negatif,değişken pozitifse; lower limit",VarInterval[k,0])
                else:
                    """---------------FIND COEFFICIENT FONKSİYONU----------------"""
                    find_coeff = find_coefficient(num_var, st, strVars, k, constraint, j)
                    print("coefficient:", find_coeff)
                    if find_coeff < 0:
                        """----------------FIND LOWER LIMIT FONKSİYONU---------------"""

                        st=find_lower_limit(num_var,st, strVars, constraint, VarInterval, j, k)
                        print("ll st",st)
                        print("değişken negatif, coefficient negatifse; lower limit",VarInterval[k,0])
                        """----------FIND BRENT ROOT------------------"""
                        if "x" in st:
                            f = lambda x: eval(st)
                            brent = Brentq(epsilon=0.0000001)
                            tempResult = brent(f, VarInterval[k, 0], VarInterval[k, 1])
                            result = float(tempResult.x0)
                            print(tempResult)
                            print("st'de x varsa;root: geçici sonuç",result)
                        else:
                            result = float(eval(st))
                            print("st'de x yoksa;root: geçici sonuç",result)
                        """--------------------------------------"""
                        if result > 0:      #bunun eksi durumu yok???
                            if result >= VarInterval[k, 0] and result < VarInterval[k, 1]:   #aralık daralmış olmuyor sanki?
                                VarInterval[k, 0] = result
                                print("lower limit",VarInterval[k, 0])
                        result = 0

                        """--------------------------------------"""
                    else:
                        """------------SET LOWER LIMIT ZERO------------------------"""
                        VarInterval[k, 0] = 0
                        print("coefficient pozitif,rhs ve değişken negatif; lower limit",VarInterval[k,0])
                        """---------------------------------------------"""
        elif sign == ">=":
            if float(rhs) >=0:
                if splitVar[0] == st:
                    """-----------------SET LOWER LIMIT ZERO-----------------"""
                    #VarInterval[k, 0] = 0   #bunu alıyor direkt
                    #print("rhs ve değişken pozitif, lower limit",VarInterval[k,0])
                    """------------------find lower limit--------------------"""
                    st = find_lower_limit(num_var, st, strVars, constraint, VarInterval, j, k)
                    print("ll,st", st)
                    print("değişken işareti negatif,coefficient pozitif; lower limit:", VarInterval[k, 0])
                    """--------------find brent root-----------------"""
                    if "x" in st:
                        f = lambda x: eval(st)
                        brent = Brentq(epsilon=0.0000001)
                        tempResult = brent(f, VarInterval[k, 0], VarInterval[k, 1])
                        result = float(tempResult.x0)
                        print(tempResult)
                        print("st'de x varsa,root: geçici çözüm:", result)
                    else:
                        result = float(eval(st))
                        print("st'de x yoksa,root:geçici sonuç:", result)

                    """---------------------------------------------------"""
                    if result > 0:
                        if result >= VarInterval[k, 0] and result < VarInterval[k, 1]:
                            VarInterval[k, 0] = result
                            print("lower limit", VarInterval[k, 0])
                    result = 0

                    """---------------------------------------------"""

                else:
                    """--------------FIND COEFFICIENT FONKSİYONU-----------------"""
                    find_coeff = find_coefficient(num_var, st, strVars, k, constraint, j)
                    print("coefficient:", find_coeff)
                    if find_coeff < 0:

                        """---------set lower limit zero-----------"""
                        VarInterval[k, 0] = 0
                        print("değişken işareti ve coefficient negatif,lower limit", VarInterval[k, 0])

                        """---------------------------------------"""
                    else: #burda  burda da aynı durum var. değişken işareti ? katsayı negatifliği??
                        """----------find lower limit-------------"""
                        st=find_lower_limit(num_var, st, strVars, constraint, VarInterval, j, k)
                        print("ll,st",st)
                        print("değişken işareti negatif,coefficient pozitif; lower limit:", VarInterval[k, 0])
                        """--------------find brent root-----------------"""
                        if "x" in st:
                            f = lambda x: eval(st)
                            brent = Brentq(epsilon=0.0000001)
                            tempResult = brent(f, VarInterval[k, 0], VarInterval[k, 1])
                            result = float(tempResult.x0)
                            print(tempResult)
                            print("st'de x varsa,root: geçici çözüm:",result)
                        else:
                            result = float(eval(st))
                            print("st'de x yoksa,root:geçici sonuç:",result)

                        """---------------------------------------------------"""
                        if result > 0:
                            if result >= VarInterval[k, 0] and result < VarInterval[k, 1]:
                                VarInterval[k, 0] = result
                                print("lower limit",VarInterval[k, 0])
                        result = 0

            else:
                if splitVar[0] == st:
                    """-----------SET LOWER LIMIT ZERO--------------------"""
                    VarInterval[k, 0] = 0
                    print("rhs negatif,değişken pozitif; lower limit:",VarInterval[k,0])
                    """---------------------------------"""
                else:
                    """---------find coefficient-----------"""
                    find_coeff = find_coefficient(num_var, st, strVars, k, constraint, j)
                    print("coefficient:",find_coeff)
                    if find_coeff < 0:

                        if "-" in st:       #buraya da bakmalı
                            st=st.replace("-", "+")   #ilk değişkenin eksisini kaldırır. her - olan değişkeni + yapar. Başına da + koyar.
                            st=st[1:]
                            print("st",st)

                        """------------find upper limit-----------"""

                        st=find_upper_limit(num_var, st, strVars, constraint, VarInterval, j, k)  #fonksiyon değerindeki çıkarması için st'ye tanımladık.
                        print("find upper limit sonrası st",st)
                        #print("rhs, değişken işareti, coefficient negatif; upper limit:", VarInterval[k, 1])

                        """--------find brent root-------------"""
                        if "x" in st:
                            f = lambda x: eval(st)
                            brent = Brentq(epsilon=0.0000001)
                            tempResult = brent(f, VarInterval[k, 0], VarInterval[k, 1])
                            result = float(tempResult.x0)
                            print(tempResult)
                            print("st'de x varsa, root:geçici sonuç:",result)
                        else:
                            result = float(eval(st))
                            print("st'de x yoksa, root:geçici sonuç:",result)

                        """---------------------------------------------------"""
                        if result > 0:
                            if result > VarInterval[k, 0] or result < VarInterval[k, 1]:
                                VarInterval[k, 1] = result
                                print("upper limit",VarInterval[k, 1])
                        result = 0
                    else:
                        """------------set lower limit zero---------------"""
                        VarInterval[k, 0] = 0
                        print("lower limit:", VarInterval[k, 0])
        else:
            #print(sign)
            print("Hata oluştu!")


    lowerlimit = np.append(lowerlimit, VarInterval[k, 0])
    upperlimit = np.append(upperlimit,VarInterval[k, 1])
    myDataTableIntervals = [strVars,lowerlimit,upperlimit]
    #print("Intervals:",myDataTableIntervals)

for i in range(0,num_var):
    variable = strVars[i]
    lower = lowerlimit[i]
    upper = upperlimit[i]
    x=[variable,lower,upper]
    print(x)
    #myDataTable = pd.DataFrame(data=x, index=None,columns=["Variable", "Lower Bound", "Upper Bound"])





