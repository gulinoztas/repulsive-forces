import numpy as np
import determine_intervals
import random_set
import evaluate_constraints
import strToformula
import obj_func_val
import CalculateGoal
import goal
import trackBarObjVal
myObjVal = 1.0E+308
CurrentSolution = np.zeros(determine_intervals.num_var)
x=np.array(())
for i in range(0,random_set.rand_set_size):
    for j in range(0,determine_intervals.num_var):
        CurrentSolution[j] = random_set.myRandomDataTableTrain[i,j+2]
        #print("currentsolution",j,CurrentSolution[j])

    """-------evaluate constraint--------"""
    if myObjVal != 1.0E+308:
        objVal = myObjVal
    else:
        #objVal = strToformula.strToformula(obj_func_val.obj, determine_intervals.strVars, CurrentSolution)
        objVal = obj_func_val.objective[i]

    #print("obj val", objVal)




