import numpy as np
import pandas as pd
holdBest = float()
"""
def initializeConstTables():
"""

#myRandomDataTableConst = pd.DataFrame(data=None, index=None, columns=["Order#"])
newcolumn = np.zeros((3))

myRandomDataTableConst = np.array(())
#myDataTableSlacks = pd.DataFrame(data=None, index=None, columns=None)
myDataTableSlacks = np.array((10,3))
randomSetSize = 20  #default
num_constraints = 10

for j in range(0,num_constraints):
    myRandomDataTableConst[j,0]=newcolumn[j]
    if j<num_constraints:
        myRandomDataTableConst[j,1]=newcolumn[j]
    else:
        myRandomDataTableConst[j,2]=newcolumn[j]
    myRandomDataTableConst = np.append(myRandomDataTableConst, newcolumn[j]).reshape((j + 1), len(newcolumn[j]))
myRandomDataTableConsts = pd.DataFrame(data=myRandomDataTableConst, index=None, columns=["Order#","Constraint","Satisfy"])
print(myRandomDataTableConsts)