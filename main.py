import numpy as np
import variables
from init import *
from findneighbors import *
from update import *
from ReLocate import *
from UpdateBests import *
from atomvb import *
from create import *
from export import *
import pandas as pd
from rsab_v3 import *
from check_duplication import check_duplication
from duplication import duplication
import main_2
import determine
from openpyxl.workbook import Workbook
"""----------------------------------------------------------"""

def Main(kth):
    Interval = determine.determine() #DETERMINE INTERVALS (determining domains of each variable)
    #atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit, variables.set_size,variables.textboxiterations).weights()   #OPTIONAL: The weights of MUPE can be normalized
    for trials in range(0,variables.trials):
        item1 = variables.weight1[0] #c1 in MUPE
        item2 = variables.weight2[0] #c2 in MUPE
        item3 = variables.weight3[0] #c3 in MUPE
        """----------RSAB Algorithm----------""" #optinal
        variables.CurrentInterval = main_2.main_int(Interval,item1,item2,item3) #RSAB ALGORITHM(OPTINAL: narrows determined intervals)
        print(variables.CurrentInterval)
        """------------------------"""
        variables.relocate_interval = Interval.copy()  # copy the initial determined intervals      #burası olucak
        variables.relocate_interval = pd.DataFrame(data=variables.relocate_interval)
       


        #variables.CurrentInterval = pd.DataFrame(data=variables.CurrentInterval, index=None, columns=None)
        #variables.relocate_interval = variables.CurrentInterval.copy()  #tez 21/04
        #variables.relocate_interval = pd.DataFrame(data=variables.relocate_interval) #tez 21/04

        """----------REF Algorithm-----------"""
        init.init(item1,item2,item3,kth) #INITIALIZATION: Generating initial population

        variables.TrackBarForceIt = 10 #initial value for the calculation of alpha in Relocate
        variables.loop = 0 #iteration in each trial

        allbest = np.zeros((variables.loop + 1, 1))  #to check improvement in fitness among loops
        allbest[variables.loop] = variables.bestfit[variables.gbest] #to check improvement in fitness among loops
        variables.b = variables.bestfit[variables.gbest]- variables.MaxValue #to check improvement in fitness among loops

        while variables.hitObj<variables.fe*variables.stop: #until stopping condition is met

            if abs(variables.bestfit[variables.gbest]) <= 1e-30: #if fitness value is lower than 1e-30 bypass REF algorithm
                break

            variables.loop +=1
            allbest = np.append(allbest,0)
            variables.neighborhoodsize = variables.GlobalNeighborhoodsize
            variables.boolImprovement = False
            variables.avgDistance = 0
            variables.impCounter = 0
            variables.iNeighbor=[]


            for k in range(0,variables.set_size):
                if k>0:
                    variables.fitness[k] = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).f(item1,item2,item3,variables.position[k],k,variables.fitness[k])[0]
                findneighbors(k) #the closest neighbors are defined for each candidate solution

                for neighbor in range(variables.neighborhoodsize):
                    variables.neigh+=1
                    update(item1,item2,item3,k,variables.iNeighbor[k][neighbor,0],kth,1) #new locations are determined according to the repulsive forces caused by neighbors

                    variables.impCounter += 1 if variables.boolImprovement == False else 0 if variables.impCounter<=0 else variables.impCounter-1
                    if variables.impCounter>=variables.set_size/10:
                        variables.TrackBarForceIt = variables.TrackBarForceIt-1 if variables.TrackBarForceIt> -10 else 0
                    if variables.impCounter > variables.worstHit:
                        variables.worstHit = variables.impCounter #worst so far

                ReLocate(k,variables.deltaXs,kth,1,item1,item2,item3)
                UpdateBests(k,kth)

            check_duplication(item1,item2,item3) #RSAB-REF #satisfies Pauli's exclusion principle
            #duplication(item1, item2, item3)    #REF
            """----------------------calculates improvement for successive iterations-------------------------"""
            variables.prebestfit[trials] = variables.bestfit[variables.gbest]
            if trials == 0:
                variables.a = (variables.prebestfit[trials] - variables.MaxValue)
            else:
                variables.a = (variables.prebestfit[trials] - variables.prebestfit[trials - 1])
            allbest[variables.loop] = variables.bestfit[variables.gbest]
            variables.b = (allbest[variables.loop]-allbest[variables.loop-1])
            if variables.b >= 0:
                variables.sayac+=1
                variables.fe = variables.hitObj if variables.sayac==1 else variables.fe
            elif variables.b<0:
                variables.sayac = 0
                variables.fe = 100000
            else:
                variables.sayac = variables.sayac
            print("trial",trials,"loop",variables.loop,"sayac",variables.sayac,"hitObj",variables.hitObj,"best",variables.bestfit[variables.gbest])
            if variables.hitObj>30000: #stopping condition (FES reached maxFES)
                break
            """-----------------------------------------------------------------------------------------------"""
        """-------------------------------------creates result tables---------------------------------------"""
        variables.tekrar = 0
        interval_table(trials,variables.init)   #creates interval table
        result_table(trials,variables.best_so_far) #creates final table
        variables.sayac = 1
        variables.hitObj = 0
        variables.database = pd.DataFrame(data=variables.database)
        excel(variables.database,variables.function+'database',variables.num_var,variables.set_size) #saves excel file
    variables.ave_table = average(variables.best_so_far)
    variables.ave_table = pd.DataFrame(data=variables.ave_table,index = ["Average"],columns=atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).title_result())
    variables.Intervals = pd.DataFrame(data=variables.init,index=None,columns=atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).title_interval())
    print(variables.Intervals)
    variables.Results = pd.DataFrame(data=variables.best_so_far, index=None, columns=atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).title_result())
    variables.Results = variables.Results.append(variables.ave_table)
    print(variables.Results)
    """------------------------------------------------------------------------------------------------------"""

    return

import time
start_time = time.time()
Main(1)
print("time:",time.time()-start_time)
excel(variables.Results,variables.function,variables.num_var,variables.set_size) #saves excel file (best-so-far solutions for each run)
excel(variables.Intervals,variables.function+'interval',variables.num_var,variables.set_size) #saves excel file (updated intervals)