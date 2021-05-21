import math
import numpy as np
import variables
from rsab_v3 import *
from collections import Counter
from opfunu.dimension_based.benchmark2d import Functions
from opfunu.cec.cec2014.function import *
class atom():
    def __init__(self, num_var, num_const, lowerlimit,upperlimit,rand_set_size,textboxiterations):
        self.num_var = num_var
        self.num_const = num_const
        self.lowerlimit = lowerlimit
        self.upperlimit = upperlimit
        self.rand_set_size = rand_set_size
        self.textboxiteration = textboxiterations
    def WorstValue(self):
        goalSign = 1 if eval("{:02.1f}".format(float(variables.bestfit[variables.gbest]))) == 0.0 else abs(variables.bestfit[variables.gbest]) / variables.bestfit[variables.gbest]
        if variables.objective == "Min":
            if goalSign ==1:
                WorstValue = 1.0E+100
            else:
                WorstValue = 1.0E+100
        else:
            if goalSign ==1:
                WorstValue = -1.0E+100
            else:
                WorstValue = -1.0E+100
        return WorstValue
    def Fun(self,i,CurrentSolution,item1,item2,item3): #calculates fitness value (objective value, constraint satisfied rate, total deviation)
        trainSetonConstraints = np.zeros([2, self.num_const + 1])
        constraintPerformance = np.zeros(self.num_const)
        variables.satisfiedConstraints = 0
        variables.maxDeviatedConst = 0
        ref = rsab(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations)
        for k in range(0, variables.subject_to_const):
            st = str(ref.const2()[k+variables.num_bound][0])
            strVars = ref.strVars()
            val = ref.strToformula(st,strVars,CurrentSolution)
            if eval(str(val) + str(ref.const2()[k+variables.num_bound][1]) + str(ref.const2()[k+variables.num_bound][2])):
                satisfy = True
                trainSetonConstraints[1, k] = 1
                constraintPerformance[k] += 1
            else:
                if float(ref.const2()[k+variables.num_bound][2]) != 0:
                    variables.maxDeviatedConst += -abs(val - float(ref.const2()[k+variables.num_bound][2]))/float(ref.const2()[k+variables.num_bound][2])
                else:
                    variables.maxDeviatedConst += -abs(val - float(ref.const2()[k+variables.num_bound][2]))
                satisfy = False
                trainSetonConstraints[1, k] = 0
                trainSetonConstraints[1, variables.num_const] = 0
            variables.satisfiedConstraints += trainSetonConstraints[1, k]
        if variables.satisfiedConstraints == variables.subject_to_const:#variables.num_const:
            trainSetonConstraints[1, variables.num_const] = 1
            variables.constraintSatisfiedRate = 1
        elif abs(variables.maxDeviatedConst) <= 0.00000000001:#0.00001:#0.00000000001: for 3rd article#//<=0.00001:abs #0.0000001:
            variables.satisfiedConstraints = variables.subject_to_const#variables.num_const
            variables.maxDeviatedConst = 0
            variables.constraintSatisfiedRate = 1
        else:
            variables.constraintSatisfiedRate = variables.satisfiedConstraints / variables.subject_to_const#variables.num_const
        variables.objVal = ref.call_function(variables.function, CurrentSolution)
        myGoal = ref.Goal(variables.objVal, variables.constraintSatisfiedRate, variables.maxDeviatedConst,item1,item2,item3)

        return variables.constraintSatisfiedRate,variables.maxDeviatedConst,myGoal
    def f(self,item1,item2,item3,CurrentSolution,i=-1,compareFuncVal=1E+100): #compare fitness values
        global tmpObjVal,strVars,objective
        variables.tmpObjVal = rsab(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).call_function(variables.function,CurrentSolution)
        constraintsatisfiedRate = atom(self.num_var, self.num_const, self.lowerlimit, self.upperlimit,self.rand_set_size, self.textboxiteration).Fun(i,CurrentSolution,item1,item2,item3)[0]
        maxDeviatedConst = atom(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.rand_set_size,self.textboxiteration).Fun(i,CurrentSolution,item1,item2,item3)[1]
        if variables.objective=="Min":
            Goal = rsab(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).Goal(variables.tmpObjVal,constraintsatisfiedRate,maxDeviatedConst,item1,item2,item3) #satisfied constraint ve maxdeviatedconst güncellenmeli
            if Goal <= compareFuncVal:
                tmp = Goal
                if tmp == 0:
                    tmp = atom(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.rand_set_size,self.textboxiteration).WorstValue()
                else:
                    tmp = tmp
            else:
                tmp = compareFuncVal
        else:
            Goal = atom(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.rand_set_size,self.textboxiteration).Fun(i,CurrentSolution,item1,item2,item3)[2]
            if Goal >= compareFuncVal:
                tmp = Goal
                if tmp == 0:
                    tmp = 1.0E+111
                else:
                    tmp = tmp
            else:
                tmp = compareFuncVal
        return tmp,constraintsatisfiedRate,maxDeviatedConst,Goal
    def f1(self,Goal,compareFuncVal=1E+100): #compare fitness values
        global tmpObjVal,strVars,objective
        if variables.objective=="Min":
            if Goal <= compareFuncVal:
                tmp = Goal
                if tmp == 0:
                    tmp = atom(self.num_var, self.num_const, self.lowerlimit, self.upperlimit, self.rand_set_size,self.textboxiteration).WorstValue()
                else:
                    tmp = tmp
            else:
                tmp = compareFuncVal
            #print("tmp", tmp)
        else:
            if Goal >= compareFuncVal:
                tmp = Goal
                if tmp == 0:
                    tmp = 1.0E+111
                else:
                    tmp = tmp
            else:
                tmp = compareFuncVal
        return tmp
    def calculateRelativeDistance(self,x1,x2): #calculate relative distance between particles
        for i in range(0,variables.dimension):
            variables.calculateRelativeDistance +=(x1[i]-x2[i])**2 / (abs((x1[i]+x2[i])/2+0.000000000000000000000000000001))  #tanımsız olmasın diye eklendi
        if math.isnan((variables.calculateRelativeDistance)):
            variables.calculateRelativeDistance += 0
        return math.sqrt(variables.calculateRelativeDistance)
    def calculateAngle(self,x1,x2):
        if variables.dimension<=1:
            return 0
        totalXs = np.zeros((variables.dimension))
        totalSSXs = np.zeros((2))
        totalXs[0]= 1
        totalXs[1] = 1
        for i in range(0,variables.dimension):
            totalXs[i] = totalXs[i]*x1[i]
            totalXs[i] = totalXs[i]*x2[i]
            totalSSXs[0] += x1[i]**2
            totalSSXs[1] += x2[i]**2
        totalSS = 0
        totalSS = totalSSXs[0]**0.5 * totalSSXs[1]**0.5
        tmpAngle = (totalXs[0]+totalXs[1])/ (totalSS+0.000000000000000000001)
        tmpAngle = math.cos(tmpAngle) if tmpAngle <= 1 else 0
        return tmpAngle
    def calculateDistance(self,x1,x2): #calculates euclidean distance
        variables.calculateDistance= 0
        for i in range(0,variables.dimension):
            variables.calculateDistance += (x1[i]-x2[i])**2
        if math.isnan((variables.calculateDistance)):
            variables.calculateDistance += 0
        return math.sqrt(variables.calculateDistance)
    def verify(self,x,i):   #in case of the new location is out of intervals
        if math.isnan(x) or math.isinf(x):
            print("dur4")
        if x > float(variables.CurrentInterval[i][2]):
            x = float(variables.CurrentInterval[i][2])
        elif x < float(variables.CurrentInterval[i][1]):
            x = float(variables.CurrentInterval[i][1])
        if math.isnan(x):
            print("dur4_1")
        if variables.function=="pressure":
            if i<2: #for x1 and x2
                x = x- (x % 0.0625)
        if variables.function == "dispatch":
            x = int(x)
        return x
    def title_interval(self): #generates title for interval table
        x = []
        for i in range(0, variables.num_var):
            x.append("x" + str(i + 1) + "-LL")
            x.append("x" + str(i + 1) + "-UL")
        return x
    def title_result(self): #generates title for result table
        x = []
        x.append("Iteration Number")
        x.append("Function Evaluation")
        for i in range(0, variables.num_var):
            x.append("x" + str(i + 1))
        x.append("Obj")
        x.append("Fitness")
        return x
    def summary_title(self): #generates title for summary table
        x = []
        x.append("item1")
        x.append("item2")
        x.append("item3")
        x.append("Iteration")
        x.append("Eval")
        for i in range(0, variables.num_var):
            x.append("x" + str(i + 1))
        x.append("Obj")
        x.append("Fitness")
        x.append("satisfied constraints")
        x.append("maxdeviated")
        return x
    def duplicate(input): #check duplication
        freqDict = Counter(map(tuple, input))
        x = np.array(())
        s = 0
        for (row, freq) in freqDict.items():
            if freq > 1:
                s += 1
                x = np.concatenate((row, x), axis=0)
        x = x.reshape(s, variables.num_var)
        return x
    def check_database(self, Interval, database, test, k): #check database whether the new location has been visited before or not.
        while any(np.equal(database, test).all(1)) == True:
            if len(variables.constrained) == 0:
                if variables.allow>variables.set_size: #for unconstrained problems. it has been restricted with set size so that it can exit the loop.
                    break
            variables.allow +=1
            test = np.array([[(rsab(variables.num_var, variables.num_const, variables.lowerlimit,variables.upperlimit, variables.set_size,variables.textboxiterations).generate(j, Interval)) for j in range(0, variables.dimension)]])
        return test
    def duplicated_index(self, x, general): #gives duplicated index
        ind = np.array(())
        for t in range(0, len(x)):
            find = (np.equal(general, x[t]).all(1))
            r = [i for i, j in enumerate((find)) if j == True]
            indeks = r[0]
            ind = np.append(ind, indeks)
        return ind
    def truncate(self,number, decimals=0): #Returns a value truncated to a specific number of decimal places.
        if not isinstance(decimals, int):
            raise TypeError("decimal places must be an integer.")
        elif decimals < 0:
            raise ValueError("decimal places has to be 0 or more.")
        elif decimals == 0:
            return math.trunc(number)
        factor = 10.0 ** decimals
        return np.trunc(number * factor) / factor
    def weights(self): #normalizes the constants in MUPE
        obj = variables.weight1.copy()[0]
        satis = variables.weight2.copy()[0]
        dev = variables.weight3.copy()[0]
        variables.weight1[0] = obj * 0.1
        variables.weight3[0] = dev * 0.1 if obj + dev <= 10 else (10 - obj) * 0.1
        variables.weight2[0] = (10 - (obj + dev)) * 0.1
        return
