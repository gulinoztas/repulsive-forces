import numpy as np
import determine_intervals
import random_set
from evaluate_constraints import EvaluateConstraint
CurrentSolution = np.zeros(determine_intervals.num_var-1)

for i in range(0,random_set.rand_set_size):
    for j in range(0,determine_intervals.num_var):
        CurrentSolution[j] = random_set.myRandomDataTableTrain[i,j+2]
    """-------evaluate constraint fonksiyonu------"""
    EvaluateConstraint(CurrentSolution,i)

myDataGridRandomConst.DataSource = myRandomDataTableConst
myDataGridRSlacks.DataSource = myDataTableSlacks