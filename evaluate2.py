import numpy as np
import variables
from rsab_v3 import *
def evaluate(CurrentInterval,i,DataTableTrain,DataTableSlacks,DataTableConst,trainSet,item1,item2,item3):
    ref = rsab(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations)
    myObjVal = 1.0E+308 #default objective value
    constraintSatisfiedRate = -1 #default constraint satisfied rate
    trainSetonConstraints = np.zeros([2, variables.num_const + 1])
    constraintPerformance = np.zeros(variables.num_const)
    DataTableTrain[i, 0] = i + 1
    DataTableTrain[i, 1] = 1
    variables.maxDeviatedConst = 0 #default amount of maximum deviation
    variables.satisfiedConstraints = 0 #default amount of satisfied constraints

    for j in range(0, variables.num_var): #generating initial candidate solution
        trainSet[i, j] = ref.generate(j,CurrentInterval)
        DataTableTrain[i, j + 2] = trainSet[i, j]
        variables.CurrentSolution[j] = DataTableTrain[i, j + 2]

    if len(variables.constrained)==0: #in case of unconstrained problems
        variables.constraintSatisfiedRate = 1
        variables.maxDeviatedConst = 0
        if myObjVal != 1.0E+308:
            objVal = myObjVal
        else:
            objVal = ref.call_function(variables.function, variables.CurrentSolution) #calculating objective value
        if objVal == 0.0:
            print("dur")

        DataTableTrain[i, variables.num_var + 2] = objVal
        """---------------MUPE-----------------"""
        myGoal = ref.Goal(objVal, variables.constraintSatisfiedRate, variables.maxDeviatedConst, item1, item2, item3) #calculating fitness value with MUPE
        """---------------MUPE-----------------"""
        ImpYes = False

        trainSet[i, variables.num_var] = myGoal
        if variables.objective == "Min":
            if variables.holdBest[variables.num_var + 4] > myGoal:  # and variables.satisfiedConstraints == variables.num_const: #10/11/2020
                ImpYes = True
        else:
            if variables.holdBest[variables.num_var + 4] < myGoal:
                ImpYes = True
        if ImpYes == True:
            bestOrderId = i + 1
            bestGoalValue = myGoal
            bestObjVal = objVal
            TotalError = 0
            for j in range(0, variables.num_var):
                variables.previousBest[j] = variables.holdBest[j]
                variables.holdBest[j] = trainSet[i, j]
                #CurrentInterval[j][3] = trainSet[i, j]
                CurrentInterval[3][j] = trainSet[i, j]
            variables.previousBest[variables.num_var] = variables.holdBest[variables.num_var]
            variables.previousBest[variables.num_var + 1] = variables.holdBest[variables.num_var + 1]
            variables.previousBest[variables.num_var + 2] = variables.holdBest[variables.num_var + 2]
            variables.previousBest[variables.num_var + 3] = variables.holdBest[variables.num_var + 3]
            variables.previousBest[variables.num_var + 4] = variables.holdBest[variables.num_var + 4]
            variables.previousBest[variables.num_var + 5] = variables.holdBest[variables.num_var + 5]

            variables.holdBest[variables.num_var] = bestOrderId
            variables.holdBest[variables.num_var + 1] = bestObjVal
            variables.holdBest[variables.num_var + 2] = variables.constraintSatisfiedRate
            variables.holdBest[variables.num_var + 3] = TotalError
            variables.holdBest[variables.num_var + 4] = bestGoalValue
            variables.holdBest[variables.num_var + 5] = variables.set_size

        DataTableTrain[i, variables.num_var + 3] = variables.constraintSatisfiedRate
        DataTableTrain[i, variables.num_var + 4] = variables.maxDeviatedConst
        DataTableTrain[i, variables.num_var + 5] = myGoal


    else: #in case of constrained problems
        for k in range(0, variables.subject_to_const):
            st = str(ref.const()[k+variables.num_bound][0])
            strVars = ref.strVars()
            val = ref.strToformula(st,strVars,variables.CurrentSolution)
            if eval(str(val) + str(ref.const()[k+variables.num_bound][1]) + str(ref.const()[k+variables.num_bound][2])):
                if float(ref.const()[k+variables.num_bound][2]) != 0:
                    DataTableSlacks[i, k + 1] = abs(val - float(ref.const()[k+variables.num_bound][2])) / float(ref.const()[k+variables.num_bound][2])
                else:
                    DataTableSlacks[i, k + 1] = abs(val - float(ref.const()[k+variables.num_bound][2]))
                satisfy = True
                trainSetonConstraints[1, k] = 1
                constraintPerformance[k] += 1
            else:
                if float(ref.const()[k+variables.num_bound][2]) != 0:
                    DataTableSlacks[i, k + 1] = -abs(val - float(ref.const()[k+variables.num_bound][2])) / float(ref.const()[k+variables.num_bound][2])
                    variables.maxDeviatedConst += -abs(val - float(ref.const()[k+variables.num_bound][2])) / float(ref.const()[k+variables.num_bound][2])
                else:
                    DataTableSlacks[i, k + 1] = -abs(val - float(ref.const()[k+variables.num_bound][2]))
                    variables.maxDeviatedConst += -abs(val - float(ref.const()[k+variables.num_bound][2]))
                satisfy = False
                trainSetonConstraints[1, k] = 0
                trainSetonConstraints[1, variables.num_const] = 0
            variables.satisfiedConstraints += trainSetonConstraints[1, k]

        if myObjVal != 1.0E+308:
            objVal = myObjVal
        else:
            objVal = ref.call_function(variables.function,variables.CurrentSolution)
        if objVal == 0.0:
            print("dur")


        if variables.satisfiedConstraints == variables.subject_to_const:
            trainSetonConstraints[1,variables.num_const] = 1
            DataTableSlacks[i, variables.subject_to_const + 1] = variables.satisfiedConstraints
            DataTableTrain[i, variables.num_var + 2] = objVal
            DataTableTrain[i, variables.num_var + 3] = variables.satisfiedConstraints
            DataTableTrain[i, variables.num_var + 4] = 0
            constraintSatisfiedRate = 1

        elif abs(variables.maxDeviatedConst) <= 0.00001:  #BURADA DEĞİŞİKLİK YAPILABİLİR
            variables.satisfiedConstraints = variables.subject_to_const
            variables.maxDeviatedConst = 0
            DataTableSlacks[i, variables.subject_to_const + 1] = variables.satisfiedConstraints
            DataTableTrain[i, variables.num_var + 2] = objVal
            DataTableTrain[i, variables.num_var + 3] = variables.satisfiedConstraints
            DataTableTrain[i, variables.num_var + 4] = 0
            constraintSatisfiedRate = 1
        else:
            DataTableSlacks[i, variables.subject_to_const + 1] = variables.satisfiedConstraints
            DataTableTrain[i, variables.num_var + 2] = objVal
            DataTableTrain[i, variables.num_var + 3] = variables.satisfiedConstraints
            DataTableTrain[i, variables.num_var + 4] = variables.maxDeviatedConst
            constraintSatisfiedRate = variables.satisfiedConstraints / variables.subject_to_const
        """------------MUPE-------------"""
        myGoal = ref.Goal(objVal,constraintSatisfiedRate,variables.maxDeviatedConst,item1,item2,item3)
        """------------MUPE-------------"""
        ImpYes = False

        trainSet[i, variables.num_var] = myGoal
        if variables.objective == "Min":
            if variables.holdBest[variables.num_var + 4] > myGoal: #in case of improvement
                ImpYes = True
        else:
            if variables.holdBest[variables.num_var + 4] < myGoal:
                ImpYes = True
        if ImpYes == True:
            bestOrderId = i + 1
            bestGoalValue = myGoal
            bestObjVal = objVal
            TotalError = variables.maxDeviatedConst
            for j in range(0, variables.num_var):
                variables.previousBest[j] = variables.holdBest[j]
                variables.holdBest[j] = trainSet[i, j]
                CurrentInterval[3][j] = trainSet[i, j]
            variables.previousBest[variables.num_var] = variables.holdBest[variables.num_var]
            variables.previousBest[variables.num_var + 1] = variables.holdBest[variables.num_var + 1]
            variables.previousBest[variables.num_var + 2] = variables.holdBest[variables.num_var + 2]
            variables.previousBest[variables.num_var + 3] = variables.holdBest[variables.num_var + 3]
            variables.previousBest[variables.num_var + 4] = variables.holdBest[variables.num_var + 4]
            variables.previousBest[variables.num_var + 5] = variables.holdBest[variables.num_var + 5]

            variables.holdBest[variables.num_var] = bestOrderId
            variables.holdBest[variables.num_var + 1] = bestObjVal
            variables.holdBest[variables.num_var + 2] = constraintSatisfiedRate
            variables.holdBest[variables.num_var + 3] = TotalError
            variables.holdBest[variables.num_var + 4] = bestGoalValue
            variables.holdBest[variables.num_var + 5] = variables.set_size
        DataTableTrain[i, variables.num_var + 5] = myGoal
        DataTableConst[i, 0] = i + 1
        DataTableSlacks[i, 0] = i + 1

        for j in range(0, variables.subject_to_const + 1):
            DataTableConst[i, j + 1] = trainSetonConstraints[1, j]

    return myGoal,variables.constraintSatisfiedRate,variables.maxDeviatedConst  #outputs of MUPE

