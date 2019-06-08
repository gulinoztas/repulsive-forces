import determine_intervals
import numpy as np
import evaluate_constraints
import goal
import random_set
import trackBarObjVal
import obj_func_val
MinValue = -1.7976931348623157E+308
MaxValue = 1.7976931348623157E+308
def CalculateGoal(i,constraintSatisfiedRate,maxDeviatedConst,objVal):
    holdBest = np.zeros(determine_intervals.num_var+5)
    ImpYes = False
    MaxValue = 1.7976931348623157E+308
    MinValue = -1.7976931348623157E+308
    numIterations = 0
    j=0
    objective = "Min"

    constraintSatisfiedRate = obj_func_val.slacks_table.iloc[i, 10]
    maxDeviatedConst = obj_func_val.randoms.iloc[i, 8]
    objVal = obj_func_val.objective[i]

    if holdBest[0] == 0:
        for item in range(0, determine_intervals.num_var + 5):
            holdBest[item] = MaxValue if objective == "Min" else MinValue
        # print("revised holdbest",holdBest)

    Calculate_Goal = goal.Goal(constraintSatisfiedRate, maxDeviatedConst, objVal, trackBarObjVal.valTrackBarObjVal)
    # Calculated_Goals = np.append(Calculated_Goals,Calculate_Goal)
    # print("Calculated Goal",Calculate_Goal)
    # random_set.trainSet[i,4]=Calculate_Goal
    random_set.trainset_table.iloc[i, 4] = Calculate_Goal
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
        bestObjVal = obj_func_val.randoms.iloc[i, 6]
        TotalError = obj_func_val.randoms.iloc[i, 8]
        # print("bestorderıd", bestOrderId,"best goal",bestGoalValue,"best obj val",bestObjVal,"total error",TotalError)

        for j in range(0, determine_intervals.num_var):
            holdBest[j] = random_set.trainset_table.iloc[i, j]
            determine_intervals.Intervals.iloc[j, 3] = random_set.trainset_table.iloc[i, j]
        # print("Intervals",determine_intervals.Intervals,"holdbest",holdBest)
        # print("fefe",random_set.trainset_table)

        holdBest[determine_intervals.num_var] = bestOrderId
        holdBest[determine_intervals.num_var + 1] = bestObjVal
        holdBest[determine_intervals.num_var + 2] = constraintSatisfiedRate
        holdBest[determine_intervals.num_var + 3] = TotalError
        holdBest[determine_intervals.num_var + 4] = bestGoalValue

        numIterations = 0
        numIterations += 1
    return Calculate_Goal

