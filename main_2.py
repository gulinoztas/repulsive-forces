#import determine
from rsab_v3 import *
import pandas as pd
from statistics import *
from evaluate2 import *
import numpy as np
import variables
import itertools
def main_int(Interval,item1,item2,item3):

    ref = rsab(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit, variables.set_size,variables.textboxiterations)
    variables.CurrentInterval=Interval.copy()
    variables.update = 1

    if variables.textboxiterations!=0: #in case of RSAB algorithm is employed
        trainSet = np.zeros([variables.testcase, variables.num_var + 1])  #for 1000-sized initial population
        DataTableTrain = np.zeros([variables.testcase, variables.num_var + 6]) #for 1000-sized initial population
        DataTableConst = np.zeros([variables.testcase, variables.subject_to_const + 2]) #for 1000-sized initial population
        DataTableSlacks = np.zeros([variables.testcase, variables.subject_to_const + 2]) #for 1000-sized initial population
        variables.holdBest = list(itertools.chain([variables.MaxValue for i in range(0, variables.num_var + 6)])) if variables.objective == "Min" else list(itertools.chain([variables.MinValue for i in range(0, variables.num_var + 6)])) #initial best-so-far vector is created.
        """---------------1000-sized initial population-----------------"""
        for i in range(0, variables.testcase): #FOR ONCE
            myGoal = evaluate(variables.CurrentInterval,i,DataTableTrain,DataTableSlacks,DataTableConst,trainSet,item1,item2,item3)[0] #1000-sized initial population is created and evaluated with MUPE
        ek = min(DataTableTrain[:, variables.num_var + 5]) if variables.objective=="Min" else max(DataTableTrain[:, variables.num_var + 5]) #best-so-far solution among 1000-sized population
        res = [i for i, j in enumerate(DataTableTrain[:, variables.num_var + 5]) if j == ek]
        current_best_in_iteration = res[0]
        """---------------1000-sized initial population-----------------"""

        for t in range(1, variables.textboxiterations + 1): #Number of defined iterations
            if variables.holdBest[variables.num_var + 4] < DataTableTrain[current_best_in_iteration, variables.num_var + 5]: # in case of no improvement
                variables.CurrentInterval = Interval.copy()  #enlarge domains in case of no improvement
                variables.CurrentInterval[:][3] = variables.holdBest[0:variables.num_var] #assign best-so-far
                if len(variables.constrained)==0: #for unconstrained problems
                    variables.CurrentInterval = ref.update_interval3(variables.CurrentInterval, variables.holdBest) #update domains in terms of midpoint
                else: #for constrained problems
                    variables.CurrentInterval = ref.update_interval5(variables.CurrentInterval,variables.holdBest) #update domains in terms of holdbest
            else:  #in case of improvement
                if len(variables.constrained) == 0: #for unconstrained problems
                    variables.CurrentInterval = ref.update_interval5(variables.CurrentInterval, variables.holdBest) #update domains in terms of holdbest
                else: #for constrained problems
                    variables.CurrentInterval = ref.update_interval3(variables.CurrentInterval, variables.holdBest) #update domains in terms of midpoint

            """-------------increased-sized population-------------"""
            #trainSet = np.zeros([variables.set_size, variables.num_var + 1])
            #DataTableTrain = np.zeros([variables.set_size, variables.num_var + 6])
            #DataTableConst = np.zeros([variables.set_size, variables.subject_to_const + 2])
            #DataTableSlacks = np.zeros([variables.set_size, variables.subject_to_const + 2])
            """-------------increased-sized population-------------"""
            """---------------20-sized population------------------"""
            trainSet = np.zeros([variables.init_size, variables.num_var + 1]) #for 20-sized initial population
            DataTableTrain = np.zeros([variables.init_size, variables.num_var + 6]) #for 20-sized initial population
            DataTableConst = np.zeros([variables.init_size, variables.subject_to_const + 2]) #for 20-sized initial population
            DataTableSlacks = np.zeros([variables.init_size, variables.subject_to_const + 2]) #for 20-sized initial population
            """---------------20-sized population------------------"""
            for i in range(0, variables.init_size):  #variables.set_size
                evaluate(variables.CurrentInterval, i,DataTableTrain,DataTableSlacks,DataTableConst,trainSet,item1,item2,item3) #20-sized initial population is created and evaluated with MUPE
            ek = min(DataTableTrain[:, variables.num_var + 5]) if variables.objective=="Min" else max(DataTableTrain[:, variables.num_var + 5])#best-so-far solution among 20-sized population
            res = [i for i, j in enumerate(DataTableTrain[:, variables.num_var + 5]) if j == ek]
            current_best_in_iteration = res[0]

            if variables.holdBest[variables.num_var + 4] < DataTableTrain[current_best_in_iteration, variables.num_var + 5]: #no improvement
                variables.counter += 1
                variables.set_size += variables.increase #in case of no improvement set size is increased by the amount of increase
                variables.init_size += variables.increase
            else:
                variables.counter = variables.counter
                variables.bestInterval = variables.CurrentInterval #best interval

            variables.bound = np.transpose(variables.CurrentInterval[1:3, :]).reshape(1, 2 * variables.num_var)
            variables.boundary[t-1,0:variables.num_var*2] = variables.bound
            variables.boundary[t - 1, variables.num_var * 2] = variables.holdBest[variables.num_var + 4]
            variables.bound = np.array(())

        table = pd.DataFrame(data=variables.boundary)
        table.to_excel(r'C:\Users\Pau\Google Drive\ref\totalintervals.xlsx') #saving location should be updated
        variables.CurrentInterval = pd.DataFrame(data=variables.CurrentInterval, index=None, columns=None)

        for k in range(0,variables.num_var*2,2):
            lower1 = mean(variables.boundary[:, k])
            lower2 = mode(variables.boundary[:,k])
            upper1 = mean(variables.boundary[:,k+1])
            upper2 = mode(variables.boundary[:,k+1])
            lower3 = median(variables.boundary[:, k])
            upper3 = median(variables.boundary[:,k+1])
            variables.CurrentInterval[k/2][1:3] = [min(lower1, lower2,lower3), max(upper1, upper2,upper3)] #the final updated domains
    else:  #in case of RSAB is not employed
        variables.holdBest = list(itertools.chain([variables.MaxValue for i in range(0, variables.num_var + 6)])) if variables.objective == "Min" else list(itertools.chain([variables.MinValue for i in range(0, variables.num_var + 6)]))  #initial best-so-far vector is created.
        variables.CurrentInterval = pd.DataFrame(data=variables.CurrentInterval, index=None, columns=None)
    variables.update = 0

    return variables.CurrentInterval


