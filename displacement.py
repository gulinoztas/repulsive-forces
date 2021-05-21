import numpy as np
from atomvb import *
from rsab_v3 import *
import variables
import pandas as pd

def Displacement(k,item1,item2,item3,Interval2): #calculates net forces caused by the best-so-far solution in the population
    distance = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit,variables.set_size, variables.textboxiterations).calculateDistance(variables.bestpos[variables.gbest],variables.position[k])
    B = variables.TrackBarForceIt  # [-10,10]
    myGravityConst = variables.GravitationCorrection * 10 ** (int(variables.TrackBarForceIt) + 4 + math.floor(math.log10(distance + 0.00000000000001) / math.log10(10)))  # )+)+ math.floor(math.log10(abs(variables.bestfit[k1])) / math.log10(10)) + math.floor(math.log10(abs(myfitness))/math.log10(10))
    Force = myGravityConst * (1 / variables.bestfit[variables.gbest]) * (1 / variables.fitness[k]) / (distance ** 2 + 0.00000000000001) if variables.objective == "Min" else variables.bestfit[variables.gbest] * variables.fitness[k] / (distance + 0.00000000000001) ** 2
    for i in range(0, variables.dimension):
        SQRdifference = (variables.bestpos[variables.gbest, i] - variables.position[k,i]) ** 2 / 1.0E+200 if distance == 0 else (variables.bestpos[variables.gbest, i] -variables.position[k,i]) ** 2 / (distance ** 2 + 0.00000000000001)
        Force0 = Force * SQRdifference
        if variables.objective == "Min":
            DeltaX = Force0 * 1.0E+100 if variables.bestfit[variables.gbest] == 0 else Force0 * variables.bestfit[variables.gbest]
        else:
            DeltaX = Force0 / 1.0E+100 if variables.bestfit[variables.gbest] == 0 else Force0 / variables.bestfit[variables.gbest]
        if math.isnan(DeltaX) or math.isinf(DeltaX):
            print("dur12")
        DeltaX = abs(DeltaX) if (variables.bestpos[variables.gbest, i] - variables.position[k,i]) < 0 else -abs(DeltaX)
        variables.deltaXns[i] = DeltaX
    multiplier = 1
    alpha = (variables.TrackBarForceIt+10)*0.045
    myTempGoal = variables.fitness[k]
    for i in range(0,variables.dimension):
        tempPosition = variables.position[k,i]
        myDiv = abs(variables.deltaXns[i]/(tempPosition+0.000000000000000000000000001))
        myTempGracCorr = abs(1/(myDiv+1))
        if variables.deltaXns[i] != 0 and tempPosition!= 0:
            variables.GravitationCorrection = 1/(myDiv+0.0000000001)
        variables.deltaXns[i] = (variables.deltaXns[i]) % float(variables.CurrentInterval[i][2]) if variables.deltaXns[i] > float(variables.CurrentInterval[i][2]) else variables.deltaXns[i]
        variables.test[k,i] = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).verify((tempPosition + variables.deltaXns[i]) * alpha + (1 - alpha) * variables.bestpos[variables.gbest, i],i)
    variables.position[k, :] = atom(variables.num_var, variables.num_const, variables.lowerlimit,variables.upperlimit, variables.set_size,variables.textboxiterations).check_database(Interval2,variables.position, variables.test[k,:],k)
    """-----------------------------------------DATABASE CONTROL-------------------------------------------"""
    if any(np.equal(variables.database[:,0:variables.dimension],variables.position[k,:]).all(1))==True:
        find = (np.equal(variables.database[:, 0:variables.dimension], variables.test[k, :]).all(1))
        r = [i for i, j in enumerate((find)) if j == True]
        indeks = r[0]
        if myTempGoal>variables.database[indeks,variables.dimension]:
            variables.fitness[k] = variables.database[indeks,variables.dimension]
        else:
            variables.fitness[k] = myTempGoal
    else:
        test_fitness = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit, variables.set_size,variables.textboxiterations).Fun(k, variables.position[k, :], item1, item2, item3)[2]
        if test_fitness < myTempGoal:
            variables.fitness[k] = test_fitness
            variables.satisfaction[k] = np.array([variables.constraintSatisfiedRate, variables.maxDeviatedConst, variables.objVal])
            new_list = np.array([np.append(variables.position[k, :], variables.fitness[k])])
            new_list = np.array([np.append(new_list, variables.satisfaction[k])])
            variables.database = np.concatenate((new_list, variables.database), axis=0)
        else:
            variables.fitness[k] = myTempGoal
            variables.satisfaction[k] = np.array([variables.constraintSatisfiedRate, variables.maxDeviatedConst, variables.objVal])
            new_list = np.array([np.append(variables.test[k, :], test_fitness)])
            new_list = np.array([np.append(new_list, variables.satisfaction[k])])
            variables.database = np.concatenate((new_list, variables.database), axis=0)
    """---------------------------------------------------------------------------------------------------"""
