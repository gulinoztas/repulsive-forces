import numpy as np
import determine_intervals
from myRandomVal import myRandomVal
import pandas as pd
import openpyxl
holdbest = np.zeros(determine_intervals.num_var+5)
rand_set_size = 50
train = rand_set_size
trainSet =np.zeros([train,determine_intervals.num_var])

myRandomDataTableTrain = np.zeros([train,determine_intervals.num_var+2])

"""-------------modify random train set-------------"""
for i in range(0,train):
    myRandomDataTableTrain[i,0]=i+1
    myRandomDataTableTrain[i,1]=1
    for j in range(0,determine_intervals.num_var):
        trainSet[i,j]= myRandomVal(j)
        myRandomDataTableTrain[i,j+2]=trainSet[i,j]
print(myRandomDataTableTrain)    #küsüratsız veriyor şuan round kullanıldığından
myRandomDataTable = pd.DataFrame(data=myRandomDataTableTrain, index=None,columns=["Order","Bias","x1","x2","x3","x4"])
print(myRandomDataTable)
export_excel = myRandomDataTable.to_excel(r'C:\Users\Pau\Google Drive\gülin Tez\random_table.xlsx',index=None,header=True)