import variables
#from rsab_v2 import *
from rsab_v3 import *
#from atomvb import *

def UpdateBests(k,kth):
    from Best_Three import Best_Three
    ImpYes = False
    if variables.objective ==  "Min":
        ImpYes = True if variables.bestfit[k]-variables.fitness[k]>0 else False #check the improvement
    else:
        ImpYes = True if variables.bestfit[k] - variables.fitness[k] < 0 else False
    if ImpYes == True:
        if variables.initial==1:
            Best_Three(k) #saving best three candidate solutions
        else:
            if variables.objective == "Min":
                if variables.fitness[k] < variables.selectNewBest[0, 1]:
                    Best_Three(k) #saving best three candidate solutions
            else:
                if variables.fitness[k] > variables.selectNewBest[0, 1]:
                    Best_Three(k) #saving best three candidate solutions
        variables.boolImprovement = True
        variables.bestfit[k] = variables.fitness[k] #fitness values of best-so-far solutions
        variables.bestpos[k, :] = [variables.position[k,l] for l in range(0,variables.dimension)] #positions of best-so-far solutions
        ImpYes = False
        if variables.objective == "Min":
            ImpYes = True if variables.bestfit[variables.gbest] > variables.bestfit[k] else False
        else:
            ImpYes = True if variables.bestfit[variables.gbest] < variables.bestfit[k] else False
        if ImpYes == True:
            variables.gbest = k #assigning the rank number of the best-so-far among all population
            for i in range(0,variables.dimension):
                variables.CurrentInterval[i][3] = variables.bestpos[k, i]
            variables.TrackBarForceIt = variables.TrackBarForceIt+1 if variables.TrackBarForceIt<10 else 10 #a parameter used in Relocate for alpha calculation
    else:
        variables.boolImprovement = False
    return


