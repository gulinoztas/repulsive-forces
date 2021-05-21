import variables
from atomvb import *
def AddNewBest(m):
    for i in range(0,variables.set_size):
        if i!= variables.selectNewBest[0,0] and i!= variables.selectNewBest[1,0] and i!=variables.selectNewBest[2,0]:
            variables.tempAngle = 4
            variables.tempDist = 100
            for j in range(0,3):
                if j!=m:
                    if atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).calculateAngle(variables.bestpos[i],variables.bestpos[int(variables.selectNewBest[j,0])-1]) < variables.tempAngle and atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).calculateRelativeDistance(variables.bestpos[i],variables.bestpos[int(variables.selectNewBest[j,0])-1])< variables.tempDist:
                        variables.tempAngle = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).calculateAngle(variables.bestpos[i],variables.bestpos[int(variables.selectNewBest[j,0])-1])
                        variables.tempDist = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).calculateRelativeDistance(variables.bestpos[i],variables.bestpos[int(variables.selectNewBest[j,0])-1])
            if 0.05<variables.tempAngle<4 and 0.5<variables.tempDist<100 and variables.fitness[i]<variables.selectNewBest[m,1]:
                variables.selectNewBest[m,1] = variables.fitness[i]
                variables.selectNewBest[m,0] = i
