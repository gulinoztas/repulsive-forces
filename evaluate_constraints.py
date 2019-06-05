import numpy as np
import determine_intervals
import random_set
import strToformula
import obj_func_val
from goal import Goal
from CalculateGoal import CalculateGoal
import trackBarObjVal
def EvaluateConstraint(myCurretSolution,i=-1,myGoal = 0,myObjVal=1.0E+308):
    train = 1
    trainSetonConstraints = np.array(2,determine_intervals.num_constraints+1)
    constraintPerformance = np.array(determine_intervals.num_constraints)
    maxDeviatedConst = 0
    satisfiedConstraints =0
    constraintSatisfiedRate = -1
    satisfy = bool()
    myDataTableSlacks = np.array(())
    myRandomDataTableConst = np.array(())
    objVal = np.array(())

    for k in range(0,determine_intervals.num_constraints):
        val = strToformula.strToformula(determine_intervals.constraint[k][0],determine_intervals.strVars,myCurretSolution)

        if i==1:   #i mi? 1 mi?
            if i != -1:
                myDataTableSlacks[i,k+1] = abs(val-float(determine_intervals.constraint[k][2]/determine_intervals.constraint[k][2])) if float(determine_intervals.constraint[k][2])!=0 else abs(val-float(determine_intervals.constraint[k][2]))
                satisfy = True
                trainSetonConstraints[1,k]=1
                constraintPerformance[k] += 1
        else:       #unreachable
            if i != -1:
                myDataTableSlacks[i,k+1] = -abs(val-float(determine_intervals.constraint[k][2]/determine_intervals.constraint[k][2])) if float(determine_intervals.constraint[k][2])!=0 else -abs(val-float(determine_intervals.constraint[k][2]))
                maxDeviatedConst += -abs(val-float(determine_intervals.constraint[k][2]/determine_intervals.constraint[k][2])) if float(determine_intervals.constraint[k][2])!=0 else -abs(val-float(determine_intervals.constraint[k][2]))
                satisfy = False
                trainSetonConstraints[1,k]= 0
                trainSetonConstraints[1,determine_intervals.num_constraints]=0
        satisfiedConstraints += trainSetonConstraints[k,1]
    if myObjVal!=1.0E+308:
        objVal = myObjVal
    else:
        objVal=strToformula.strToformula(obj_func_val.obj,determine_intervals.strVars,myCurretSolution)
    if objVal == 0:
        print("dur")

    if i != 1:
        if satisfiedConstraints == determine_intervals.num_constraints:
            trainSetonConstraints[1,determine_intervals.num_constraints]=1
            myDataTableSlacks[i,determine_intervals.num_constraints+1]=satisfiedConstraints
    if satisfiedConstraints == determine_intervals.num_constraints:
        if i!=1:
            random_set.myRandomDataTableTrain[i,determine_intervals.num_var+4] = 0
            constraintSatisfiedRate = 1
    elif abs(maxDeviatedConst)<= 0.00001:
        satisfiedConstraints = determine_intervals.num_constraints
        maxDeviatedConst = 0
        if i != 1:
            random_set.myRandomDataTableTrain[i,determine_intervals.num_var+4]=0
            constraintSatisfiedRate = 1
    else:
        if i !=1:
            random_set.myRandomDataTableTrain[i,determine_intervals.num_var+4] = maxDeviatedConst
            constraintSatisfiedRate = satisfiedConstraints / determine_intervals.num_constraints

    if i !=1:
        random_set.myRandomDataTableTrain[i,determine_intervals.num_var+5] = CalculateGoal(i,constraintSatisfiedRate,maxDeviatedConst,objVal,myCurretSolution)   #calculate goal fonksiyonu
        myGoal = random_set.myRandomDataTableTrain[i,determine_intervals.num_var+5]
        myRandomDataTableConst[i,0]=i+1
        myDataTableSlacks[i,0]=i+1
        for j in range(0,determine_intervals.num_constraints):
            myRandomDataTableConst[i,j+1]=trainSetonConstraints[1,j]
    else:
        myGoal = Goal(constraintSatisfiedRate,trackBarObjVal.valTrackBarSatisfaction,maxDeviatedConst,trackBarObjVal.valTrackBarDeviation,objVal,trackBarObjVal.valTrackBarObjVal)
