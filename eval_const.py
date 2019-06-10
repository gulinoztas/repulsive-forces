import determine_intervals
import numpy as np
import goal
import random_set
import trackBarObjVal
import obj_func_val
import trackBarObjVal
import pandas as pd
MinValue = -1.7976931348623157E+308
MaxValue = 1.7976931348623157E+308
Calculated_Goals = np.array(())
holdbesttt = np.array(())
for i in range(0,random_set.train):

    holdBest = np.zeros(determine_intervals.num_var+5)
    ImpYes = False
    MaxValue = 1.7976931348623157E+308
    MinValue = -1.7976931348623157E+308
    numIterations = 0
    j=0
    objective = "Min"
    constraintSatisfiedRate = obj_func_val.slacks_table.iloc[i,determine_intervals.num_constraints+1]
    #print("satisfied",constraintSatisfiedRate)
    maxDeviatedConst = obj_func_val.randoms.iloc[i,determine_intervals.num_constraints-1]
    objVal = obj_func_val.objective[i]
    #print("holdbest",holdBest)
    print("satisfied rate",obj_func_val.slacks_table.iloc[i,determine_intervals.num_constraints+1],"deviation",obj_func_val.randoms.iloc[i,determine_intervals.num_constraints-1],"objval",obj_func_val.objective[i])

    if holdBest[0]== 0:
        for item in range(0,determine_intervals.num_var+5):
            holdBest[item]=MaxValue if objective =="Min" else MinValue
        #print("holdbest",holdBest)
    #print("maxdeviation",maxDeviatedConst)
    Calculate_Goal = goal.Goal(constraintSatisfiedRate,maxDeviatedConst,objVal,trackBarObjVal.valTrackBarObjVal)
    Calculated_Goals = np.append(Calculated_Goals,Calculate_Goal)
    #print("Calculated Goal",Calculate_Goal)
    #random_set.trainSet[i,4]=Calculate_Goal
    random_set.trainset_table.iloc[i,determine_intervals.num_var] = Calculate_Goal
    #print("CALCULATE GOAL",Calculate_Goal)
    #print(random_set.trainset_table)

#print(random_set.trainset_table)

    if objective == "Min":
        if holdBest[determine_intervals.num_var+4] > Calculate_Goal:
            ImpYes = True
    else:
        if holdBest[determine_intervals.num_var+4] < Calculate_Goal:
            ImpYes = True


    if ImpYes == True:
        bestOrderId = i+1
        bestGoalValue = Calculate_Goal
        bestObjVal = obj_func_val.randoms.iloc[i,determine_intervals.num_var+2]
        TotalError = obj_func_val.randoms.iloc[i,determine_intervals.num_var+4]
        print("bestorderıd", bestOrderId,"best goal",bestGoalValue,"best obj val",bestObjVal,"total error",TotalError)


        for j in range(0,determine_intervals.num_var):
            holdBest[j]=random_set.trainset_table.iloc[i,j]
            determine_intervals.Intervals.iloc[j,3] = random_set.trainset_table.iloc[i,j]
        print(determine_intervals.Intervals,"holdbest",holdBest)
        print("fefe",random_set.trainset_table)

        holdBest[determine_intervals.num_var] = bestOrderId
        holdBest[determine_intervals.num_var+1] = bestObjVal
        holdBest[determine_intervals.num_var+2] = constraintSatisfiedRate
        holdBest[determine_intervals.num_var+3] = TotalError
        holdBest[determine_intervals.num_var+4] = bestGoalValue

        numIterations = 0
        numIterations += 1
        holdbesttt = np.append(holdbesttt,holdBest)

    print("calculate goal", Calculate_Goal)
holdbest = holdbesttt.reshape(50,9)
#print("son durum",deneme)


holdBestt = pd.DataFrame(data=holdbest, index=None,columns=["x1","x2","x3","x4","best order ID","best obj val","constraint satisfied rate","total error","best goal value"])
#export_excel = holdBestt.to_excel(r'C:\Users\Pau\Google Drive\gülin Tez\holdbest.xlsx',index=None,header=True)
print(holdBestt)
MyRandomDataTableTrain = pd.DataFrame(data=obj_func_val.randoms)
MyRandomDataTableTrain.insert(determine_intervals.num_var + 5, "my Goal", Calculated_Goals)
print("My random datatable train",MyRandomDataTableTrain)
export_excel = MyRandomDataTableTrain.to_excel(r'C:\Users\Pau\Google Drive\gülin Tez\myrandomdatatabletrain.xlsx',index=None,header=True)