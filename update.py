from ForceIt import ForceIt
import variables
def update(item1,item2,item3,k1,k2,kth,alpha): #the repulsive forces of neighbors are calculated
    ForceIt(item1,item2,item3,variables.bestpos[int(k2)],variables.bestfit[int(k2)],k1,4,alpha,k2)
    return
