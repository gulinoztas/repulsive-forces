import variables
from atomvb import *
import pandas as pd
def check_duplication(item1,item2,item3):
    variables.check_dup+=1
    variables.check = variables.position.copy()
    freqDict = Counter(map(tuple, variables.check)) #the frequencies of candidate solutions in the population
    x = np.array(())
    s = 0
    for (row, freq) in freqDict.items():
        if freq > 1:
            s += 1
            x = np.concatenate((row, x), axis=0) #the list of particles occurred more than one.
    x = x.reshape(s, variables.num_var)
    variables.tekrar += len(x)
    variables.allow2 = 0
    while len(x) > 0:   #until the frequencies of the particles are at most one.
        if len(variables.constrained) == 0:
            variables.allow2+=1
            if variables.allow2>variables.set_size:  #for unconstrained problems. it has been restricted with set size so that it can exit the loop.
                break



        Interval2 = rsab(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit,variables.set_size, variables.textboxiterations).improve_interval2(variables.bestpos,Interval,variables.gbest) #the initial defined range is used to update intervals

        index = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit,variables.set_size, variables.textboxiterations).duplicated_index(x,variables.check)  #check the index of the duplicated particles
        for g in range(0, len(index)):
            if variables.g_best_update!=0:

                Interval2 = rsab(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit,variables.set_size, variables.textboxiterations).improve_interval2(variables.bestpos,Interval,variables.gbest) #the initial defined range is used to update intervals

            control = np.array([[(rsab(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit, variables.set_size, variables.textboxiterations).generate(j, Interval2)) for j in range(0, variables.dimension)]]) #duplicated particles is generated again within the new intervals
            control = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit, variables.set_size, variables.textboxiterations).truncate(control, variables.p) #locations are assumed as duplication in case of first three digits are the same
            variables.position[int(index[g]), :] = atom(variables.num_var, variables.num_const, variables.lowerlimit,variables.upperlimit, variables.set_size,variables.textboxiterations).check_database(variables.relocate_interval, variables.check, control, int(index[g])) #generate new particles until no duplication

            variables.allow = 0

            """------------------------------------DATABASE CONTROL----------------------------------------"""
            if any(np.equal(variables.database[:, 0:variables.dimension], variables.position[int(index[g]), :]).all(1)) == True:
                find = (np.equal(variables.database[:, 0:variables.dimension], variables.position[int(index[g]), :]).all(1))
                r = [i for i, j in enumerate((find)) if j == True]
                indeks = r[0]
                variables.fitness[int(index[g])] = variables.database[indeks, variables.dimension]

            else:
                tempGoal = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit,variables.set_size, variables.textboxiterations).f(item1, item2, item3,variables.position[int(index[g])],int(index[g]),variables.fitness[int(index[g])])[0]
                if variables.fitness[int(index[g])] != tempGoal:  # yeni nokta eski noktadan daha iyiyse
                    variables.fitness[int(index[g])] = tempGoal
                    variables.satisfaction[int(index[g])] = np.array([variables.constraintSatisfiedRate, variables.maxDeviatedConst, variables.objVal])
                    new_list = np.array([np.append(variables.position[int(index[g]), :], variables.fitness[int(index[g])])])
                    new_list = np.array([np.append(new_list, variables.satisfaction[int(index[g])])])
                    variables.database = np.concatenate((new_list, variables.database), axis=0)
                else:  # yeni nokta eski noktadan daha iyi değil ancak yine de o nokta database e kaydedilir.
                    fitness_database = atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit,variables.set_size, variables.textboxiterations).Fun(0, variables.position[int(index[g]), :],item1, item2, item3)[2]
                    variables.fitness[int(index[g])] = fitness_database
                    variables.satisfaction[int(index[g])] = np.array([variables.constraintSatisfiedRate, variables.maxDeviatedConst, variables.objVal])
                    new_list = np.array([np.append(variables.position[int(index[g]), :], fitness_database)])
                    new_list = np.array([np.append(new_list, variables.satisfaction[int(index[g])])])
                    variables.database = np.concatenate((new_list, variables.database), axis=0)
            """------------------------------------------------------------------------------------------"""
            if variables.fitness[int(index[g])] < variables.bestfit[int(index[g])]: #check whether the new location is better or not. (updates current best particles)
                variables.bestpos[int(index[g])] = variables.position[int(index[g])]
                variables.bestfit[int(index[g])] = variables.fitness[int(index[g])]
            find = min(variables.bestfit)
            r = [i for i, j in enumerate((variables.bestfit)) if j == find]
            best = r[0]
            variables.gbest = best
            if variables.fitness[int(index[g])] < variables.bestfit[variables.gbest]: #check whether best-so-far is changed or not.
                variables.g_best_update+=1
                variables.gbest = int(index[g])
                find = max(variables.bestfit)
                r = [i for i, j in enumerate((variables.bestfit)) if j == find]
                indeks = r[0]
                variables.bestfit[indeks] = variables.bestfit[variables.gbest]
                variables.bestpos[indeks] = variables.bestpos[variables.gbest]
                variables.bestfit[variables.gbest] = variables.fitness[int(index[g])]
                variables.bestpos[variables.gbest] = variables.bestpos[int(index[g])]
            else:
                variables.g_best_update = 0
        """-----------------duplication check---------------------""" #after updating duplicated particles (last control)
        variables.check = variables.position.copy()
        freqDict = Counter(map(tuple, variables.check))
        x = np.array(())
        s = 0
        for (row, freq) in freqDict.items():
            if freq > 1:
                s += 1
                x = np.concatenate((row, x), axis=0)
        x = x.reshape(s, variables.num_var)
        """-------------------------------------------------------"""
    return