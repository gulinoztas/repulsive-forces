import determine_intervals
import numpy as np
from evaluate_constraints import EvaluateConstraint
import evaluate_constraints
from goal import Goal
import goal
import random_set
import trackBarObjVal
def CalculateGoal(i,constraintSatisfiedRate,maxDeviatedConst,objVal,myCurrentSolution):
    holdBest = np.array(determine_intervals.num_var+5)
    ImpYes = False
    MaxValue = 1.7976931348623157E+308
    MinValue = -1.7976931348623157E+308
    numIterations = 0
    if holdBest[0]== None:
        for item in range(0,determine_intervals.num_var+5):
            holdBest[item]=MaxValue if goal.objective =="Min" else MinValue
    CalculateGoal = Goal(constraintSatisfiedRate, trackBarObjVal.valTrackBarSatisfaction, maxDeviatedConst, trackBarObjVal.valTrackBarDeviation, objVal, trackBarObjVal.valTrackBarObjVal)
    random_set.trainSet[i,determine_intervals.num_var] = CalculateGoal
    if goal.objective == "Min":
        if holdBest[determine_intervals.num_var+5]> CalculateGoal:
            ImpYes = True
    else:
        if holdBest[determine_intervals.num_var+5]<CalculateGoal:
            ImpYes = True
    if ImpYes == True:
        bestOrderId = i+1
        bestGoalValue = CalculateGoal
        bestObjVal = objVal
        TotalError = maxDeviatedConst
        constraintSatisfiedRate = evaluate_constraints.satisfiedConstraints / determine_intervals.num_constraints

        for j in range (0,determine_intervals.num_var):
            holdBest[j]=random_set.trainSet[i,j]
            determine_intervals.Intervals.iloc[j,3]=random_set.trainSet[i,j]

        holdBest[determine_intervals.num_var] = bestOrderId
        holdBest[determine_intervals.num_var + 1] = bestObjVal
        holdBest[determine_intervals.num_var + 2] = constraintSatisfiedRate
        holdBest[determine_intervals.num_var + 3] = TotalError
        holdBest[determine_intervals.num_var + 4] = bestGoalValue

        print("best order id",bestOrderId)
        print("best objective value",bestObjVal)
        print("satisfaction rate",constraintSatisfiedRate)
        print("Deviation",abs(TotalError))
        print("Goal Indicator",bestGoalValue)
        numIterations = 0

    else:
        numIterations +=1

    return CalculateGoal
