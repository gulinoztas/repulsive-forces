import createrandomset
import numpy as np
import determine_intervals
import math


sets = createrandomset.values
objective = np.array(())
col = np.array(())
col2=np.array(())
for j in range(0,len(sets)):
    print(sets[j])
    obj = (0.6224 * sets[j,0] * sets[j,2] * sets[j,3] + 1.7781 * sets[j,1] * sets[j,2] ** 2 + 3.1661 * sets[j,0] ** 2 * sets[j,3] + 19.84 * sets[j,0] ** 2 * sets[j,2])
    #obj = 20+math.exp(1)-20*math.exp(-0.2*(0.2*(sets[j,0]**2+sets[j,1]**2+sets[j,2]**2+sets[j,3]**2+sets[j,4]**2))**0.5)-math.exp(0.2*(math.cos(2*3.14159265358979*sets[j,0])+ math.cos(2*3.14159265358979*sets[j,1])+ math.cos(2*3.14159265358979*sets[j,2])+ math.cos(2*3.14159265358979*sets[j,3])+ math.cos(2*3.14159265358979*sets[j,4])))     #ackley amaç fonk
    #objective = np.append(objective,obj)    #her random değerlerini amaç fonksiyonunda yerine koyar ve değerleri ekleyerek devam eder.
    #print(obj)
    sum=0
    for i in range(0, determine_intervals.num_constraints):

        lhs = determine_intervals.constraint[i][0]
        if i == 0:
            lhs = -sets[j, 0] + 0.0193 * sets[j, 2]
            # print(lhs)
            if lhs <= float(determine_intervals.constraint[i][2]):
                sat =1
                print(lhs, sat)
            else:
                sat=0
                print(lhs, sat)

        if i == 1:
            lhs = -sets[j, 1] + 0.0193 * sets[j, 2]
            # print(lhs)
            if lhs <= float(determine_intervals.constraint[i][2]):
                sat=1
                print(lhs, sat)
            else:
                sat = 0
                print(lhs, sat)

        if i == 2:
            lhs = 3.14159265359 * sets[j, 2] ** 2 * sets[j, 3] + 4 / 3 * 3.14159265359 * sets[j, 2] ** 3
            # print(lhs)
            if lhs >= float(determine_intervals.constraint[i][2]):
                sat = 1
                print(lhs, sat)
            else:
                sat = 0
                print(lhs, sat)

        if i == 3:
            lhs = sets[j, 3]
            # print(lhs)
            if lhs <= float(determine_intervals.constraint[i][2]):
                sat = 1
                print(lhs,sat)
            else:
                sat = 0
                print(lhs, sat)

        if i == 4:
            lhs = sets[j, 0]
            # print(lhs)
            if lhs <= float(determine_intervals.constraint[i][2]):
                sat = 1
                print(lhs, sat)
            else:
                sat = 0
                print(lhs, sat)

        if i == 5:
            lhs = sets[j, 1]
            #print(lhs)
            if lhs <= float(determine_intervals.constraint[i][2]):
                sat = 1
                print(lhs, sat)
            else:
                sat = 0
                print(lhs, sat)

        if i == 6:
            lhs = sets[j, 2]
            # print(lhs)
            if lhs <= float(determine_intervals.constraint[i][2]):
                sat = 1
                print(lhs, sat)
            else:
                sat = 0
                print(lhs, sat)

        if i == 7:
            lhs = sets[j, 0]
            #print(lhs)
            if lhs >= float(determine_intervals.constraint[i][2]):
                sat = 1
                print(lhs,sat)
            else:
                sat = 0
                print(lhs, sat)

        if i == 8:
            lhs = sets[j, 1]
            if lhs >= float(determine_intervals.constraint[i][2]):
                sat = 1
                print(lhs, sat)
            else:
                sat = 0
                print(lhs, sat)
        if sat==1:
            sum+=1
    print(sum)
    if sum != determine_intervals.num_constraints:
        satisfied = "1"
        print("Unsatisfied")
    else:
        satisfied="0"
        print("Satisfied")




    #obj_func_values = objective.reshape(len(sets), 1)   #hesaplanan değerleri şekillendirir.
    #obj_func_values = objective
    #table = np.append(sets,obj_func_values,axis = 1).reshape(len(sets),determine_intervals.num_var+1)     #tanımlanan random değerler ile bu değerler kullanılarak hesaplanan amaç fonksiyonu değerlerini tek tabloda verir.
    #table = np.append(sets, obj, axis=1).reshape(len(sets), determine_intervals.num_var + 1)
    #table = np.append(table,lhs,axis = 2)
    #print(obj_func_values)
    #print(table)
    



