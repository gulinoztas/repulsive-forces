import numpy as np
import determine_intervals
import random_set
import strToformula
import obj_func_val
import CalculateGoal
import goal
import trackBarObjVal
CurrentSolution = np.zeros(determine_intervals.num_var)
myCurrentSolution = np.zeros(determine_intervals.num_var)
myObjVal = 1.0E+308
constraintSatisfiedRate = -1
for i in range(0,random_set.train):

    for j in range(0,determine_intervals.num_var):
        CurrentSolution[j]= random_set.rndDataTable.iloc[i,j+2]
    #print("current solution",CurrentSolution)


    trainSetonConstraints = np.zeros([2,determine_intervals.num_constraints+1])
    constraintPerformance = np.zeros(determine_intervals.num_constraints)
    maxDeviatedConst = 0
    satisfiedConstraints = 0

    for k in range(0,determine_intervals.num_constraints):
        val = strToformula.strToformula(determine_intervals.constraint[k][0],determine_intervals.strVars,CurrentSolution)
        #print("val",k,val)

        if 1==1:
            if i != -1:
                random_set.myDataTableSlacks[i,k+1]= abs(val-float(determine_intervals.constraint[k][2]))/float(determine_intervals.constraint[k][2]) if float(determine_intervals.constraint[k][2])!=0 else abs(val-float(determine_intervals.constraint[k][2]))
                #print("değer", abs(val - float(determine_intervals.constraint[k][2])) / float(determine_intervals.constraint[k][2]))
    #print(random_set.myDataTableSlacks)
                satisfy = True
                trainSetonConstraints[1,k]=1
    #print("seton",trainSetonConstraints)
                constraintPerformance[k] +=1
    #print("performance",constraintPerformance)
                #print("slacks",random_set.myDataTableSlacks)

        else:
            if i != -1:
                random_set.myDataTableSlacks[i,k+1]= abs(val-float(determine_intervals.constraint[k][2]))/float(determine_intervals.constraint[k][2]) if float(determine_intervals.constraint[k][2])!=0 else abs(val-float(determine_intervals.constraint[k][2]))
                satisfy = False
                trainSetonConstraints[1,k] = 0
                trainSetonConstraints[1,determine_intervals.num_constraints] = 0
    #print("seton",trainSetonConstraints)

        satisfiedConstraints += trainSetonConstraints[1,k]
#print(satisfiedConstraints)

    if myObjVal != 1.0E+308:
        objVal = myObjVal
    else:
        #print("current one",CurrentSolution)
        #objVal = strToformula.strToformula(obj_func_val.obj, determine_intervals.strVars, CurrentSolution) #her set için yapmıyor yalnızca sonuncusu için çalışıyor.
        objVal = obj_func_val.objective[i]
        #print("objval",objVal)

    if objVal == 0:
        print("dur")

    if i != -1:
        if satisfiedConstraints == determine_intervals.num_constraints:
            trainSetonConstraints[1,determine_intervals.num_constraints]=1
            random_set.myDataTableSlacks[i,determine_intervals.num_constraints+1] = satisfiedConstraints
    #print("seton",trainSetonConstraints)
    #print("slacks",random_set.myDataTableSlacks)

    if satisfiedConstraints == determine_intervals.num_constraints:
        if i != -1:
            random_set.rndDataTable.iloc[i,determine_intervals.num_var+2] = 0  #shows all constraints are satisfied
            constraintSatisfiedRate = 1

    elif abs(maxDeviatedConst) <= 0.00001:
        satisfiedConstraints = determine_intervals.num_constraints
        maxDeviatedConst = 0
        if i != -1:
            random_set.rndDataTable.iloc[i,determine_intervals.num_var+2] = 0
            constraintSatisfiedRate = 1
    else:
        if i != -1:
            random_set.rndDataTable.iloc[i,determine_intervals.num_var+2] = maxDeviatedConst  #shows total deviation from constraints
            constraintSatisfiedRate = satisfiedConstraints/determine_intervals.num_constraints
#print("fsdnfml",random_set.rndDataTable)

    if i != -1:
        random_set.rndDataTable.iloc[i,determine_intervals.num_var+3] = CalculateGoal.CalculateGoal(i,constraintSatisfiedRate,maxDeviatedConst,objVal)
        myGoal = random_set.rndDataTable.iloc[i,determine_intervals.num_var+3]
        random_set.myRandomDataTableConst[i,0]=i+1
        random_set.myDataTableSlacks[i,0]=i+1
    print("goal",i,myGoal)
"""

        for j in range(0,determine_intervals.num_constraints+1):
            random_set.myRandomDataTableConst[i,j+1]= trainSetonConstraints[1,j]
    else:
        myGoal = goal.Goal(constraintSatisfiedRate,maxDeviatedConst,objVal,trackBarObjVal.valTrackBarObjVal)


"""




