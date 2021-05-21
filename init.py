import variables
import numpy as np
from rsab_v3 import *
import UpdateBests
from atomvb import *
import matplotlib.pyplot as plt
def init(item1,item2,item3,kth):
    variables.initial=+1
    GraviationCorrection = 1
    variables.set_size = variables.rand_set_size #Update the set size

    for k in range(0,variables.set_size):
        test = np.array([[(rsab(variables.num_var, variables.num_const, variables.lowerlimit,variables.upperlimit, variables.set_size,variables.textboxiterations).generate(j, variables.CurrentInterval)) for j in range(0, variables.dimension)]]) #generating initial population
        variables.position[k,:] = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit, variables.set_size,variables.textboxiterations).check_database(variables.CurrentInterval,variables.position,test,k) #controlling duplication in the initial population

    if variables.textboxiterations != 0: #in case of RSAB is employed
        variables.position[0, :] = variables.holdBest[0:variables.num_var] #best-so-far solution is used in REF Algorithm

    variables.bestpos = variables.position.copy() #copy best population
    variables.fitness = np.array([[atom(variables.num_var, variables.num_const, variables.lowerlimit,variables.upperlimit, variables.set_size,variables.textboxiterations).WorstValue()] for i in range(0, variables.set_size)]) #default fitness matrix
    variables.bestfit = np.array([[atom(variables.num_var, variables.num_const, variables.lowerlimit,variables.upperlimit, variables.set_size,variables.textboxiterations).WorstValue()] for i in range(0, variables.set_size)]) #default bestfit matrix


    if variables.objective == "Min":
        variables.selectNewBest = np.array([[variables.set_size, 1e+100], [variables.set_size, 1e+100], [variables.set_size,1e+100]])   #to select best three candidate
    else:
        variables.selectNewBest = np.array([[variables.set_size, -1e+100], [variables.set_size, -1e+100], [variables.set_size, -1e+100]])

    for k in range(0,variables.set_size):
        if k == 0: #first particle in the population
            if variables.textboxiterations != 0: #in case of RSAB is employed
                variables.fitness[k] = variables.holdBest[variables.num_var + 4] #best-so-far coming from RSAB
                variables.satisfaction[k] = np.array([variables.holdBest[variables.num_var + 2], variables.holdBest[variables.num_var + 3], variables.holdBest[variables.num_var + 1]])
            else: #in case of RSAB is not employed
                tempgoal = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit,variables.set_size, variables.textboxiterations).Fun(k, variables.position[k][0:variables.num_var], item1, item2, item3)[2] #Fitness value calculated in MUPE
                variables.fitness[k] = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit,variables.set_size, variables.textboxiterations).f1(tempgoal,variables.fitness[k]) #objective value, maximum deviation, constraint satisfaction rate
                variables.satisfaction[k] = np.array([variables.constraintSatisfiedRate,variables.maxDeviatedConst,variables.objVal])
        else:
            tempgoal = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit, variables.set_size,variables.textboxiterations).Fun(k, variables.position[k][0:variables.num_var], item1, item2, item3)[2] #Fitness value calculated in MUPE
            variables.fitness[k] = atom(variables.num_var, variables.num_const, variables.lowerlimit,variables.upperlimit, variables.set_size, variables.textboxiterations).f1(tempgoal, variables.fitness[k]) #objective value, maximum deviation, constraint satisfaction rate
            variables.satisfaction[k] = np.array([variables.constraintSatisfiedRate, variables.maxDeviatedConst, variables.objVal])

        UpdateBests.UpdateBests(k,kth) #updating best-so-far solutions

    variables.selectNewBest = variables.selectNewBest[np.argsort(variables.selectNewBest[:, 1])]   #sort best three candidate solutions.
    """--------------CREATE DATABASE-----------------"""
    variables.database = np.zeros((variables.set_size, variables.dimension + 4))
    variables.database[:,0:variables.dimension] = variables.position[:]
    variables.database[:,variables.dimension]= np.transpose(variables.fitness[:])
    variables.database[:,variables.dimension+1:variables.dimension+4]=variables.satisfaction[:]
    """--------------CREATE DATABASE-----------------"""


    return

