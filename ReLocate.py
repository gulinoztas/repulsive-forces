import numpy as np
from atomvb import *
from rsab_v3 import *
import variables
import pandas as pd
import matplotlib.pyplot as plt
#import interval
from matplotlib import axes
from matplotlib.lines import Line2D
def ReLocate(k,DeltaX,kth,alpha,item1,item2,item3):

    alpha =(variables.TrackBarForceIt+10)*0.045
    myTempGoal = variables.fitness[k]

    for i in range(0,variables.dimension):
        tempPosition = variables.position[k,i]
        myDiv = abs(DeltaX[i]/(tempPosition+0.000000000000000000000000001)) #tanımsız olmasını engellemek için eklendi
        myTempGracCorr = abs(1/(myDiv+1))
        if DeltaX[i] != 0 and tempPosition!= 0:
            variables.GravitationCorrection = 1/(myDiv+0.0000000001)
        if float(variables.CurrentInterval[i][2])>=1e-30:  #0 olunca inf or nan çıkıyor.
            DeltaX[i] = (DeltaX[i]) % float(variables.CurrentInterval[i][2]) if DeltaX[i]>float(variables.CurrentInterval[i][2]) else DeltaX[i]
        else:
            DeltaX[i] =DeltaX[i]

        variables.test[k,i] = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).verify((tempPosition + DeltaX[i]) * alpha + (1 - alpha) * variables.bestpos[variables.gbest, i],i) #new location is calculated. (Eq.3.9))

    """------------------------------DATABASE CONTROL----------------------------------""" #saves the new location to the database
    if any(np.equal(variables.database[:,0:variables.dimension],variables.test[k,:]).all(1))==True:  #in case of the new location has not been visited previously.
        find = (np.equal(variables.database[:, 0:variables.dimension], variables.test[k, :]).all(1))
        r = [i for i, j in enumerate((find)) if j == True]
        indeks = r[0]
        if myTempGoal>variables.database[indeks,variables.dimension]:  #check whether the new location is better or no
            variables.position[k, :] = variables.test[k, :]
            variables.fitness[k] = variables.database[indeks,variables.dimension]
        else:
            variables.position[k, :] = variables.test[k, :]
            variables.fitness[k] = myTempGoal
    else:  #in case of the new location has been visited before
        test_fitness = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit, variables.set_size,variables.textboxiterations).Fun(k, variables.test[k, :], item1, item2, item3)[2]
        if test_fitness < myTempGoal:  #in case of improvement
            variables.position[k, :] = variables.test[k, :]
            variables.fitness[k] = test_fitness
            variables.satisfaction[k] = np.array([variables.constraintSatisfiedRate, variables.maxDeviatedConst, variables.objVal])
            new_list = np.array([np.append(variables.position[k, :], variables.fitness[k])])
            new_list = np.array([np.append(new_list, variables.satisfaction[k])])
            variables.database = np.concatenate((new_list, variables.database), axis=0)
        else:  #in case of no improvement
            variables.position[k, :] = variables.test[k, :]
            variables.fitness[k] = myTempGoal
            variables.satisfaction[k] = np.array([variables.constraintSatisfiedRate, variables.maxDeviatedConst, variables.objVal])
            new_list = np.array([np.append(variables.test[k, :], test_fitness)])
            new_list = np.array([np.append(new_list, variables.satisfaction[k])])
            variables.database = np.concatenate((new_list, variables.database), axis=0)
    """------------------------------------------------------------------------------------------"""
