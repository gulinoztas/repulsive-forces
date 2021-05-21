import variables
import numpy as np
import init
from atomvb import *
def findneighbors(k): #finds neighbors according to the distances
    variables.avgDistance = k * variables.set_size * variables.avgDistance
    iPopindex = k
    variables.temp = np.zeros((variables.set_size))
    import itertools
    if k==0:
        variables.iNeighbor = np.array(list(itertools.chain([np.zeros((variables.set_size, 2)) for i in range(0, variables.set_size)])))
    for jPopindex in range(0, variables.set_size):
        a = variables.bestpos[iPopindex]
        b = variables.bestpos[jPopindex]
        distance = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit,variables.set_size, variables.textboxiterations).calculateDistance(variables.bestpos[iPopindex], variables.bestpos[jPopindex])
        variables.avgDistance += distance
        if math.isnan((variables.position[jPopindex, 0])):
            print("Dur3")
        if iPopindex != jPopindex:
            variables.iNeighbor[iPopindex][jPopindex, 0:2] = [jPopindex,(distance ** 2) / (((variables.bestfit[iPopindex] *variables.bestfit[jPopindex]) + 0.000000000000000000000000000001))] if variables.objective == "Min" else [jPopindex,1 / ((variables.bestfit[iPopindex] * variables.bestfit[jPopindex]) / distance ** 2)]
        else:
            variables.iNeighbor[iPopindex][jPopindex, 0:2] = [jPopindex,1e+300] if variables.objective == "Min" else [jPopindex,1E+300]

        variables.temp[jPopindex] = jPopindex

    variables.iNeighbor[iPopindex] = variables.iNeighbor[iPopindex][np.argsort(variables.iNeighbor[iPopindex][:,1])]
    variables.avgDistance = variables.avgDistance / ((k + 1) * variables.set_size)

    return
