import math
import trackBarObjVal
import obj_func_val
def Goal(constraintSatisfiedRate,maxDeviatedConst,objVal,valTrackBarObjVal):
    hitObj = 0
    hitObj +=1
    #constraintSatisfiedRate = obj_func_val.constraintSatisfiedRate
    #maxDeviatedConst=5
    goal1 = float()
    goal2 = float()
    goal3 = float()
    CurrentWeight1 = float()
    CurrentWeight2 = float()
    CurrentWeight3 = float()
    #objVal = obj_func_val.obj
    goalSign = 1 if objVal==float else abs(objVal)/objVal
    objective = "Min"


    if objective=="Min":
        goal1 = 1/((constraintSatisfiedRate+1.0E-100)**(1+CurrentWeight2))
        if goalSign == -1:
            goal1 = 1/goal1
        if abs(maxDeviatedConst)<200:
            goal2=1/math.exp(((goalSign*maxDeviatedConst)*(1+CurrentWeight3)))
        else:
            goal2=1.0E+100
        goal3 = (abs(objVal+0.000000000000001)**(CurrentWeight1+trackBarObjVal.valTrackBarObjVal))
        Goall = goalSign * goal1 * goal2 * goal3
    else:
        goal1 = (constraintSatisfiedRate+1.0E-100)**(1+CurrentWeight2)
        if goalSign == -1:
            goal1 = 1/goal1
        if abs(maxDeviatedConst)<200:
            goal2 = (math.exp(((goalSign)*maxDeviatedConst)*(1+CurrentWeight3)))
        else:
            goal2 = -1.0E+100
        goal3=abs(objVal)**(CurrentWeight1 + trackBarObjVal.valTrackBarObjVal)
        Goall = goalSign*goal1*goal2*goal3
    return Goall

