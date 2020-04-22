import numpy as np
import math
from pyroots import Brentq
import pandas as pd
from random import *
from statistics import mean
from statistics import stdev
from scipy import stats
import time
import cProfile
import re
import pstats2
from pstats2 import *
import pyprof2calltree
from pyprof2calltree import visualize,convert
class initialize():
    def __init__(self, num_var, num_const,lowerlimit,upperlimit):
        self.num_var = num_var
        self.num_const = num_const
        self.lowerlimit = lowerlimit
        self.upperlimit = upperlimit
    def const(self):
        global constraint
        constraint = []
        global lowerlimit, upperlimit,num_var,num_const
        for j in range(1, self.num_var + 1):
            if j<10:
                constraint.append(["x0" + str(j), ">=", self.lowerlimit[j - 1]])
                constraint.append(["x0" + str(j), "<=", self.upperlimit[j - 1]])
            else:
                constraint.append(["x" + str(j), ">=", self.lowerlimit[j - 1]])
                constraint.append(["x" + str(j), "<=", self.upperlimit[j - 1]])
        return constraint
    def strVars(self):
        strVars = []
        for i in range(1, self.num_var + 1):
            if i < 10:
                strVars.append("x0" + str(i))
            else:
                strVars.append("x" + str(i))
        return strVars
    def find_upper_limit(self, sign, st, VarInterval, j, k):
        initialize(self.num_var,self.num_const,self.lowerlimit,self.upperlimit).const()
        for i in range(0, self.num_var):
            if i == k:
                st = st.replace(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).strVars()[i], "x")
                # print("x konulduğunda", st)
            elif sign == ">=":
                st = st.replace(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).strVars()[i],
                                min((str(0.000000000000001 + (VarInterval[i, 0]))),
                                    str(abs(float(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).const()[j][2])))))
                # print("upper kısıt", st)
            else:
                st = st.replace(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).strVars()[i],
                                min((str(0.000000000000001 + (VarInterval[i, 0]))),
                                    str(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).const()[j][2])))
                # print("upper2 kısıt", st)
        st = st + "-" + str(abs(float(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).const()[j][2])))
        return st
    def find_lower_limit(self, st, VarInterval, j, k):
        for i in range(0, self.num_var):
            if i == k:
                st = st.replace(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).strVars()[i], "x")
            else:
                st = st.replace(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).strVars()[i],max((str(0.000000000000001 + (VarInterval[i, 0]))), str(abs(float(initialize(self.num_var, self.num_const, self.lowerlimit,self.upperlimit).const()[j][2])))))
        st = st + "-" + str(abs(float(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).const()[j][2])))
        return st
    def brentroot(self, st, VarInterval,k):
        if "x" in st:
            f = lambda x: eval(st)
            brent = Brentq(epsilon=0.00000000000001)
            tempResult = brent(f, VarInterval[k, 0], VarInterval[k, 1])
            result = float(tempResult.x0)
        else:
            result = float(eval(st))
        return result
    def find_coefficient(self,st, k, sign):
        for i in range(0, self.num_var):
            if i == k:
                st = st.replace(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).strVars()[i], "1")
            else:
                if sign == ">=":
                    st = st.replace(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).strVars()[i], "0")
                elif st[1] == "<=":
                    st = st.replace(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).strVars()[i], "0")
                else:
                    st = st.replace(initialize(self.num_var, self.num_const,self.lowerlimit,self.upperlimit).strVars()[i], "0")
        find_coeff = eval(st)
        return find_coeff
    def dejongf1(self,x):
        cum1=0
        for j in range(0, self.num_var):
            cum1 = cum1 + x[j] * x[j]
        objVal = cum1
        return objVal
    def ackley(self,x):
        cum1 = 0
        cum2 = 0
        for j in range(0,self.num_var):
            cum1 = cum1 + x[j] * x[j]
            cum2 = cum2 + math.cos(2*math.pi*x[j])
        objVal = -20*(math.e**(-0.20*math.sqrt(0.20*cum1))-math.e**((1/self.num_var)*cum2))+20+math.e
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
        cum2 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + (x[j]) ** 2
            cum2 = cum2 * math.cos((x[j]) / math.sqrt(j))
        objVal = 1 + (1 / 4000) * cum1 - cum2
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
    def schwefel(self,x):
        cum1 = 0
        cum2 = 0
        for j in range(0, self.num_var):
            cum1 = cum1 + x[j]
            cum2 = cum2 + cum1 ** 2
        objVal = cum2
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
    def bird(self,x,y):
        objVal = math.sin(x) * math.e ** (1 - math.cos(y)) ** 2 + math.cos(y) * math.e ** (1 - math.sin(x)) ** 2 + (x - y) ** 2
        return objVal
    def cb3(self,x,y):
        objVal = 2 * (x ** 2) - 1.05 * (x ** 4) + (1 / 6) * (x ** 6) + x * y + y ** 2
        return objVal
    def bohachevsky2(self,x,y):
        objVal = x ** 2 + 2 * y ** 2 - 0.3 * math.cos(3*math.pi * x) * math.cos(4*math.pi * y) + 0.3
        return objVal
    def paraboloid(self,x,y,z):
        objVal = 2 * x ** 2 + 10 * y ** 2 + 5 * z ** 2 + 6 * x * y - 2 * x * z + 4 * y * z - 6 * x - 14 * y - 2 * z + 6
        return objVal
    def branin(self,x,y):
        #objVal = (y - (5.1/(4*(math.pi**2))) * (x ** 2) + (5/math.pi) * x) ** 2 + 10*(1-(1/(8*math.pi))) * math.cos(x) + 10
        objVal = (1/51.95)*((y - 0.1293 * (x ** 2) + 1.5924 * x) ** 2 + 9.602 * math.cos(x) - 44.81)
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
    def determine(self):
        global VarInterval, myDataTableIntervals,Interval,holdBest
        VarInterval = np.zeros((self.num_var, 2))
        myDataTableIntervals = np.array(())
        lowerlimitt = np.array(())
        upperlimitt = np.array(())
        ref = initialize(self.num_var, self.num_const, self.lowerlimit, self.upperlimit)

        for k in range(0, self.num_var):
            VarInterval[k, 0] = 0
            VarInterval[k, 1] = 2147483647
            itr = 0
            a = np.array(())
            lower = np.array(())
            upper = np.array(())
            for j in range(0, self.num_const):
                st = ref.const()[j][0]
                splitVar = ref.const()[j][0].split("-", -1)  # eksi işaretli değişkenleri ayrıştırır.
                sign = ref.const()[j][1]
                rhs = ref.const()[j][2]
                if sign == "<=":
                    if float(rhs) >= 0:
                        if splitVar[0] == st:
                            st = ref.find_upper_limit(sign, st, VarInterval, j, k)
                            result = ref.brentroot(st, VarInterval, k)
                            if result > 0:  # 0a eşitse ne yapacak
                                if result > VarInterval[k, 0] or result < VarInterval[k, 1]:
                                    VarInterval[k, 1] = result
                            result = 0
                        else:
                            find_coeff = ref.find_coefficient(st, k, sign)
                            if find_coeff < 0:
                                VarInterval[k, 0] = 0
                            else:
                                st = ref.find_upper_limit(sign, st, VarInterval, j, k)
                                result = ref.brentroot(st, VarInterval, k)
                                if result > 0:  # 0a eşitse ne yapacak
                                    if result > VarInterval[k, 0] or result < VarInterval[k, 1]:
                                        VarInterval[k, 1] = result
                                result = 0
                    else:
                        if splitVar[0] == st:
                            VarInterval[k, 0] = 0
                        else:
                            find_coeff = ref.find_coefficient(st, k, sign)
                            if find_coeff < 0:
                                st = ref.find_lower_limit(st, VarInterval, j, k)
                                result = ref.brentroot(st, VarInterval, k)
                                if result > 0:
                                    if result >= VarInterval[k, 0] and result < VarInterval[k, 1]:
                                        VarInterval[k, 0] = result
                                result = 0
                            else:
                                VarInterval[k, 0] = 0
                elif sign == ">=":
                    if float(rhs) >= 0:
                        if splitVar[0] == st:
                            VarInterval[k, 0] = 0
                        else:
                            find_coeff = ref.find_coefficient(st, k, sign)
                            if find_coeff < 0:
                                VarInterval[k, 0] = 0
                            else:
                                st = ref.find_lower_limit(st, VarInterval, j, k)
                                result = ref.brentroot(st, VarInterval, k)
                                if result > 0:
                                    if result >= VarInterval[k, 0] and result < VarInterval[k, 1]:
                                        VarInterval[k, 0] = result
                                result = 0
                    else:
                        if splitVar[0] == st:
                            st = ref.find_lower_limit(st, VarInterval, j, k)
                            result = ref.brentroot(st, VarInterval, k)
                            if result > 0:
                                if result >= VarInterval[k, 0] and result <= VarInterval[k, 1]:
                                    VarInterval[k, 0] = -result
                            result = 0
                        else:
                            find_coeff = ref.find_coefficient(st, k, sign)
                            if find_coeff < 0:
                                if "-" in st:  # buraya da bakmalı
                                    st = st.replace("-","+")  # ilk değişkenin eksisini kaldırır. her - olan değişkeni + yapar. Başına da + koyar.
                                    st = st[1:]
                                st = ref.find_upper_limit(sign, st, VarInterval, j, k)
                                result = ref.brentroot(st, VarInterval, k)
                                if result > 0:
                                    if result > VarInterval[k, 0] or result < VarInterval[k, 1]:
                                        VarInterval[k, 1] = result
                                result = 0
                            else:
                                VarInterval[k, 0] = 0
                else:
                    print("Hata oluştu!")
                lower = np.append(lower, VarInterval[k, 0])
                upper = np.append(upper, VarInterval[k, 1])
            variable = ref.strVars()[k]
            lower = max(lower)
            upper = min(upper)

            lowerlimitt = np.append(lowerlimitt, VarInterval[k, 0])
            upperlimitt = np.append(upperlimitt, VarInterval[k, 1])
            myDataTableIntervals = [ref.strVars(), lowerlimitt,upperlimitt, np.zeros(self.num_var)]
        myDataTableIntervals = np.reshape(myDataTableIntervals, (4,self.num_var))
        # print(myDataTableIntervals)
        Interval = pd.DataFrame(data=myDataTableIntervals, index=None, columns=None)
        MinValue = -1.7976931348623157E+308
        MaxValue = 1.7976931348623157E+308
        holdBest = np.zeros(self.num_var + 6)
        objective = "Min"
        for item in range(0, self.num_var + 5):
            if objective == "Min":
                holdBest[item] = MaxValue
            else:
                holdBest[item] = MinValue
        return Interval

class evaluate(initialize):
    def __init__(self,num_var,num_const,lowerlimit,upperlimit,rand_set_size):
        super().__init__(num_var, num_const, lowerlimit, upperlimit)
        self.rand_set_size = rand_set_size
    def generate(self,rndCategoryLow,rndCategoryUp):
        k = int(4 * random() + 1)
        IntegerVars = False
        if k == 1:
            myRandomVal = ((rndCategoryUp - rndCategoryLow) / 4) * random() + rndCategoryLow
        elif k == 2:
            myRandomVal = ((rndCategoryUp - rndCategoryLow) / 4) * random() + (rndCategoryUp - rndCategoryLow) / 4 + rndCategoryLow
        elif k == 3:
            myRandomVal = ((rndCategoryUp - rndCategoryLow) / 4) * random() + 2 * (rndCategoryUp - rndCategoryLow) / 4 + rndCategoryLow
        else:
            myRandomVal = ((rndCategoryUp - rndCategoryLow) / 4) * random() + 3 * (rndCategoryUp - rndCategoryLow) / 4 + rndCategoryLow
        if IntegerVars == False:
            myRandomVal = "{:02.3f}".format(myRandomVal)
        return myRandomVal
    def strToformula(self,k,CurrentSolution):
        ref = initialize(self.num_var, self.num_const, self.lowerlimit, self.upperlimit)
        st = str(ref.const()[k][0])
        for j in range(0, self.num_var):
            st = st.replace(ref.strVars()[j], str(0.000000000000001 + CurrentSolution[j]))
        return eval(st)
    def Goal(self,objVal,constraintSatisfiedRate,maxDeviatedConst):
        hitObj = 0
        hitObj += 1
        goal1 = float()
        goal2 = float()
        goal3 = float()
        CurrentWeight1 = 2
        CurrentWeight2 = 0.5
        CurrentWeight3 = 0.01
        goalSign = 1 if eval("{:03.1f}".format(objVal)) == 0.00 else abs(objVal) / objVal
        objective = "Min"
        if objective == "Min":
            goal1 = 1 / ((constraintSatisfiedRate + 1.0E-100) ** (1 + CurrentWeight2))
            if goalSign == -1:
                goal1 = 1 / goal1
            if abs(maxDeviatedConst) < 200:
                goal2 = 1 / math.exp(((goalSign * maxDeviatedConst) * (1 + CurrentWeight3)))
            else:
                goal2 = 1.0E+100
            goal3 = (abs(objVal + 0.000000000000001) ** (CurrentWeight1))
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
    def create_table(self,counter,CurrentInterval):
        global bestOrderId, bestGoalValue, bestObjVal, TotalError,holdBest,DataTableTrain,DataTableSlacks,DataTableConst,trainSet,previousBest,delta,CurrentSolution,res
        CurrentSolution = np.zeros(self.num_var)
        trainSet = np.zeros([self.rand_set_size, self.num_var + 1])
        DataTableTrain = np.zeros([self.rand_set_size, self.num_var + 6])
        DataTableConst = np.zeros([self.rand_set_size, self.num_const + 2])
        DataTableSlacks = np.zeros([self.rand_set_size, self.num_const + 2])
        previousBest = np.zeros(self.num_var + 6)
        delta = np.zeros(self.num_var)
        ref = initialize(self.num_var,self.num_const,self.lowerlimit,self.upperlimit)
        ref2=evaluate(self.num_var, self.num_const,self.lowerlimit,self.upperlimit,self.rand_set_size)
        for i in range(0,self.rand_set_size):
            myObjVal = 1.0E+308
            constraintSatisfiedRate = -1
            trainSetonConstraints = np.zeros([2, self.num_const + 1])
            constraintPerformance = np.zeros(self.num_const)
            maxDeviatedConst = 0
            satisfiedConstraints = 0
            DataTableTrain[i, 0] = i + 1
            DataTableTrain[i, 1] = 1
            for j in range(0, self.num_var):
                rndCategoryLow = float(CurrentInterval[j][1])
                rndCategoryUp = float(CurrentInterval[j][2])
                trainSet[i, j] = ref2.generate(rndCategoryLow,rndCategoryUp)
                DataTableTrain[i, j + 2] = trainSet[i, j]
                CurrentSolution[j] = DataTableTrain[i, j + 2]
            for k in range(0, self.num_const):
                val = ref2.strToformula(k,CurrentSolution)
                if eval(str(val) + str(ref.const()[k][1]) + str(ref.const()[k][2])):
                    if float(ref.const()[k][2]) != 0:  # farklı formda yazdım.
                        DataTableSlacks[i, k + 1] = abs(val - float(ref.const()[k][2])) / float(ref.const()[k][2])
                    else:
                        DataTableSlacks[i, k + 1] = abs(val - float(ref.const()[k][2]))
                    satisfy = True
                    trainSetonConstraints[1, k] = 1
                    constraintPerformance[k] += 1
                else:
                    if float(ref.const()[k][2]) != 0:
                        DataTableSlacks[i, k + 1] = -abs(val - float(ref.const()[k][2])) / float(ref.const()[k][2])
                        maxDeviatedConst += -abs(val - float(ref.const()[k][2])) / float(ref.const()[k][2])
                    else:
                        DataTableSlacks[i, k + 1] = -abs(val - float(ref.const()[k][2]))
                        maxDeviatedConst += -abs(val - float(ref.const()[k][2]))
                    satisfy = False
                    trainSetonConstraints[1, k] = 0
                    trainSetonConstraints[1, self.num_const] = 0
                satisfiedConstraints += trainSetonConstraints[1, k]
            if myObjVal != 1.0E+308:
                objVal = myObjVal
            else:
                objVal = ref.exponential(DataTableTrain[i,2:self.num_var+2])
                #objVal = ref.mccormick(DataTableTrain[i,2],DataTableTrain[i,3]) #2 boyutlularda
            if objVal == 0.0:
                print("dur")
            if satisfiedConstraints == self.num_const:
                trainSetonConstraints[1,self.num_const] = 1
                DataTableSlacks[i, self.num_const + 1] = satisfiedConstraints
                DataTableTrain[i, self.num_var + 2] = objVal
                DataTableTrain[i, self.num_var + 3] = satisfiedConstraints
            if satisfiedConstraints == self.num_const:
                DataTableTrain[i, self.num_var + 4] = 0
                constraintSatisfiedRate = 1
            elif abs(maxDeviatedConst) <= 0.00001:
                satisfiedConstraints = self.num_const
                maxDeviatedConst = 0
                DataTableSlacks[i, self.num_const + 1] = satisfiedConstraints
                DataTableTrain[i, self.num_var + 2] = objVal
                DataTableTrain[i, self.num_var + 3] = satisfiedConstraints
                DataTableTrain[i, self.num_var + 4] = 0
                constraintSatisfiedRate = 1
            else:
                DataTableSlacks[i, self.num_const + 1] = satisfiedConstraints
                DataTableTrain[i, self.num_var + 2] = objVal
                DataTableTrain[i, self.num_var + 3] = satisfiedConstraints
                DataTableTrain[i, self.num_var + 4] = maxDeviatedConst
                constraintSatisfiedRate = satisfiedConstraints / self.num_const
            if i != -1:
                ImpYes = False
                objective = "Min"
                Calculate_Goal = ref2.Goal(objVal,constraintSatisfiedRate,maxDeviatedConst)
                trainSet[i, self.num_var] = Calculate_Goal
                if objective == "Min":
                    if holdBest[self.num_var + 4] > Calculate_Goal:
                        ImpYes = True
                else:
                    if holdBest[self.num_var + 4] < Calculate_Goal:
                        ImpYes = True
                if ImpYes == True:
                    bestOrderId = i + 1
                    bestGoalValue = Calculate_Goal
                    bestObjVal = objVal
                    TotalError = maxDeviatedConst
                    for j in range(0, self.num_var):
                        previousBest[j] = holdBest[j]
                        holdBest[j] = trainSet[i, j]
                        CurrentInterval[j][3] = trainSet[i,j]
                        delta[j] = holdBest[j] - previousBest[j]
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
                    holdBest[self.num_var + 5] = self.rand_set_size
                DataTableTrain[i, self.num_var + 5] = Calculate_Goal
                myGoal = DataTableTrain[i, self.num_var + 5]
                DataTableConst[i, 0] = i + 1
                DataTableSlacks[i, 0] = i + 1
                for j in range(0, self.num_const + 1):
                    DataTableConst[i, j + 1] = trainSetonConstraints[1, j]
            else:
                myGoal = ref2.Goal(objVal,constraintSatisfiedRate,maxDeviatedConst)
        global titles
        titles = ref.strVars()
        DataTableTrain = pd.DataFrame(data=DataTableTrain, index=None,columns=None)
        DataTableConst = pd.DataFrame(data=DataTableConst, index=None,columns= None)
        DataTableSlacks = pd.DataFrame(data=DataTableSlacks, index=None,columns=None)
        ek = min(DataTableTrain.iloc[:, self.num_var + 5])
        res = [i for i, j in enumerate(DataTableTrain.iloc[:, self.num_var + 5]) if j == ek]
        current_best_in_iteration = res[0]
        return DataTableTrain

class improve(evaluate):
    def __init__(self, num_var, num_const, lowerlimit,upperlimit,rand_set_size,textboxiterations):
        super().__init__(num_var, num_const, lowerlimit, upperlimit,rand_set_size)
        self.textboxiterations = textboxiterations
    def bestOrder(self, DataTableTrain):
        ek = min(DataTableTrain.iloc[:, self.num_var + 5])
        res = [i for i, j in enumerate(DataTableTrain.iloc[:, self.num_var + 5]) if j == ek]
        return res[0]
    def update_interval(self,CurrentInterval,uni_low,uni_up):
        for k in range(0, self.num_var):
            randInterval_lower = float(uniform(uni_low, uni_up) * (holdBest[k] - float(CurrentInterval[k][1])) + uniform(uni_low, uni_up) * abs(holdBest[k] - float(CurrentInterval[k][1])))
            randInterval_upper = float(uniform(uni_low, uni_up) * (float(CurrentInterval[k][2]) - holdBest[k]) + uniform(uni_low, uni_up) * abs(float(CurrentInterval[k][2]) - holdBest[k]))
            if holdBest[k] - randInterval_lower - self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3]) < 0 and (holdBest[k]) - randInterval_lower - self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3]) > float(CurrentInterval[k][1]):
                CurrentInterval[k][1] = ((holdBest[k]) - randInterval_lower - self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3]))
            else:
                CurrentInterval[k][1] = CurrentInterval[k][1]
            if (holdBest[k]) + randInterval_upper + self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3]) > 0 and (holdBest[k]) + randInterval_upper + self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3]) < float(CurrentInterval[k][2]):
                CurrentInterval[k][2] = ((holdBest[k]) + randInterval_upper + self.num_const * (1 - holdBest[self.num_var + 2]) * (holdBest[self.num_var + 3]))
            else:
                CurrentInterval[k][2] = CurrentInterval[k][2]
        return CurrentInterval
    def improve_solution(self,DataTableTrain,current_best_in_iteration,CurrentInterval):
        global res,counter
        counter = 1
        hold = np.array(())
        for t in range(1,self.textboxiterations+1):
            uni_low =(0.5 - 0.01 * (t - 1))
            uni_up = 1 - 0.01 * (t - 1)
            if holdBest[self.num_var+4]<= DataTableTrain.iloc[current_best_in_iteration, self.num_var + 5]:
                CurrentInterval = improve(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.rand_set_size,self.textboxiterations).update_interval(CurrentInterval,uni_low,uni_up)
            else:
                CurrentInterval = improve(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.rand_set_size,self.textboxiterations).update_interval(CurrentInterval,uni_low,uni_up)
            print(t, CurrentInterval)
            DataTableTrain = evaluate(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.rand_set_size).create_table(counter,CurrentInterval)
            ek = min(DataTableTrain.iloc[:, self.num_var + 5])
            res = [i for i, j in enumerate(DataTableTrain.iloc[:, self.num_var + 5]) if j == ek]
            current_best_in_iteration = res[0]
            print(DataTableTrain,current_best_in_iteration)
            if  holdBest[self.num_var+4]< DataTableTrain.iloc[current_best_in_iteration, self.num_var + 5]:
                counter += 1
                self.rand_set_size += 10
                print(self.rand_set_size)
                print("counter",counter)
            else:
                counter = counter
                print("counter",counter)
        return holdBest

class run(improve):
    def __init__(self, num_var, num_const, lowerlimit,upperlimit,rand_set_size,textboxiterations):
        super().__init__(num_var, num_const, lowerlimit, upperlimit,rand_set_size,textboxiterations)
    def ortalama(self,column,table):
        ortalama_bestsofar = np.array(())
        for i in range(0,column):
            x=mean(table.iloc[:,i])
            ortalama_bestsofar=np.append(ortalama_bestsofar,x)
        return ortalama_bestsofar
    def rsab(self,num_run):
        global best,bestsofar,limits
        bestsofar = np.array(())
        limits = np.array(())
        for p in range(1, num_run+1):
            print("Run:",p)
            counter = 1
            CurrentInterval = initialize(self.num_var,self.num_const,self.lowerlimit,self.upperlimit).determine()
            print(CurrentInterval)
            DataTableTrain = evaluate(self.num_var,self.num_const,self.lowerlimit,self.upperlimit,self.rand_set_size).create_table(counter, CurrentInterval)
            print(DataTableTrain)
            ek = min(DataTableTrain.iloc[:, self.num_var + 5])
            res = [i for i, j in enumerate(DataTableTrain.iloc[:, self.num_var + 5]) if j == ek]
            current_best_in_iteration = res[0]
            print(current_best_in_iteration)
            ref = improve(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.rand_set_size, self.textboxiterations).improve_solution(DataTableTrain, res[0], CurrentInterval)
            #print(DataTableTrain)
            #bestsofar = np.append(bestsofar,improve(num_var,num_const,lowerlimit,upperlimit,rand_set_size,textboxiterations).improve_solution(DataTableTrain, res[0],CurrentInterval))
            bestsofar = np.append(bestsofar,ref)
            #limit = [CurrentInterval[0][1], CurrentInterval[0][2], CurrentInterval[1][1], CurrentInterval[1][2], CurrentInterval[2][1], CurrentInterval[2][2]]
            #limit = [CurrentInterval[0][1], CurrentInterval[0][2], CurrentInterval[1][1], CurrentInterval[1][2], CurrentInterval[2][1], CurrentInterval[2][2],CurrentInterval[3][1], CurrentInterval[3][2],CurrentInterval[4][1], CurrentInterval[4][2],CurrentInterval[5][1], CurrentInterval[5][2],CurrentInterval[6][1], CurrentInterval[6][2],CurrentInterval[7][1], CurrentInterval[7][2],CurrentInterval[8][1], CurrentInterval[8][2],CurrentInterval[9][1], CurrentInterval[9][2],CurrentInterval[10][1], CurrentInterval[10][2],CurrentInterval[11][1], CurrentInterval[11][2],CurrentInterval[12][1], CurrentInterval[12][2],CurrentInterval[13][1], CurrentInterval[13][2],CurrentInterval[14][1], CurrentInterval[14][2],CurrentInterval[15][1], CurrentInterval[15][2],CurrentInterval[16][1], CurrentInterval[16][2],CurrentInterval[17][1], CurrentInterval[17][2],CurrentInterval[18][1], CurrentInterval[18][2],CurrentInterval[19][1], CurrentInterval[19][2],CurrentInterval[20][1], CurrentInterval[20][2],CurrentInterval[21][1], CurrentInterval[21][2],CurrentInterval[22][1], CurrentInterval[22][2],CurrentInterval[23][1], CurrentInterval[23][2],CurrentInterval[24][1], CurrentInterval[24][2],CurrentInterval[25][1], CurrentInterval[25][2],CurrentInterval[26][1], CurrentInterval[26][2],CurrentInterval[27][1], CurrentInterval[27][2],CurrentInterval[28][1], CurrentInterval[28][2],CurrentInterval[29][1], CurrentInterval[29][2]]
            limit = [CurrentInterval[0][1], CurrentInterval[0][2], CurrentInterval[1][1], CurrentInterval[1][2]]
            limits = np.append(limits, limit)
        limits = limits.reshape(num_run, self.num_var*2)
        best = bestsofar.reshape(num_run, self.num_var+6)
        return limits,best

def export(best,limits):
    #bestso = pd.DataFrame(data=best, index=None,columns=["x01", "x02", "x03", "x04", "x05", "x06", "x07", "x08", "x09", "x10", "x11","x12", "x13", "x14", "x15", "x16", "x17", "x18", "x19", "x20", "x21", "x22","x23", "x24", "x25", "x26", "x27", "x28", "x29", "x30", "best order id","best objval", "constraint satisfied rate", "total error", "best goal","set size"])
    #bestso = pd.DataFrame(data=best, index=None,columns=["x01", "x02","x03", "best order id", "best objval", "constraint satisfied rate","total error", "best goal", "set size"])
    #limitss = pd.DataFrame(data=limits, index=None,columns=["x1-Lower Limit", "x1-Upper Limit", "x2-Lower Limit", "x2-Upper Limit","x3-Lower Limit", "x3-Upper Limit", "x4-Lower Limit", "x4-Upper Limit","x5-Lower Limit", "x5-Upper Limit", "x6-Lower Limit", "x6-Upper Limit","x7-Lower Limit", "x7-Upper Limit", "x8-Lower Limit", "x8-Upper Limit","x9-Lower Limit", "x9-Upper Limit", "x10-Lower Limit", "x10-Upper Limit","x11-Lower Limit", "x11-Upper Limit", "x12-Lower Limit", "x12-Upper Limit","x13-Lower Limit", "x13-Upper Limit", "x14-Lower Limit", "x14-Upper Limit","x15-Lower Limit", "x15-Upper Limit", "x16-Lower Limit", "x16-Upper Limit","x17-Lower Limit", "x17-Upper Limit", "x18-Lower Limit", "x18-Upper Limit","x19-Lower Limit", "x19-Upper Limit", "x20-Lower Limit", "x20-Upper Limit","x21-Lower Limit", "x21-Upper Limit", "x22-Lower Limit", "x22-Upper Limit","x23-Lower Limit", "x23-Upper Limit", "x24-Lower Limit", "x24-Upper Limit","x25-Lower Limit", "x25-Upper Limit", "x26-Lower Limit", "x26-Upper Limit","x27-Lower Limit", "x27-Upper Limit", "x28-Lower Limit", "x28-Upper Limit","x29-Lower Limit", "x29-Upper Limit", "x30-Lower Limit", "x30-Upper Limit"])
    #limitss = pd.DataFrame(data=limits, index=None,columns=["x01 lower limit", "x01 upper limit", "x02 lower limit", "x02 upper limit", "x03 lower limit", "x03 upper limit"])
    bestso = pd.DataFrame(data=best, index=None,columns=["x01", "x02", "best order id", "best objval", "constraint satisfied rate","total error", "best goal", "set size"])
    limitss = pd.DataFrame(data=limits, index=None,columns=["x01 lower limit", "x01 upper limit", "x02 lower limit", "x02 upper limit"])
    export_excel = limitss.to_excel(r'C:\Users\Pau\Desktop\desktop\rsab-results\exponential222--limits.xlsx', index=None,header=True)
    export_excel = bestso.to_excel(r'C:\Users\Pau\Desktop\desktop\rsab-results\exponential222--.xlsx', index=None,header=True)
    #ortalama_best = run(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.rand_set_size,self.textboxiterations).ortalama(self.num_var + 6, bestso)
    #ortalama_limit = run(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.rand_set_size,self.textboxiterations).ortalama(self.num_var * 2, limitss)
    return bestso, limitss

#print(cProfile.run('run(2,4,[-1]*2,[1]*2,10,50).rsab(1)'))
#export(best,limits)
#start_time = time.time()
#print(run(2,4,[-1]*2,[1]*2,10,50).rsab(30))
#print('Duration: {} seconds'.format((time.time() - start_time)))

#command = """run(2,4,[-1]*2,[1]*2,10,50).rsab(1)"""
#cProfile.runctx( command, globals(), locals(), filename="OpenGLContext.profile" )



#run(2,4,[-1]*2,[1]*2,10,50).rsab(1)

if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()
    run(2,4,[-1]*2,[1]*2,10,50).rsab(30)
    pr.disable()
    pr.print_stats()
    pr.dump_stats("result.txt")
    convert("result.txt","output")