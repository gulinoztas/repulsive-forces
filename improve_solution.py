import CalculateGoal
import random_set
import math
from random import random
import CalculateGoal
import obj_func_val
import eval_const
import myRandomVal
import goal
import trackBarObjVal
import numpy as np
import determine_intervals
randInterval = 0
noImprovement = False
tmpBestVal = CalculateGoal.MinValue
num_Iteration = 20
CurrentSolution = np.zeros(determine_intervals.num_var)
for j in range(1,num_Iteration+1):
    if num_Iteration>= 20*random_set.train:
        randInterval = float(0.21*math.log10(random()+0.009)+1)
    if eval_const.holdBest[determine_intervals.num_var+4] <= eval_const.MyRandomDataTableTrain.iloc[eval_const.bestOrderId-1,determine_intervals.num_var+5]:
        for k in range(0,determine_intervals.num_var):
            if (eval_const.MyRandomDataTableTrain.iloc[eval_const.bestOrderId-1,k+2]-randInterval-determine_intervals.num_constraints*(1-eval_const.constraintSatisfiedRate)*float(abs(eval_const.TotalError))) > 0:
                determine_intervals.Intervals[k,1] = eval_const.MyRandomDataTableTrain.iloc[eval_const.bestOrderId-1,k+2]-randInterval-determine_intervals.num_constraints*(1-eval_const.constraintSatisfiedRate)*float(abs(eval_const.TotalError))
            else:
                determine_intervals.Intervals[k,1] = 0

            if (eval_const.MyRandomDataTableTrain.iloc[eval_const.bestOrderId-1,k+2] + randInterval + determine_intervals.num_constraints*(1-eval_const.constraintSatisfiedRate)*float(abs(eval_const.TotalError))) < determine_intervals.VarInterval[k,1]:
                determine_intervals.VarInterval[k,2] = eval_const.MyRandomDataTableTrain.iloc[eval_const.bestOrderId-1,k+2]+ randInterval + determine_intervals.num_constraints*(1-eval_const.constraintSatisfiedRate)*float(abs(eval_const.TotalError))
            else:
                determine_intervals.Intervals[k,2]= determine_intervals.VarInterval[k,1]

    else:
        for k in range(0,determine_intervals.num_var):
            if eval_const.holdBest[k]-randInterval-determine_intervals.num_constraints *(1-eval_const.holdBest[determine_intervals.num_var+2])*abs(eval_const.holdBest[determine_intervals.num_var+3]) > 0:
                determine_intervals.Intervals[k,1] = eval_const.holdBest[k]-randInterval-determine_intervals.num_constraints*(1-eval_const.holdBest[determine_intervals.num_var+2])*abs(eval_const.holdBest[determine_intervals.num_var+3])
            else:
                determine_intervals.Intervals[k,1]= 0

            if eval_const.holdBest[k]+randInterval+determine_intervals.num_constraints *(1-eval_const.holdBest[determine_intervals.num_var+2])*abs(eval_const.holdBest[determine_intervals.num_var+3]) < determine_intervals.VarInterval[k,1]:
                determine_intervals.Intervals[k,2] = eval_const.holdBest[k]+randInterval+determine_intervals.num_constraints*(1-eval_const.holdBest[determine_intervals.num_var+2])*abs(eval_const.holdBest[determine_intervals.num_var+3])
            else:
                determine_intervals.Intervals[k,2]= determine_intervals.VarInterval[k,1]

    for i in range(0, random_set.train):
        eval_const.MyRandomDataTableTrain[i, 0] = i + 1
        eval_const.MyRandomDataTableTrain[i, 1] = 1
        for j in range(0, determine_intervals.num_var):
            random_set.trainSet[i, j] = myRandomVal.myRandomVal(j)
            eval_const.MyRandomDataTableTrain[i, j + 2] = random_set.trainSet[i, j]

            CurrentSolution[j] = eval_const.MyRandomDataTableTrain[i, j + 2]
        """------------evaluate constraints--------------"""
        holdBest = np.zeros(determine_intervals.num_var + 5)
        ImpYes = False
        MaxValue = 1.7976931348623157E+308
        MinValue = -1.7976931348623157E+308
        numIterations = 0
        j = 0
        objective = "Min"
        constraintSatisfiedRate = obj_func_val.slacks_table.iloc[i, determine_intervals.num_constraints + 1]
        # print("satisfied",constraintSatisfiedRate)
        maxDeviatedConst = obj_func_val.randoms.iloc[i, determine_intervals.num_constraints - 1]
        objVal = obj_func_val.objective[i]
        # print("holdbest",holdBest)
        print("satisfied rate", obj_func_val.slacks_table.iloc[i, determine_intervals.num_constraints + 1], "deviation",
              obj_func_val.randoms.iloc[i, determine_intervals.num_constraints - 1], "objval",
              obj_func_val.objective[i])

        if holdBest[0] == 0:
            for item in range(0, determine_intervals.num_var + 5):
                holdBest[item] = MaxValue if objective == "Min" else MinValue
            # print("holdbest",holdBest)
        # print("maxdeviation",maxDeviatedConst)
        Calculate_Goal = goal.Goal(constraintSatisfiedRate, maxDeviatedConst, objVal, trackBarObjVal.valTrackBarObjVal)
        #Calculated_Goals = np.append(Calculated_Goals, Calculate_Goal)
        # print("Calculated Goal",Calculate_Goal)
        # random_set.trainSet[i,4]=Calculate_Goal
        random_set.trainset_table.iloc[i, determine_intervals.num_var] = Calculate_Goal
        # print("CALCULATE GOAL",Calculate_Goal)
        # print(random_set.trainset_table)

        # print(random_set.trainset_table)

        if objective == "Min":
            if holdBest[determine_intervals.num_var + 4] > Calculate_Goal:
                ImpYes = True
        else:
            if holdBest[determine_intervals.num_var + 4] < Calculate_Goal:
                ImpYes = True

        if ImpYes == True:
            bestOrderId = i + 1
            bestGoalValue = Calculate_Goal
            bestObjVal = obj_func_val.randoms.iloc[i, determine_intervals.num_var + 2]
            TotalError = obj_func_val.randoms.iloc[i, determine_intervals.num_var + 4]
            print("bestorderıd", bestOrderId, "best goal", bestGoalValue, "best obj val", bestObjVal, "total error",
                  TotalError)

            for j in range(0, determine_intervals.num_var):
                holdBest[j] = random_set.trainset_table.iloc[i, j]
                determine_intervals.Intervals.iloc[j, 3] = random_set.trainset_table.iloc[i, j]
            print(determine_intervals.Intervals, "holdbest", holdBest)
            print("fefe", random_set.trainset_table)

            holdBest[determine_intervals.num_var] = bestOrderId
            holdBest[determine_intervals.num_var + 1] = bestObjVal
            holdBest[determine_intervals.num_var + 2] = constraintSatisfiedRate
            holdBest[determine_intervals.num_var + 3] = TotalError
            holdBest[determine_intervals.num_var + 4] = bestGoalValue

            numIterations = 0
            numIterations += 1

    numIterations = 0

print("revised intervals",determine_intervals.Intervals)