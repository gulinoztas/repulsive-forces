import variables
from atomvb import *
from UpdateBests import UpdateBests
from displacement import Displacement
def duplication(item1,item2,item3): #checks duplicated particles
    variables.check = variables.position.copy()
    variables.check = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit, variables.set_size, variables.textboxiterations).truncate(variables.check, 6)
    freqDict = Counter(map(tuple, variables.check))
    x = np.array(())
    s = 0
    for (row, freq) in freqDict.items():
        if freq > 1:
            s += 1
            x = np.array(())
            x = np.concatenate((row, x), axis=0)
            find = (np.equal(variables.check[:, 0:variables.dimension], x).all(1))
            r = [i for i, j in enumerate((find)) if j == True]
            variables.deltaXns = np.zeros((variables.num_var))
            for g in range(0,len(r)-1):
                Interval2 = rsab(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit,variables.set_size, variables.textboxiterations).improve_interval2(variables.bestpos,variables.relocate_interval,variables.gbest)
                Displacement(int(r[g]), item1, item2, item3, variables.relocate_interval)
                UpdateBests(int(r[g]), 0)
                variables.deltaXns[:] += [variables.deltaXns[i] * 1.02 for i in range(0, variables.dimension)]
    return