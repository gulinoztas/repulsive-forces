import variables
from atomvb import *
from AddNewBest import AddNewBest

def Best_Three(k):
    """
    if variables.initial==1:
        variables.tempDist = variables.avgDistance if variables.avgDistance > 0 else 0.5
        for m in range(0, 3):
            if variables.selectNewBest[m, 1] == atom(variables.num_var, variables.num_const, variables.lowerlimit,
                                                     variables.upperlimit, variables.set_size,
                                                     variables.textboxiterations).WorstValue():
                continue
            variables.tempDist = atom(variables.num_var, variables.num_const, variables.lowerlimit,
                                      variables.upperlimit, variables.set_size,
                                      variables.textboxiterations).calculateRelativeDistance(variables.position[k],
                                                                                             variables.bestpos[int(
                                                                                                 variables.selectNewBest[
                                                                                                     m, 0]) - 1])
            variables.tempAngle = atom(variables.num_var, variables.num_const, variables.lowerlimit,
                                       variables.upperlimit, variables.set_size,
                                       variables.textboxiterations).calculateAngle(variables.position[k],
                                                                                   variables.bestpos[int(
                                                                                       variables.selectNewBest[
                                                                                           m, 0]) - 1])
            if variables.tempDist < 0.5 and variables.tempAngle < 0.05:
                variables.similarDist = True
                variables.pointerToDist = m
        for m in range(0, 3):
            if variables.selectNewBest[m, 0] == variables.set_size:
                continue
            if variables.selectNewBest[m, 0] == k:
                variables.sameK = True
                variables.pointerToK = m
        if variables.objective == "Min":
            a = variables.fitness[k] < variables.selectNewBest[2, 1]
            b = variables.fitness[k] < variables.selectNewBest[1, 1]
            c = variables.fitness[k] < variables.selectNewBest[0, 1]
        else:
            a = variables.fitness[k] > variables.selectNewBest[2, 1]
            b = variables.fitness[k] > variables.selectNewBest[1, 1]
            c = variables.fitness[k] > variables.selectNewBest[0, 1]
        if variables.similarDist == False and variables.sameK == False:
            if a:
                variables.selectNewBest[0, 0] = variables.selectNewBest[1, 0]
                variables.selectNewBest[0, 1] = variables.selectNewBest[1, 1]
                variables.selectNewBest[1, 0] = variables.selectNewBest[2, 0]
                variables.selectNewBest[1, 1] = variables.selectNewBest[2, 1]
                variables.selectNewBest[2, 0] = k
                variables.selectNewBest[2, 1] = variables.fitness[k]

            elif b:
                variables.selectNewBest[0, 0] = variables.selectNewBest[1, 0]
                variables.selectNewBest[0, 1] = variables.selectNewBest[1, 1]
                variables.selectNewBest[1, 0] = k
                variables.selectNewBest[1, 1] = variables.fitness[k]
            elif c:
                variables.selectNewBest[0, 0] = k
                variables.selectNewBest[0, 1] = variables.fitness[k]
        elif variables.sameK and variables.similarDist:
            if variables.objective == "Min":
                h = variables.fitness[k] < variables.selectNewBest[variables.pointerToK, 1]
            else:
                h = variables.fitness[k] > variables.selectNewBest[variables.pointerToK, 1]
            if h:
                variables.selectNewBest[variables.pointerToK, 0] = k
                variables.selectNewBest[variables.pointerToK, 1] = variables.fitness[k]
                for m in range(0, 3):
                    # if m != variables.pointerToK and variables.calculateRelativeDistance[variables.position[k],variables.bestpos[int(variables.selectNewBest[m,0])-1]] < 0.5: #variables.bestpos[int(variables.selectNewBest[m,0])-1]
                    if m != variables.pointerToK and atom(variables.num_var, variables.num_const, variables.lowerlimit,
                                                          variables.upperlimit, variables.set_size,
                                                          variables.textboxiterations).calculateRelativeDistance(
                            variables.position[k], variables.bestpos[int(variables.selectNewBest[
                                                                             m, 0]) - 1]) < 0.5:  # variables.bestpos[int(variables.selectNewBest[m,0])-1]
                        variables.selectNewBest[m, 0] = variables.set_size
                        variables.selectNewBest[m, 1] = atom(variables.num_var, variables.num_const,
                                                             variables.lowerlimit, variables.upperlimit,
                                                             variables.set_size,
                                                             variables.textboxiterations).WorstValue()
                        AddNewBest(m)
        elif variables.similarDist:
            if variables.objective == "Min":
                d = variables.fitness[k] < variables.selectNewBest[variables.pointerToDist, 1]
            else:
                d = variables.fitness[k] > variables.selectNewBest[variables.pointerToDist, 1]
            if d:
                variables.selectNewBest[variables.pointerToDist, 0] = k
                variables.selectNewBest[variables.pointerToDist, 1] = variables.fitness[k]
                for m in range(0, 3):
                    if variables.selectNewBest[m, 0] == k:
                        variables.selectNewBest[m, 0] = variables.set_size
                        variables.selectNewBest[m, 1] = atom(variables.num_var, variables.num_const,
                                                             variables.lowerlimit, variables.upperlimit,
                                                             variables.set_size,
                                                             variables.textboxiterations).WorstValue()
                        AddNewBest(m)
        elif variables.sameK:
            if variables.objective == "Min":
                e = variables.fitness[k] < variables.selectNewBest[variables.pointerToK, 1]
            else:
                e = variables.fitness[k] > variables.selectNewBest[variables.pointerToK, 1]
            if e:
                variables.selectNewBest[variables.pointerToK, 0] = k
                variables.selectNewBest[variables.pointerToK, 1] = variables.fitness[k]
                for m in range(0, 3):
                    if m != variables.pointerToK and atom(variables.num_var, variables.num_const, variables.lowerlimit,
                                                          variables.upperlimit, variables.set_size,
                                                          variables.textboxiterations).calculateRelativeDistance(
                            variables.position[k], variables.bestpos[int(variables.selectNewBest[m, 0]) - 1]) < 0.5:
                        variables.selectNewBest[m, 0] = variables.set_size
                        variables.selectNewBest[m, 1] = atom(variables.num_var, variables.num_const,
                                                             variables.lowerlimit, variables.upperlimit,
                                                             variables.set_size,
                                                             variables.textboxiterations).WorstValue()
                        AddNewBest(m)
        for m in range(0, 3):
            if variables.selectNewBest[m, 0] == variables.set_size:
                continue
            for n in range(0, 3):
                if variables.selectNewBest[n, 0] == variables.set_size:
                    continue
                if m != n:
                    variables.tempDist = atom(variables.num_var, variables.num_const, variables.lowerlimit,
                                              variables.upperlimit, variables.set_size,
                                              variables.textboxiterations).calculateRelativeDistance(
                        variables.bestpos[int(variables.selectNewBest[n, 0]) - 1],
                        variables.bestpos[int(variables.selectNewBest[m, 0]) - 1])
                    variables.tempAngle = atom(variables.num_var, variables.num_const, variables.lowerlimit,
                                               variables.upperlimit, variables.set_size,
                                               variables.textboxiterations).calculateAngle(
                        variables.bestpos[int(variables.selectNewBest[n, 0]) - 1],
                        variables.bestpos[int(variables.selectNewBest[m, 0]) - 1])
                    if variables.tempDist < 0.5 or variables.tempAngle < 0.05:
                        if variables.objective == "Min":
                            f = variables.selectNewBest[n, 1] < variables.selectNewBest[m, 1]
                        else:
                            f = variables.selectNewBest[n, 1] > variables.selectNewBest[m, 1]
                        if f:
                            variables.selectNewBest[m, 0] = variables.set_size
                            variables.selectNewBest[m, 1] = atom(variables.num_var, variables.num_const,
                                                                 variables.lowerlimit, variables.upperlimit,
                                                                 variables.set_size,
                                                                 variables.textboxiterations).WorstValue()
                            AddNewBest(m)
                        else:
                            variables.selectNewBest[n, 0] = variables.set_size
                            variables.selectNewBest[n, 1] = atom(variables.num_var, variables.num_const,
                                                                 variables.lowerlimit, variables.upperlimit,
                                                                 variables.set_size,
                                                                 variables.textboxiterations).WorstValue()
                            AddNewBest(m)
        variables.selectNewBest = variables.selectNewBest[np.argsort(variables.selectNewBest[:, 1])]
    else:
        if variables.objective=="Min":
            if variables.fitness[k]< variables.selectNewBest[0,1]:
                variables.tempDist = variables.avgDistance if variables.avgDistance>0 else 0.5
                for m in range(0, 3):
                    if variables.selectNewBest[m, 1] == atom(variables.num_var, variables.num_const, variables.lowerlimit,variables.upperlimit, variables.set_size,variables.textboxiterations).WorstValue():
                        continue
                    variables.tempDist = atom(variables.num_var, variables.num_const, variables.lowerlimit,variables.upperlimit, variables.set_size,variables.textboxiterations).calculateRelativeDistance(variables.position[k],variables.bestpos[int(variables.selectNewBest[m, 0]) - 1])
                    variables.tempAngle = atom(variables.num_var, variables.num_const, variables.lowerlimit,variables.upperlimit, variables.set_size,variables.textboxiterations).calculateAngle(variables.position[k],variables.bestpos[int(variables.selectNewBest[m, 0]) - 1])
                    if variables.tempDist < 0.5 and variables.tempAngle < 0.05:
                        variables.similarDist = True
                        variables.pointerToDist = m
                for m in range(0, 3):
                    if variables.selectNewBest[m, 0] == variables.set_size:
                        continue
                    if variables.selectNewBest[m, 0] == k:
                        variables.sameK = True
                        variables.pointerToK = m
                if variables.objective == "Min":
                    a = variables.fitness[k] < variables.selectNewBest[2, 1]
                    b = variables.fitness[k] < variables.selectNewBest[1, 1]
                    c = variables.fitness[k] < variables.selectNewBest[0, 1]
                else:
                    a = variables.fitness[k] > variables.selectNewBest[2, 1]
                    b = variables.fitness[k] > variables.selectNewBest[1, 1]
                    c = variables.fitness[k] > variables.selectNewBest[0, 1]
                if variables.similarDist == False and variables.sameK == False:
                    if a:
                        variables.selectNewBest[0, 0] = variables.selectNewBest[1, 0]
                        variables.selectNewBest[0, 1] = variables.selectNewBest[1, 1]
                        variables.selectNewBest[1, 0] = variables.selectNewBest[2, 0]
                        variables.selectNewBest[1, 1] = variables.selectNewBest[2, 1]
                        variables.selectNewBest[2, 0] = k
                        variables.selectNewBest[2, 1] = variables.fitness[k]

                    elif b:
                        variables.selectNewBest[0, 0] = variables.selectNewBest[1, 0]
                        variables.selectNewBest[0, 1] = variables.selectNewBest[1, 1]
                        variables.selectNewBest[1, 0] = k
                        variables.selectNewBest[1, 1] = variables.fitness[k]
                    elif c:
                        variables.selectNewBest[0, 0] = k
                        variables.selectNewBest[0, 1] = variables.fitness[k]
                elif variables.sameK and variables.similarDist:
                    if variables.objective == "Min":
                        h = variables.fitness[k] < variables.selectNewBest[variables.pointerToK, 1]
                    else:
                        h = variables.fitness[k] > variables.selectNewBest[variables.pointerToK, 1]
                    if h:
                        variables.selectNewBest[variables.pointerToK, 0] = k
                        variables.selectNewBest[variables.pointerToK, 1] = variables.fitness[k]
                        for m in range(0, 3):
                            # if m != variables.pointerToK and variables.calculateRelativeDistance[variables.position[k],variables.bestpos[int(variables.selectNewBest[m,0])-1]] < 0.5: #variables.bestpos[int(variables.selectNewBest[m,0])-1]
                            if m != variables.pointerToK and atom(variables.num_var, variables.num_const,variables.lowerlimit, variables.upperlimit,variables.set_size,variables.textboxiterations).calculateRelativeDistance(
                                    variables.position[k], variables.bestpos[int(variables.selectNewBest[m, 0]) - 1]) < 0.5:  # variables.bestpos[int(variables.selectNewBest[m,0])-1]
                                variables.selectNewBest[m, 0] = variables.set_size
                                variables.selectNewBest[m, 1] = atom(variables.num_var, variables.num_const,variables.lowerlimit, variables.upperlimit,variables.set_size,variables.textboxiterations).WorstValue()
                                AddNewBest(m)
                elif variables.similarDist:
                    if variables.objective == "Min":
                        d = variables.fitness[k] < variables.selectNewBest[variables.pointerToDist, 1]
                    else:
                        d = variables.fitness[k] > variables.selectNewBest[variables.pointerToDist, 1]
                    if d:
                        variables.selectNewBest[variables.pointerToDist, 0] = k
                        variables.selectNewBest[variables.pointerToDist, 1] = variables.fitness[k]
                        for m in range(0, 3):
                            if variables.selectNewBest[m, 0] == k:
                                variables.selectNewBest[m, 0] = variables.set_size
                                variables.selectNewBest[m, 1] = atom(variables.num_var, variables.num_const,variables.lowerlimit, variables.upperlimit,variables.set_size,variables.textboxiterations).WorstValue()
                                AddNewBest(m)
                elif variables.sameK:
                    if variables.objective == "Min":
                        e = variables.fitness[k] < variables.selectNewBest[variables.pointerToK, 1]
                    else:
                        e = variables.fitness[k] > variables.selectNewBest[variables.pointerToK, 1]
                    if e:
                        variables.selectNewBest[variables.pointerToK, 0] = k
                        variables.selectNewBest[variables.pointerToK, 1] = variables.fitness[k]
                        for m in range(0, 3):
                            if m != variables.pointerToK and atom(variables.num_var, variables.num_const,variables.lowerlimit, variables.upperlimit,variables.set_size,variables.textboxiterations).calculateRelativeDistance(variables.position[k], variables.bestpos[int(variables.selectNewBest[m, 0]) - 1]) < 0.5:
                                variables.selectNewBest[m, 0] = variables.set_size
                                variables.selectNewBest[m, 1] = atom(variables.num_var, variables.num_const,variables.lowerlimit, variables.upperlimit,variables.set_size,variables.textboxiterations).WorstValue()
                                AddNewBest(m)
                for m in range(0, 3):
                    if variables.selectNewBest[m, 0] == variables.set_size:
                        continue
                    for n in range(0, 3):
                        if variables.selectNewBest[n, 0] == variables.set_size:
                            continue
                        if m != n:
                            variables.tempDist = atom(variables.num_var, variables.num_const, variables.lowerlimit,variables.upperlimit, variables.set_size,variables.textboxiterations).calculateRelativeDistance(
                                variables.bestpos[int(variables.selectNewBest[n, 0]) - 1],
                                variables.bestpos[int(variables.selectNewBest[m, 0]) - 1])
                            variables.tempAngle = atom(variables.num_var, variables.num_const, variables.lowerlimit,variables.upperlimit, variables.set_size,variables.textboxiterations).calculateAngle(
                                variables.bestpos[int(variables.selectNewBest[n, 0]) - 1],
                                variables.bestpos[int(variables.selectNewBest[m, 0]) - 1])
                            if variables.tempDist < 0.5 or variables.tempAngle < 0.05:
                                if variables.objective == "Min":
                                    f = variables.selectNewBest[n, 1] < variables.selectNewBest[m, 1]
                                else:
                                    f = variables.selectNewBest[n, 1] > variables.selectNewBest[m, 1]
                                if f:
                                    variables.selectNewBest[m, 0] = variables.set_size
                                    variables.selectNewBest[m, 1] = atom(variables.num_var, variables.num_const,variables.lowerlimit, variables.upperlimit,variables.set_size,variables.textboxiterations).WorstValue()
                                    AddNewBest(m)
                                else:
                                    variables.selectNewBest[n, 0] = variables.set_size
                                    variables.selectNewBest[n, 1] = atom(variables.num_var, variables.num_const,variables.lowerlimit, variables.upperlimit,variables.set_size,variables.textboxiterations).WorstValue()
                                    AddNewBest(m)
                variables.selectNewBest = variables.selectNewBest[np.argsort(variables.selectNewBest[:, 1])]
    """
    variables.tempDist = variables.avgDistance if variables.avgDistance > 0 else 0.5
    for m in range(0,3):
        if variables.selectNewBest[m,1] == atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).WorstValue():
            continue
        variables.tempDist = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).calculateRelativeDistance(variables.position[k],variables.bestpos[int(variables.selectNewBest[m,0])-1])
        variables.tempAngle = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).calculateAngle(variables.position[k],variables.bestpos[int(variables.selectNewBest[m,0])-1])
        if variables.tempDist < 0.5 and variables.tempAngle < 0.05:
            variables.similarDist = True
            variables.pointerToDist = m
    for m in range(0, 3):
        if variables.selectNewBest[m,0] == variables.set_size:
            continue
        if variables.selectNewBest[m,0] == k:
            variables.sameK = True
            variables.pointerToK = m
    if variables.objective == "Min":
        a = variables.fitness[k] < variables.selectNewBest[2, 1]
        b = variables.fitness[k] < variables.selectNewBest[1, 1]
        c = variables.fitness[k] < variables.selectNewBest[0, 1]
    else:
        a = variables.fitness[k] > variables.selectNewBest[2, 1]
        b = variables.fitness[k] > variables.selectNewBest[1, 1]
        c = variables.fitness[k] > variables.selectNewBest[0, 1]
    if variables.similarDist == False and variables.sameK == False:
        if a:
            variables.selectNewBest[0, 0] = variables.selectNewBest[1, 0]
            variables.selectNewBest[0, 1] = variables.selectNewBest[1, 1]
            variables.selectNewBest[1, 0] = variables.selectNewBest[2, 0]
            variables.selectNewBest[1, 1] = variables.selectNewBest[2, 1]
            variables.selectNewBest[2, 0] = k
            variables.selectNewBest[2, 1] = variables.fitness[k]

        elif b:
            variables.selectNewBest[0, 0] = variables.selectNewBest[1, 0]
            variables.selectNewBest[0, 1] = variables.selectNewBest[1, 1]
            variables.selectNewBest[1, 0] = k
            variables.selectNewBest[1, 1] = variables.fitness[k]
        elif c:
            variables.selectNewBest[0, 0] = k
            variables.selectNewBest[0, 1] = variables.fitness[k]
    elif variables.sameK and variables.similarDist:
        if variables.objective == "Min":
            h = variables.fitness[k]< variables.selectNewBest[variables.pointerToK,1]
        else:
            h = variables.fitness[k] > variables.selectNewBest[variables.pointerToK, 1]
        if h:
            variables.selectNewBest[variables.pointerToK,0] = k
            variables.selectNewBest[variables.pointerToK,1] = variables.fitness[k]
            for m in range(0,3):
                #if m != variables.pointerToK and variables.calculateRelativeDistance[variables.position[k],variables.bestpos[int(variables.selectNewBest[m,0])-1]] < 0.5: #variables.bestpos[int(variables.selectNewBest[m,0])-1]
                if m != variables.pointerToK and atom(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit,variables.set_size, variables.textboxiterations).calculateRelativeDistance(variables.position[k], variables.bestpos[int(variables.selectNewBest[m, 0]) - 1]) < 0.5:  # variables.bestpos[int(variables.selectNewBest[m,0])-1]
                    variables.selectNewBest[m,0] = variables.set_size
                    variables.selectNewBest[m,1] = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).WorstValue()
                    AddNewBest(m)
    elif variables.similarDist:
        if variables.objective == "Min":
            d = variables.fitness[k]< variables.selectNewBest[variables.pointerToDist,1]
        else:
            d = variables.fitness[k]> variables.selectNewBest[variables.pointerToDist,1]
        if d:
            variables.selectNewBest[variables.pointerToDist,0] = k
            variables.selectNewBest[variables.pointerToDist, 1] = variables.fitness[k]
            for m in range(0,3):
                if variables.selectNewBest[m,0] == k:
                    variables.selectNewBest[m,0] = variables.set_size
                    variables.selectNewBest[m,1] = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).WorstValue()
                    AddNewBest(m)
    elif variables.sameK:
        if variables.objective == "Min":
            e = variables.fitness[k]< variables.selectNewBest[variables.pointerToK,1]
        else:
            e = variables.fitness[k]> variables.selectNewBest[variables.pointerToK,1]
        if e:
            variables.selectNewBest[variables.pointerToK,0] = k
            variables.selectNewBest[variables.pointerToK, 1] =variables.fitness[k]
            for m in range(0,3):
                if m!= variables.pointerToK and atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).calculateRelativeDistance(variables.position[k],variables.bestpos[int(variables.selectNewBest[m,0])-1])<0.5:
                    variables.selectNewBest[m,0] = variables.set_size
                    variables.selectNewBest[m,1] =atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).WorstValue()
                    AddNewBest(m)
    for m in range(0,3):
        if variables.selectNewBest[m,0] == variables.set_size:
            continue
        for n in range(0,3):
            if variables.selectNewBest[n,0]== variables.set_size:
                continue
            if m!=n:
                variables.tempDist = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).calculateRelativeDistance(variables.bestpos[int(variables.selectNewBest[n,0])-1],variables.bestpos[int(variables.selectNewBest[m,0])-1])
                variables.tempAngle = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations). calculateAngle(variables.bestpos[int(variables.selectNewBest[n,0])-1],variables.bestpos[int(variables.selectNewBest[m,0])-1])
                if variables.tempDist < 0.5 or variables.tempAngle < 0.05:
                    if variables.objective == "Min":
                        f = variables.selectNewBest[n,1]< variables.selectNewBest[m,1]
                    else:
                        f = variables.selectNewBest[n,1]> variables.selectNewBest[m,1]
                    if f:
                        variables.selectNewBest[m,0] = variables.set_size
                        variables.selectNewBest[m,1] = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).WorstValue()
                        AddNewBest(m)
                    else:
                        variables.selectNewBest[n,0] = variables.set_size
                        variables.selectNewBest[n,1] = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).WorstValue()
                        AddNewBest(m)
    if variables.initial==0:
        variables.selectNewBest = variables.selectNewBest[np.argsort(variables.selectNewBest[:, 1])]   #selectnewbestin 2. sütununa göre sıralıyor.
    #sortMyBest()
    #variables.tempArray[2,0]=variables.set_size
    #variables.tempArray[2, 1] = 1E+100


