import numpy as np
import determine_intervals
from myRandomVal import myRandomVal
import pandas as pd
import openpyxl
holdbest = np.zeros(determine_intervals.num_var+5)
rand_set_size = 50
train = rand_set_size
trainSet =np.zeros([train,determine_intervals.num_var+1])
#maxdeviation = np.zeros(train)
#goal = np.zeros(train)
myRandomDataTableTrain = np.zeros([train,determine_intervals.num_var+2])
myRandomDataTableConst = np.zeros([train,determine_intervals.num_var+4])
myDataTableSlacks = np.zeros([train,determine_intervals.num_constraints+2])
#print("slacks",myDataTableSlacks)
"""-------------modify random train set-------------"""
for i in range(0,train):
    myRandomDataTableTrain[i,0]=i+1
    myRandomDataTableTrain[i,1]=1
    for j in range(0,determine_intervals.num_var):
        trainSet[i,j]= myRandomVal(j)
        myRandomDataTableTrain[i,j+2]=trainSet[i,j]
#print("trainset",trainSet)
trainset_table = pd.DataFrame(data=trainSet,index=None,columns=["x1","x2","x3","x4","Goal"])
#print(trainset_table)
#print("myrandom datatable train",myRandomDataTableTrain)    #küsüratsız veriyor şuan round kullanıldığından
#rndDataTable = pd.DataFrame(data=myRandomDataTableTrain,index=None,columns=["order","bias","x1","x2"])
#rndDataTable.insert(4,"max deviated",maxdeviation)
#rndDataTable.insert(4,"my goal",goal)
myRandomDataTable = pd.DataFrame(data=myRandomDataTableTrain, index=None,columns=["Order","Bias","x1","x2","x3","x4"])
print(myRandomDataTable)
#print("datatable",rndDataTable)
#export_excel = myRandomDataTable.to_excel(r'C:\Users\Pau\Google Drive\gülin Tez\random_table.xlsx',index=None,header=True)