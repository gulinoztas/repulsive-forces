import numpy as np
import math
from pyroots import Brentq
from random import random
#from variables import *
#import interval
import variables
from random import *
class rsab():
    def __init__(self, num_var, num_const,lowerlimit,upperlimit,set_size,textboxiterations):
        self.num_var = num_var
        self.num_const = num_const
        self.lowerlimit = lowerlimit
        self.upperlimit = upperlimit
        self.set_size = set_size
        self.textboxiterations = textboxiterations
    def const(self): #generates list of constraints
        global constraint
        constraint = []
        global lowerlimit, upperlimit,num_var,num_const,subject_to_const
        if len(variables.lowerlimit)>0 and len(variables.upperlimit)>0:
            for j in range(1, self.num_var + 1):
                if j<10:
                    constraint.append(["x0" + str(j), ">=", self.lowerlimit[j - 1]])
                    constraint.append(["x0" + str(j), "<=", self.upperlimit[j - 1]])
                else:
                    constraint.append(["x" + str(j), ">=", self.lowerlimit[j - 1]])
                    constraint.append(["x" + str(j), "<=", self.upperlimit[j - 1]])
        if variables.subject_to_const>0:
            for i in range(0,variables.subject_to_const):
                constraint.append(variables.constrained[i])
        return constraint
    def const2(self): #generates list of constraints
        global constraint
        constraint = []
        global lowerlimit, upperlimit,num_var,num_const,subject_to_const
        if len(variables.lowerlimit)>0 and len(variables.upperlimit)>0:
            for j in range(1, self.num_var + 1):
                if j<10:
                    constraint.append(["x0" + str(j), ">=", self.lowerlimit[j - 1]])
                    constraint.append(["x0" + str(j), "<=", self.upperlimit[j - 1]])
                else:
                    constraint.append(["x" + str(j), ">=", self.lowerlimit[j - 1]])
                    constraint.append(["x" + str(j), "<=", self.upperlimit[j - 1]])
        if variables.subject_to_const>0:
            for i in range(0,variables.subject_to_const):
                constraint.append(variables.constrained2[i])
        return constraint
    def strVars(self): #generates list of variables
        global strVars
        strVars = []
        for i in range(1, self.num_var + 1):
            if i < 10:
                strVars.append("x0" + str(i))
            else:
                strVars.append("x" + str(i))
        return strVars
    def find_upper_limit(self, sign, st, VarInterval, j, k): #finds upper limit
        if j < variables.num_bound:
            for i in range(0, self.num_var):
                if rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i] in st:
                    if i == k:
                        st = st.replace(rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).strVars()[i], "x")
                    elif sign == ">=":
                        st = st.replace(rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).strVars()[i],str(0.000000000000001+ min((VarInterval[i, 0]),abs(rsab(self.num_var, self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).const()[j][2]))))
                    else:
                        st = st.replace(rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).strVars()[i],str(0.000000000000001 + min((VarInterval[i, 0]),rsab(self.num_var, self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).const()[j][2])))
            st = st + "-" + str(abs(rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).const()[j][2]))
        else:
            for i in range(0, self.num_var):
                if rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i] in st:
                    if i == k:
                        st = st.replace(rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i], "x")
                    else:
                        #st = st
                        if variables.chg==True:
                            st = st.replace(rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i], str((VarInterval[i, 1])))
                        else:
                            st = st.replace(rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i], str((VarInterval[i, 0])))

                        #st = st.replace(rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).strVars()[i],str((VarInterval[i, 0])))
            st = st + "-" + str(abs(rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).const()[j][2]))
        return st
    def find_lower_limit(self,sign, st, VarInterval, j, k): #find lower limit
        if j < variables.num_bound:
            for i in range(0, self.num_var):
                if rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i] in st:
                    if i == k:
                        st = st.replace(rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i], "x")
                    else:
                        st = st.replace(rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i], str(0.000000000000001 + min((VarInterval[i, 0]), abs((rsab(self.num_var, self.num_const,self.lowerlimit, self.upperlimit,self.set_size,self.textboxiterations).const()[j][2])))))
                        #st = st.replace(rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i], str(0.000000000000001 + min((VarInterval[i, 0]), abs((rsab(self.num_var, self.num_const,self.lowerlimit, self.upperlimit,self.set_size,self.textboxiterations).const()[j][2])))))
            st = st + "-" + str(abs((rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).const()[j][2])))
        else:
            for i in range(0, self.num_var):
                if rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i] in st:
                    if i == k:
                        st = st.replace(rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i], "x")
                    else:
                        #st = st.replace(rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i], str(0.000000000000001 + min((VarInterval[i, 1]), abs((rsab(self.num_var, self.num_const,self.lowerlimit, self.upperlimit,self.set_size,self.textboxiterations).const()[j][2])))))  #deneme 13/11/2020
                        st = st.replace(rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).strVars()[i], str(VarInterval[i,1]))  #
            st = st + "-" + str(abs((rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).const()[j][2])))
        return st
    def brentroot(self, st, VarInterval,k): #finds root of the function
        f = lambda x: eval(st)
        brent = Brentq(epsilon=1e-3)  #pressure
        if "**" in st:  #himmelblau
            tempResult = brent(f, -0, 1e+30)
        else:
            tempResult = brent(f, -1e+30, 1e+30)
        if tempResult == None:
            result = 0
        else:
            result = float(tempResult.x0)
        return result
    def find_coefficient(self,st, k, sign): #finds the coefficient of a variable in a function
        for i in range(0, self.num_var):
            if i == k:
                st = st.replace(rsab(self.num_var, self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).strVars()[i], "1")
            else:
                if sign == ">=":
                    st = st.replace(rsab(self.num_var, self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).strVars()[i], "0")
                elif sign == "<=":
                    st = st.replace(rsab(self.num_var, self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).strVars()[i], "0")
                else:
                    st = st.replace(rsab(self.num_var, self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).strVars()[i], "0")
        find_coeff = eval(st)
        return find_coeff
    """----------------------BENCHMARKS----------------------"""
    def heat(self,x):
        cum1 = 0
        for j in range(0, 3):
            cum1 = cum1 + (x[j])
        objVal = cum1
        return objVal
    def dejongf1(self,x):
        cum1=0
        for j in range(0, self.num_var):
            cum1 = cum1 + (x[j]) * (x[j])
        objVal = cum1
        return objVal
    def step2(self,x):
        cum1=0
        for j in range(0, self.num_var):
            cum1 = cum1 + math.floor(abs(x[j]+0.5))**2
        objVal = cum1
        return objVal
    def quartic(self,x):
        cum1 = 0
        for j in range(0,self.num_var):
            cum1 = cum1 + (j+1)*x[j]**4
        objVal = cum1
        return objVal
    def hyperellipsoid(self,x):
        cum1 = 0
        for j in range(0,self.num_var):
            cum1 = cum1 + (j+1)*x[j]**2
        objVal = cum1
        return objVal
    def ackley(self,x):
        cum1 = 0
        cum2 = 0
        for j in range(0,self.num_var):
            cum1 = cum1 + x[j] * x[j]
            cum2 = cum2 + math.cos(2*math.pi*x[j])
        objVal = 20+(math.e**1)-20*math.e**((-0.20)*math.sqrt((1/self.num_var)*cum1))-math.e**((1/self.num_var)*cum2)
        return objVal
    def dixonprice(self,x):
        cum1 = 0
        for j in range(1,self.num_var):
            cum1 = cum1 + (j)*(2*(x[j])**2-x[j-1])**2
        objVal = (x[0]-1)**2+cum1
        return objVal
    def rastrigin(self,x):
        cum1 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + (x[j] * x[j] - 10 * math.cos(2 * 3.14 * x[j]) + 10)
        objVal = cum1
        return objVal
    def alpine(self,x):
        cum1 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + abs(x[j] * math.sin(x[j]) + 0.1 * x[j])
        objVal = cum1
        return objVal
    def exponential(self,x):
        cum1 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + x[j] * x[j]
        objVal = -2.71 ** (-0.5 * cum1)
        return objVal
    def cosine(self,x):
        cum1 = 0
        cum2 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + x[j] * x[j]
            cum2 = cum2 + math.cos(5 * math.pi * x[j])
        objVal = cum1 - 0.10 * cum2
        return objVal
    def griewank(self,x):
        cum1 = 0
        cum2 = 1
        for j in range(0, self.num_var):
            cum1 = cum1 + x[j] * x[j]#(x[j]) ** 2
            cum2 = cum2 * (math.cos((x[j]) / math.sqrt(j+1)))
        objVal = (cum1 / 4000) - cum2 + 1
        return objVal
    def egg(self,x):
        cum1 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + ((x[j] ** 2) + 25 * (math.sin(x[j])) ** 2)
        objVal = cum1
        return objVal
    def price2(self,x):
        cum1 = 0
        cum2 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + (math.sin(x[j])) ** 2
            cum2 = cum2 + -(x[j]) ** 2
        objVal = 1 + cum1 - 0.1 * math.e ** cum2
        return objVal
    def schaffer(self,x):
        cum1 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + x[j]*x[j]
        objVal = 0.5+(((math.sin(cum1**2))**2-0.5)/(1+0.001*cum1))
        return objVal
    def schaffer4(self,x,y):
        objVal = 0.5+(((math.cos(math.sin(abs(x**2-y**2))))**2-0.5)/(1+0.001*(x**2+y**2)**2))
        return objVal
    def schwefel12(self,x):
        cum1 = 0
        cum2 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + x[j]
            cum2 = cum2 + cum1 ** 2
        objVal = cum2
        return objVal
    def schwefel220(self,x):
        cum1 = 0
        for j in range(0,self.num_var):
            cum1 = cum1 + abs(x[j])
        objVal = cum1
        return objVal
    def schwefel221(self,x):
        objVal = max(abs(x))
        return objVal
    def schwefel222(self,x):
        cum1 = 0
        cum2 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + abs(x[j])
            cum2 = cum2 * abs(x[j])
        objVal = cum1 + cum2
        return objVal
    def schwefel226(self,x):
        cum1 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + ((x[j])*math.sin(math.sqrt(abs(x[j]))))
        objVal =  -cum1
        return objVal
    def xinsheyang(self,x):
        cum1 = 0
        cum2 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + abs(x[j])
            cum2 = cum2 + math.sin(x[j] ** 2)
        objVal = cum1 * math.e ** (-cum2)
        return objVal
    def guinta(self,x):
        cum1 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + math.sin((16 / 15) * x[j] - 1) + (math.sin((16 / 15) * x[j] - 1)) ** 2 + (1 / 50) * math.sin(4 * ((16 / 15) * x[j] - 1))
        objVal = 0.6 + cum1
        return objVal
    def becker(self,x):
        cum1=0
        for j in range(0,self.num_var):
            cum1 = cum1 + (abs(x[j])-5)**2
        objVal = cum1
        return objVal
    def rosenbrock(self,x):
        cum1 = 0
        for j in range(1,self.num_var):
            cum1 = cum1 + 100*(x[j]-(x[j-1])**2)**2 + (x[j-1]-1)**2
        objVal = cum1
        return objVal
    def elliptic(self,x):
        cum1 = 0
        for j in range(0,self.num_var):
            cum1 = cum1+ 10**(6*((j)/self.num_var-1))*(x[j]**2)
        objVal = cum1
        return objVal
    def michalewicz(self,x):
        cum1=0
        m=10
        for j in range(0,self.num_var):
            cum1 = cum1 + math.sin(x[j])*(math.sin(((j+1)*x[j]**2)/math.pi))**(2*m)
        objVal = -cum1
        return objVal
    def hartman(self,x):
        alpha = [1,1.2,3,3.2]
        A = [[3,10,30],[0.1,10,35],[3,10,30],[0.1,10,35]]
        P = [[3689*10**-4,1170*10**-4,2673*10**-4],[4699*10**-4,4387*10**-4,7470*10**-4],[1091*10**-4,8732*10**-4,5547*10**-4],[381*10**-4,5743*10**-4,8828*10**-4]]
        cum1 = 0
        cum2 = 0
        for i in range(0,4):
            cum1=0
            for j in range(0, self.num_var):
                cum1 = cum1 + A[i][j]*(x[j]-P[i][j])**2
            cum2 = cum2 + alpha[i] * math.e ** (-cum1)
        objVal = -cum2
        return objVal
    def pathological(self,x):
        cum1 = 0
        for j in range(0,self.num_var-1):
            #cum1 = cum1 + (math.sin(math.sqrt(100*(x[j+1]**2)+x[j]**2))**2-0.5)/(0.001*(x[j]-x[j+1])**4+0.50)
            cum1 = cum1 + 0.5 + ((math.sin(math.sqrt(100 * (x[j] ** 2) + x[j + 1] ** 2)) ** 2) - 0.5) / (1 + 0.001 * ((x[j] ** 2) - 2 * x[j] * x[j + 1] + (x[j + 1]) ** 2) ** 2)
        objVal = cum1
        return objVal
    def g_1(self,x):
        cum1 = 0
        cum2 = 0
        cum3 = 0
        for j in range(0, 4):
            cum1 = cum1+x[j]
            cum2 = cum2+x[j]**2
        for j in range(4,13):
            cum3 = cum3 + x[j]
        objVal = 5*cum1-5*cum2-cum3
        return objVal
    def g_2(self,x):
        cum1 = 0
        cum2 = 1
        cum3 = 0
        for j in range(0,variables.num_var):
            cum1 = cum1 + (math.cos(x[j]))**4
            cum2 = cum2 * (math.cos(x[j]))**2
            cum3 = cum3 + (j+1)*(x[j]**2)
        objVal = - abs((cum1-2*cum2)/cum3)
        return objVal
    def g_3(self,x):
        cum1 = 1
        for j in range(0,variables.num_var):
            cum1 = cum1 * x[j]
        objVal = -(math.sqrt(10))**10*cum1
        return objVal
    def zakharov(self,x):
        cum1 = 0
        cum2 = 0
        for j in range(0,self.num_var):
            cum1 = cum1 + x[j]**2
            cum2 = cum2 + 0.5*(j+1)*x[j]
        objVal = cum1+cum2**2+cum2**4
        return objVal
    def shubert(self,x):
        cum2 = 1
        for j in range(0,self.num_var):
            cum1 = 0
            for i in range(1,6):
                cum1 = cum1 + i*math.cos((i+1)*x[j]+i)
                #cum1 = cum1 + math.cos((i+1)*x[j]+i)
            cum2 = cum2*cum1
        objVal = cum2
        return objVal
    def weierstrass(self,x):
        cum1=0
        cum2 = 0
        cum3 = 0
        kmax = 20
        a = 0.5
        b=3
        for j in range(0,self.num_var):
            cum1 = 0
            cum2 = 0
            for k in range(0,kmax+1):
                cum1 = cum1 + (a**k)*math.cos(2*math.pi*(b**k)*(x[j]+0.5))
                cum2 = cum2 + self.num_var*(a**k)*math.cos(math.pi*(b**k))
            cum3 = cum3+cum1-cum2
        objVal = cum3
        return objVal
    def trid(self,x):
        cum1 = 0
        cum2 = 0
        for j in range(0,self.num_var):
            cum1 = cum1 + (x[j]-1)**2
        for j in range(0,self.num_var-1):
            cum2 = cum2 + x[j+1]*x[j]
        objVal = cum1-cum2
        return objVal
    def penalized(self,x):
        a=10
        k=100
        m=4
        cum1 = 0
        cum2 = 0
        for j in range(0,self.num_var-1):
            cum1 = cum1 + (((1+0.25*(x[j]+1))-1)**2)*(1+10*(math.sin(math.pi*(1+0.25*(x[j+1]+1))))**2)
        for j in range(0,self.num_var):
            if x[j] > a:
                cum2 = cum2 + k*(x[j]-a)**m
            elif -a<=x[j]<=a:
                cum2 = cum2 + 0
            else:
                cum2 = cum2 + k*(-x[j]-a)**m
        objVal = (math.pi/self.num_var)*10*(math.sin(math.pi*(1+0.25*(x[0]+1))))**2+cum1+((1+0.25*(x[self.num_var-1]+1))-1)**2+cum2
        return objVal
    def penalized2(self,x):
        a=5
        k=100
        m=4
        cum1 = 0
        cum2 = 0
        for j in range(0,self.num_var-1):
            cum1 = cum1 + ((x[j]-1)**2)*(1+(math.sin(3*math.pi*x[j+1]))**2)
        for j in range(0,self.num_var):
            if x[j] > a:
                cum2 = cum2 + k*(x[j]-a)**m
            elif -a<=x[j]<=a:
                cum2 = cum2 + 0
            else:
                cum2 = cum2 + k*(-x[j]-a)**m
        objVal = 0.1*(math.sin(3*math.pi*x[0]))**2+cum1+((x[self.num_var-1]-1)**2)*(1+(math.sin(2*math.pi*x[self.num_var-1]))**2)+cum2
        return objVal
    def langerman(self,x):
        m=5
        c = [1,2,5,2,3]
        A = [[3,5],[5,2],[2,1],[1,4],[7,9]]
        cum2 = 0
        for i in range(0, m):
            cum1 = 0
            for j in range(0, self.num_var):
                cum1 = cum1 + (x[j] - A[i][j]) ** 2
            cum2 = cum2 + c[i] * (math.e ** ((-1 / math.pi) * cum1)) * math.cos(math.pi * cum1)
        objVal = cum2
        return objVal
    def bird(self,x,y):
        objVal = math.sin(x) * math.e ** ((1 - math.cos(y)) ** 2) + math.cos(y) * math.e ** ((1 - math.sin(x)) ** 2) + (x - y) ** 2
        return objVal
    def easom(self,x,y):
        objVal = -math.cos(x)*math.cos(y)*math.e**(-(x-math.pi)**2-(y-math.pi)**2)
        return objVal
    def cb3(self,x,y):
        objVal = 2 * (x ** 2) - 1.05 * (x ** 4) + (1 / 6) * (x ** 6) + x * y + y ** 2
        return objVal
    def bohachevsky1(self,x,y):
        objVal = x ** 2 + 2 * y ** 2 - 0.3 * math.cos(3*math.pi * x) - 0.4* math.cos(4*math.pi * y) + 0.7
        return objVal
    def bohachevsky2(self,x,y):
        objVal = x ** 2 + 2 * y ** 2 - 0.3 * math.cos(3*math.pi * x) * math.cos(4*math.pi * y) + 0.3
        return objVal
    def bohachevsky3(self,x,y):
        objVal = x ** 2 + 2 * y ** 2 - 0.3 * math.cos(3*math.pi * x+4*math.pi * y) + 0.3
        return objVal
    def goldstein(self,x,y):
        objVal = (1 + ((x + y + 1) ** 2) * (19 - 14 * x + 3 * (x ** 2) - 14 * y + 6 * x * y + 3 * (y ** 2))) * (30 + ((2 * x - 3 * y) ** 2) * (18 - 32 * x + 12 * (x ** 2) + 48 * y - 36 * x * y + 27 * (y ** 2)))
        return objVal
    def paraboloid(self,x,y,z):
        objVal = 2 * x ** 2 + 10 * y ** 2 + 5 * z ** 2 + 6 * x * y - 2 * x * z + 4 * y * z - 6 * x - 14 * y - 2 * z + 6
        return objVal
    def branin(self,x,y):
        #objVal = (y - (5.1/(4*(math.pi**2))) * (x ** 2) + (5/math.pi) * x) ** 2 + 10*(1-(1/(8*math.pi))) * math.cos(x) + 10
        #objVal = (1/51.95)*((y - 0.1293 * (x ** 2) + 1.5924 * x) ** 2 + 9.602 * math.cos(x) - 44.81)
        a=1
        b=5.1/((2*math.pi)**2)
        c=5/math.pi
        r=6
        s=10
        t=1/(8*math.pi)
        objVal = a*(y-b*x**2+c*x-r)**2+s*(1-t)*math.cos(x)+s
        return objVal
    def beale(self,x,y):
        objVal = (1.5 - x + x * y) ** 2 + (2.25 - x + x * (y ** 2)) ** 2 + (2.625 - x + x * (y) ** 3) ** 2
        return objVal
    def mccormick(self,x,y):
        objVal = math.sin(x + y) + (x - y) ** 2 - (3 / 2) * x + (5 / 2) * y + 1
        return objVal
    def himmelblau(self,x,y):
        objVal = (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2
        return objVal
    def adjiman(self,x,y):
        objVal = math.cos(x) * math.sin(y) - x / (y ** 2 + 1)
        return objVal
    def aluffi(self,x,y):
        objVal = 0.25*(x**4)-0.5*(x**2)+0.10*(x)+0.5*(y**2)
        return objVal
    def camel(self,x,y):
        objVal = 4*(x**2)-2.1*(x**4)+(1/3)*(x**6)+x*y-4*(y**2)+4*(y**4)
        return objVal
    def dropwave(self,x,y):
        objVal = -((1+math.cos(12*math.sqrt(x**2+y**2)))/(0.5*(x**2+y**2)+2))
        return objVal
    def matyas(self,x,y):
        objVal = 0.26*(x**2+y**2)-0.48*x*y
        return objVal
    def booth(self,x,y):
        objVal = (x+2*y-7)**2+(2*x+y-5)**2
        return objVal
    def kowalik(self,x,y,z,t):
        a = [4,2,1,1/2,1/4,1/6,1/8,1/10,1/12,1/14,1/16]
        b = [0.1957,0.1947,0.1735,0.1600,0.0844,0.0627,0.0456,0.0342,0.0323,0.0235,0.0246]
        cum1 = 0
        for j in range(0,11):
            cum1 = cum1 + (b[j] - ((x * (a[j] ** 2 + a[j] * y)) / (a[j] ** 2 + a[j] * z + t))) ** 2
        objVal = cum1
        return objVal
    def colville(self,x,y,z,t):
        objVal = 100 * ((x ** 2 - y) ** 2) + ((x - 1) ** 2) + ((z - 1) ** 2) + 90 * ((z ** 2 - t) ** 2) + 10.1 * (((y - 1) ** 2) + (t - 1) ** 2) + 19.8 * (y - 1) * (t - 1)
        #objVal = ((100 * (x ** 2 - y)) ** 2) + ((1 - x) ** 2) + ((z - 1) ** 2) + 90 * ((t - (z ** 2)) ** 2) + ((1 - z) ** 2) + 10.1 * (((y - 1) ** 2) + (t - 1) ** 2) + 19.8 * (y - 1) * (t - 1)
        #objVal = (100 * (x ** 2 - y) ** 2) + ((x - 1) ** 2) + ((z - 1) ** 2) + 90 * (((z ** 2) - t) ** 2) + ((1 - y) ** 2) + 10.1 * (((y - 1) ** 2) + (t - 1) ** 2) + 19.8 * (y - 1) * (t - 1)
        #objVal = (100 * (x ** 2 - y) ** 2) + ((x - 1) ** 2) + ((z - 1) ** 2) + 90 * (((z ** 2) - t) ** 2) + ((1 - y) ** 2) + 10.1 * (((y - 1) ** 2) + (t - 1) ** 2) + 19.8 * (t - 1) / y
        #objVal = 100 * (x ** 2 - y) ** 2 + (x - 1) ** 2 + (z - 1) ** 2 + 90 * (z ** 2 - t) ** 2 + 10.1 * ((y - 1) ** 2 + (t - 1) ** 2) + 19.8 * ((y + 0.000000000000001) ** -1) * (t - 1)
        return objVal
    def pressure(self,x,y,z,t):
        objVal = 0.6224*x*z*t+1.7781*y*z**2+3.1661*x**2*t+19.84*x**2*z
        return objVal
    def weldedbeam(self,x,y,z,t):
        objVal = 1.10471*(x**2*y)+0.04811*z*t*(14+y)
        return objVal
    def himmel(self,x,y,z,t,s):
        objVal = 5.3578547*z**2+0.8356891*x*s+37.293239*x-40792.141
        return objVal
    def roscub(self,x,y):
        objVal = (1-x)**2+100*(y-x**2)**2
        return objVal
    def g_6(self,x,y):
        objVal = (x-10)**3+(y-20)**3
        return objVal
    def tension(self,x,y,z):
        objVal = (x**2*y*(z+2))
        return objVal
    def dispatch(self,x,y,z,t,u,v):
        objVal = 50*x+2650+14.5*y+0.0345*(y**2)+4.2*t+0.03*(t**2)+0.031*y*t+1250+36*z+0.0435*(z**2)+0.6*u+0.027*(u**2)+0.011*z*u+23.4*v
        return objVal
    def dispatch2(self,x,y,z,t,u,v,k,l):
        objVal = 254.8863+7.6997*x+0.0017*x**2+0.00011*x**3+1250+36*y+0.0435*(y**2)+0.6*u+0.027*(u**2)+0.011*y*u+2650+34.5*z+0.1035*z**2+2.203*v+0.025*v**2+0.051*z*v+1565+20*t+0.072*t**2+2.3*k+0.020*k**2+0.004*t*k+950+2.0109*l+0.038*l**2
        return objVal
    def speed_reducer(self,x,y,z,t,u,v,k):
        objVal = 0.7854*(y**2)*x*(14.9334*z-43.0934+3.3333*(z**2))+0.7854*(u*(k**2)+t*(v**2))-1.508*x*((k**2)+(v**2))+7.477*((k**3)+(v**3))
        return objVal
    def compressor(self,x,y,z,t):
        objVal = 861000*x**0.5*y*z**(-2/3)*t**(-0.5)+36900*z+772000000*x**(-1)*y**(0.219)-765430000*x**(-1)
        return objVal
    def refrigeration(self,x,y,z,t,u,v,k,l,m,n,o,p,r,s):
        objVal = 63098.88*y*t*p+5441.5*(y**2)*p+115055.5*(y**1.664)*v+6172.27*(y**2)*v+63098.88*x*z*o+5441.5*(x**2)*o+115055.5*(x**1.664)*u+6172.27*(x**2)*u+140.53*x*o+281.29*z*o+70.26*(x**2)+281.29*x*z+281.29*(z**2)+14437*(l**1.8812)*(p**0.3424)*n*(s**-1)*(x**2)*k*(m**-1)+20470.2*(k**2.893)*(o**0.316)*(x**2)
        return objVal
    def cantilever(self,x,y,z,t,u):
        objVal = 0.0624*(x+y+z+t+u)
        return objVal
    def call_function(self,name,x):
        if name=="dejongf1":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).dejongf1(x[0:self.num_var])
        elif name == "g_1":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).g_1(x[0:self.num_var])
        elif name == "g_2":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).g_2(x[0:self.num_var])
        elif name == "g_3":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).g_3(x[0:self.num_var])
        elif name == "step2":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).step2(x[0:self.num_var])
        elif name == "weldedbeam":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).weldedbeam(x[0], x[1], x[2], x[3])
        elif name == "heat":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).heat(x[0:self.num_var])
        elif name == "langerman":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).langerman(x[0:self.num_var])
        elif name == "weierstrass":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).weierstrass(x[0:self.num_var])
        elif name == "penalized":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).penalized(x[0:self.num_var])
        elif name == "penalized2":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).penalized2(x[0:self.num_var])
        elif name == "trid":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).trid(x[0:self.num_var])
        elif name == "shubert":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).shubert(x[0:self.num_var])
        elif name == "zakharov":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).zakharov(x[0:self.num_var])
        elif name == "pathological":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).pathological(x[0:self.num_var])
        elif name == "dixonprice":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).dixonprice(x[0:self.num_var])
        elif name == "quartic":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).quartic(x[0:self.num_var])
        elif name == "hyperellipsoid":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).hyperellipsoid(x[0:self.num_var])
        elif name =="ackley":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).ackley(x[0:self.num_var])
        elif name == "rastrigin":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).rastrigin(x[0:self.num_var])
        elif name =="alpine":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).alpine(x[0:self.num_var])
        elif name =="exponential":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).exponential(x[0:self.num_var])
        elif name =="cosine":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).cosine(x[0:self.num_var])
        elif name =="griewank":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).griewank(x[0:self.num_var])
        elif name =="egg":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).egg(x[0:self.num_var])
        elif name == "elliptic":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).elliptic(x[0:self.num_var])
        elif name =="price2":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).price2(x[0:self.num_var])
        elif name =="schaffer":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).schaffer(x[0:self.num_var])
        elif name =="schwefel12":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).schwefel12(x[0:self.num_var])
        elif name == "schwefel220":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).schwefel220(x[0:self.num_var])
        elif name == "schwefel221":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).schwefel221(x[0:self.num_var])
        elif name == "schwefel222":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).schwefel222(x[0:self.num_var])
        elif name == "schwefel226":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).schwefel226(x[0:self.num_var])
        elif name =="xinsheyang":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).xinsheyang(x[0:self.num_var])
        elif name =="guinta":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).guinta(x[0:self.num_var])
        elif name =="becker":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).becker(x[0:self.num_var])
        elif name =="rosenbrock":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).rosenbrock(x[0:self.num_var])
        elif name =="michalewicz":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).michalewicz(x[0:self.num_var])
        elif name =="hartman":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).hartman(x[0:self.num_var])

        elif name == "booth":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).booth(x[0], x[1])
        elif name == "matyas":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).matyas(x[0], x[1])
        elif name =="bird":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).bird(x[0],x[1])
        elif name =="cb3":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).cb3(x[0],x[1])
        elif name == "bohachevsky1":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).bohachevsky1(x[0], x[1])
        elif name =="bohachevsky2":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).bohachevsky2(x[0],x[1])
        elif name == "bohachevsky3":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).bohachevsky3(x[0], x[1])
        elif name =="paraboloid":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).paraboloid(x[0],x[1],x[2])
        elif name =="branin":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).branin(x[0],x[1])
        elif name =="beale":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).beale(x[0],x[1])
        elif name =="mccormick":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).mccormick(x[0],x[1])
        elif name =="himmelblau":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).himmelblau(x[0],x[1])
        elif name =="adjiman":
            return rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations).adjiman(x[0],x[1])
        elif name == "aluffi":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).aluffi(x[0], x[1])
        elif name == "camel":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).camel(x[0], x[1])
        elif name == "goldstein":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).goldstein(x[0], x[1])
        elif name == "easom":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).easom(x[0], x[1])
        elif name == "dropwave":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).dropwave(x[0], x[1])
        elif name == "kowalik":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).kowalik(x[0], x[1],x[2],x[3])
        elif name == "colville":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).colville(x[0], x[1], x[2], x[3])
        elif name == "schaffer4":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).schaffer4(x[0], x[1])
        elif name == "pressure":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).pressure(x[0], x[1], x[2], x[3])
        elif name == "himmel":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).himmel(x[0], x[1], x[2], x[3],x[4])
        elif name == "roscub":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).roscub(x[0], x[1])
        elif name == "g_6":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).g_6(x[0], x[1])
        elif name == "tension":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).tension(x[0], x[1],x[2])
        elif name == "dispatch":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).dispatch(x[0], x[1],x[2],x[3], x[4],x[5])
        elif name == "dispatch2":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).dispatch2(x[0], x[1],x[2],x[3], x[4],x[5], x[6],x[7])
        elif name == "compressor":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).compressor(x[0], x[1], x[2], x[3])
        elif name == "refrigeration":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).refrigeration(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9],x[10],x[11],x[12],x[13])
        elif name == "cantilever":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).cantilever(x[0], x[1], x[2], x[3], x[4])
        elif name == "speed_reducer":
            return rsab(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.set_size,self.textboxiterations).speed_reducer(x[0], x[1], x[2], x[3], x[4], x[5], x[6])

        else:
            return "Tanımlanmamış fonksiyon girdiniz. Lütfen tekrar deneyin veya fonksiyonu tanımlayın."
    """----------------------------------------------------"""
    def generate(self,var,CurrentInterval): #generates random numbers
        if variables.update == 1:
            rndCategoryLow = float(CurrentInterval[1][var])
            rndCategoryUp = float(CurrentInterval[2][var])
        else:
            rndCategoryLow = float(CurrentInterval[var][1])
            rndCategoryUp = float(CurrentInterval[var][2])
        k = randint(1, 4)
        IntegerVars = False
        x = random()
        if k == 1:
            myRandomVal = ((rndCategoryUp - rndCategoryLow) / 4) * x + rndCategoryLow
        elif k == 2:
            myRandomVal = ((rndCategoryUp - rndCategoryLow) / 4) * x + (rndCategoryUp - rndCategoryLow) / 4 + rndCategoryLow
        elif k == 3:
            myRandomVal = ((rndCategoryUp - rndCategoryLow) / 4) * x + 2 * (rndCategoryUp - rndCategoryLow) / 4 + rndCategoryLow
        else:
            myRandomVal = ((rndCategoryUp - rndCategoryLow) / 4) * x + 3 * (rndCategoryUp - rndCategoryLow) / 4 + rndCategoryLow
        if variables.function=="pressure":
            if var < 2:
                myRandomVal = myRandomVal - (myRandomVal % 0.0625)   #pressure vessel için
        if IntegerVars == False:
            myRandomVal = "{:02.3f}".format(myRandomVal)
        else:
            myRandomVal = int(myRandomVal)
        return float(myRandomVal)
    def strToformula(self,st,strVars,CurrentSolution): #replaces variable with candidate solution
        for j in range(0, self.num_var):
            st = st.replace(strVars[j], str(0.000000000000001 + CurrentSolution[j]))
        return eval(st)
    def Goal(self,objVal,constraintSatisfiedRate,maxDeviatedConst,item1,item2,item3): #calculates the fitness value
        variables.hitObj += 1
        CurrentWeight1 = item1
        CurrentWeight2 = item2
        CurrentWeight3 = item3
        goalSign = 1 if objVal>=0  else -1
        objective = "Min"
        if objective == "Min":
            goal1 = 1 / ((constraintSatisfiedRate) ** (1 + CurrentWeight2)+1e-100)
            if goalSign == -1:
                goal1 = 1 / goal1
            if abs(((goalSign * maxDeviatedConst) * (1 + CurrentWeight3)))+1e-30<200:#abs(maxDeviatedConst) < 200:
                goal2 = 1 /(math.exp(((goalSign * maxDeviatedConst) * (1 + CurrentWeight3)))+1e-100)
            else:
                goal2 = 1.0E+100
            goal3 = (abs(objVal + 0.000000000000001) ** (CurrentWeight1+0.05)) #0.05 for 3rd article
            Goall = goalSign * goal1 * goal2 * goal3
        else:
            goal1 = (constraintSatisfiedRate + 1.0E-100) ** (1 + CurrentWeight2)
            if goalSign == -1:
                goal1 = 1 / goal1
            if abs(maxDeviatedConst) < 200:
                goal2 = (math.exp(((goalSign) * maxDeviatedConst) * (1 + CurrentWeight3)))
            else:
                goal2 = -1.0E+100
            goal3 = abs(objVal) ** (CurrentWeight1)
            Goall = goalSign * goal1 * goal2 * goal3
        return Goall
    def UpdateBest(self,i,myGoal): #updates best-so-far solution
        ImpYes = False
        if len(variables.holdBest)==0:
            for item in range(0, self.num_var + 5):
                if variables.objective == "Min":
                    variables.holdBest[item] = variables.MaxValue
                else:
                    variables.holdBest[item] = variables.MinValue
        variables.trainSet[i, self.num_var] = myGoal
        if variables.objective == "Min":
            if variables.holdBest[self.num_var + 4] > myGoal:
                ImpYes = True
        else:
            if variables.holdBest[self.num_var + 4] < myGoal:
                ImpYes = True
        if ImpYes == True:
            bestOrderId = i + 1
            bestGoalValue = myGoal
            bestObjVal = variables.tmpObjVal#variables.objVal
            TotalError = variables.maxDeviatedConst
            for j in range(0, self.num_var):
                variables.holdBest[j] = variables.trainSet[i, j]
                variables.CurrentInterval[j][3] = variables.trainSet[i, j]
            variables.holdBest[self.num_var] = bestOrderId
            variables.holdBest[self.num_var + 1] = bestObjVal
            variables.holdBest[self.num_var + 2] = variables.constraintSatisfiedRate
            variables.holdBest[self.num_var + 3] = TotalError
            variables.holdBest[self.num_var + 4] = bestGoalValue
    def CalculateGoal(self,i,constraintSatisfiedRate,maxDeviatedConst,objVal,CurrentInterval,holdBest,previousBest,trainSet,item1,item2,item3):
        ImpYes = False
        ref = rsab(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.set_size,self.textboxiterations)
        CalculateGoal = ref.Goal(objVal, constraintSatisfiedRate, maxDeviatedConst,item1,item2,item3)
        trainSet[i, self.num_var] = CalculateGoal
        if variables.objective == "Min":
            if holdBest[self.num_var + 4] > CalculateGoal:
                ImpYes = True
        else:
            if holdBest[self.num_var + 4] < CalculateGoal:
                ImpYes = True
        if ImpYes == True:
            bestOrderId = i + 1
            bestGoalValue = CalculateGoal
            bestObjVal = objVal
            TotalError = maxDeviatedConst
            for j in range(0, self.num_var):
                previousBest[j] = holdBest[j]
                holdBest[j] = trainSet[i, j]
                CurrentInterval[j][3] = trainSet[i, j]
                #delta[j] = holdBest[j] - previousBest[j]
            previousBest[self.num_var] = holdBest[self.num_var]
            previousBest[self.num_var + 1] = holdBest[self.num_var + 1]
            previousBest[self.num_var + 2] = holdBest[self.num_var + 2]
            previousBest[self.num_var + 3] = holdBest[self.num_var + 3]
            previousBest[self.num_var + 4] = holdBest[self.num_var + 4]
            previousBest[self.num_var + 5] = holdBest[self.num_var + 5]
            holdBest[self.num_var] = bestOrderId
            holdBest[self.num_var + 1] = bestObjVal
            holdBest[self.num_var + 2] = constraintSatisfiedRate
            holdBest[self.num_var + 3] = TotalError
            holdBest[self.num_var + 4] = bestGoalValue
            holdBest[self.num_var + 5] = self.set_size
        return CalculateGoal
    def update_interval(self,CurrentInterval,uni_low,uni_up,holdBest,current):
        for k in range(0, self.num_var):
            randInterval_lower = float(uniform(uni_low, uni_up) * (holdBest[k] - float(CurrentInterval[k][1])))*2
            randInterval_upper = float(uniform(uni_low, uni_up) * (float(CurrentInterval[k][2]) - holdBest[k]))*2
            if  float(CurrentInterval[k][1])<=(holdBest[k] - randInterval_lower - self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3])) < float(CurrentInterval[k][2]):
                CurrentInterval[k][1] = (((holdBest[k]) - randInterval_lower - self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3])))
            else:
                CurrentInterval[k][1] = CurrentInterval[k][1]
            if float(CurrentInterval[k][1])<((holdBest[k]) + randInterval_upper + self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3])) <= float(CurrentInterval[k][2]):
                CurrentInterval[k][2] = (((holdBest[k]) + randInterval_upper + self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3])))
            else:
                CurrentInterval[k][2] =CurrentInterval[k][2]
        return CurrentInterval
    def update_interval2(self,CurrentInterval,uni_low,uni_up,current,holdBest):
        for k in range(0, self.num_var):
            randInterval_lower = float(uniform(uni_low, uni_up) * (holdBest[k] - float(CurrentInterval[k][1])))/2
            randInterval_upper = float(uniform(uni_low, uni_up) * (float(CurrentInterval[k][2]) - holdBest[k]))/2
            if float(CurrentInterval[k][1])< (current[k]-randInterval_lower - self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3])) < float(CurrentInterval[k][2]) :
                CurrentInterval[k][1] = (current[k]-randInterval_lower - self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3]))
            else:
                CurrentInterval[k][1] = CurrentInterval[k][1]
            if float(CurrentInterval[k][1])<(current[k]+randInterval_upper + self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3])) < float(CurrentInterval[k][2]) :
                CurrentInterval[k][2] = (current[k]+randInterval_upper + self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3]))
            else:
                CurrentInterval[k][2] = CurrentInterval[k][2]
        return CurrentInterval
    def update_interval3(self,CurrentInterval,holdBest): #updates interval according to the midpoint
        for k in range(0, self.num_var):
            domain = float(CurrentInterval[2][k]) - float(CurrentInterval[1][k])
            ave = (domain/2)+float(CurrentInterval[1][k])
            randInterval = random()*(domain)
            if holdBest[k]< ave:#domain/2 :
                if float(CurrentInterval[1][k]) < ave < float(CurrentInterval[2][k]):
                    CurrentInterval[1][k] = float(CurrentInterval[1][k])
                    CurrentInterval[2][k] = ave
                else:
                    CurrentInterval[1][k] = float(CurrentInterval[1][k])
                    CurrentInterval[2][k] = float(CurrentInterval[2][k])
            else:
                if float(CurrentInterval[1][k]) < ave < float(CurrentInterval[2][k]):
                    CurrentInterval[1][k] = ave
                    CurrentInterval[2][k] = float(CurrentInterval[2][k])
                else:
                    CurrentInterval[1][k] = float(CurrentInterval[1][k])
                    CurrentInterval[2][k] = float(CurrentInterval[2][k])
        return CurrentInterval
    def update_interval4(self,CurrentInterval,previousInterval,t):
        for k in range(0, self.num_var):
            previous_range = float(previousInterval[k][2]) - float(previousInterval[k][1])
            current_range = float(CurrentInterval[k][2]) - float(CurrentInterval[k][1])
            if previous_range>current_range:
                CurrentInterval[k][1] = float(previousInterval[k][1])
                CurrentInterval[k][2] = float(previousInterval[k][2])
            else:
                if t==1:
                    CurrentInterval[k][1] = float(CurrentInterval[k][1])
                    CurrentInterval[k][2] = float(CurrentInterval[k][2])
                else:
                    CurrentInterval[k][1] = float(variables.bestInterval[k][1])
                    CurrentInterval[k][2] = float(variables.bestInterval[k][2])
        return CurrentInterval
    def update_interval5(self,CurrentInterval,holdBest): #updates interval according to the best-s0-far solution
        for k in range(0, self.num_var):
            ul=float(CurrentInterval[2][k])-holdBest[k]
            ll=holdBest[k]-float(CurrentInterval[1][k])
            if ul>ll:
                CurrentInterval[1][k] = float(CurrentInterval[1][k])
                CurrentInterval[2][k] = holdBest[k]+ll
            else:
                CurrentInterval[1][k] = holdBest[k]-ul
                CurrentInterval[2][k] = float(CurrentInterval[2][k])
        return CurrentInterval
    def improve_interval(self,database,CurrentInterval,best_so_far):
        for i in range(0, self.num_var):
            randInterval = float("{:05.3f}".format((0.21*math.log10(random()+0.009)+1)))
            if float(CurrentInterval[i][1])<database[best_so_far,i]-randInterval-variables.num_const*(1-database[best_so_far,variables.num_var+1])*database[best_so_far,variables.num_var+2]< float(CurrentInterval[i][2]):
                CurrentInterval[i][1] = database[best_so_far,i]-randInterval-variables.num_const*(1-database[best_so_far,variables.num_var+1])*database[best_so_far,variables.num_var+2]
            else:
                CurrentInterval[i][1] = float(CurrentInterval[i][1])
            if float(CurrentInterval[i][1])<database[best_so_far,i]+randInterval+variables.num_const*(1-database[best_so_far,variables.num_var+1])*database[best_so_far,variables.num_var+2]< float(CurrentInterval[i][2]):
                CurrentInterval[i][2] = database[best_so_far,i]+randInterval+variables.num_const*(1-database[best_so_far,variables.num_var+1])*database[best_so_far,variables.num_var+2]
            else:
                CurrentInterval[i][2] = float(CurrentInterval[i][2])
            CurrentInterval[i][3] = database[best_so_far,i]
        return CurrentInterval
    def improve_interval2(self,bestpos,CurrentInterval,gbest): #updates interval for duplicated particles
        for i in range(0, self.num_var):
            r = (float(CurrentInterval[i][2]) - float(CurrentInterval[i][1]))
            randInterval = float("{:05.3f}".format((0.21*math.log10(random()+0.009)+1)))*bestpos[gbest,i]   #21/04 tez için deneniyor.
            if float(CurrentInterval[i][1])<bestpos[gbest,i]-randInterval< float(CurrentInterval[i][2]):
                CurrentInterval[i][1] = bestpos[gbest,i]-randInterval
            else:
                CurrentInterval[i][1] = float(CurrentInterval[i][1])
            if float(CurrentInterval[i][1])<bestpos[gbest,i]+randInterval< float(CurrentInterval[i][2]):
                CurrentInterval[i][2] = bestpos[gbest,i]+randInterval
            else:
                CurrentInterval[i][2] = float(CurrentInterval[i][2])
            CurrentInterval[i][3] = bestpos[gbest,i]
        return CurrentInterval

