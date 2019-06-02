import createrandomset
import numpy as np
import determine_intervals
import pandas as pd

sets = createrandomset.values
objective = np.array(())
satisfied_constraint = np.array(())
total_error = np.array(())
const = np.array(())
satisfaction = np.array(())
s=np.array(())
for j in range(0, len(sets)):
    x1 = sets[j, 0]
    x2 = sets[j, 1]
    x3 = sets[j, 2]
    x4 = sets[j, 3]
    #print(sets[j])
    obj = (0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3)
    # obj = 20+math.exp(1)-20*math.exp(-0.2*(0.2*(sets[j,0]**2+sets[j,1]**2+sets[j,2]**2+sets[j,3]**2+sets[j,4]**2))**0.5)-math.exp(0.2*(math.cos(2*3.14159265358979*sets[j,0])+ math.cos(2*3.14159265358979*sets[j,1])+ math.cos(2*3.14159265358979*sets[j,2])+ math.cos(2*3.14159265358979*sets[j,3])+ math.cos(2*3.14159265358979*sets[j,4])))     #ackley amaç fonk
    # constraint = [["-x1+0.0193*x3","<=","0"], ["-x2+0.00954*x3","<=","0"],["3.14159265359*x3**2*x4+(4/3)*3.14159265359*x3**3",">=","1296000"], ["x4","<=","240"],["x1","<=","10"],["x2","<=","10"], ["x3","<=","100"],["x1",">=","0.0625"],["x2",">=","0.0625"]]

    sum = 0
    error = 0
    for i in range(0, determine_intervals.num_constraints):

        lhs=eval(determine_intervals.constraint[i][0])    #lhs her ksııtın sol yan değerini hesaplar.
        if determine_intervals.constraint[i][1] == "<=":          #küçük eşittir işaretli kısıtlar için
            if lhs <= float(determine_intervals.constraint[i][2]):    #kısıtı sağlıyorsa
                sat = 1
                slack = float(determine_intervals.constraint[i][2])-lhs
                #print("slack",slack)
                #print("left hand side:",lhs,"right hand side:",determine_intervals.constraint[i][2],"satisfied:",sat,"slack:",slack)
            else:      #kısıtı sağlamıyorsa
                sat = 0
                error = lhs-float(determine_intervals.constraint[i][2])
                #print("left hand side:",lhs,"right hand side:",determine_intervals.constraint[i][2],"satisfied:",sat,"error:",error)

        else:                 #büyük eşittir işaretli kısıtlar için
            if lhs >= float(determine_intervals.constraint[i][2]):    #kısıtı sağlıyorsa
                sat = 1
                slack = lhs -float(determine_intervals.constraint[i][2])
                #print("slack", slack)
                #print("left hand side:",lhs,"right hand side:",determine_intervals.constraint[i][2],"satisfied:",sat,"slack:",slack)
            else:         #kısıtı sağlamıyorsa
                sat = 0
                error = float(determine_intervals.constraint[i][2])-lhs
                #print("left hand side:",lhs,"right hand side:",determine_intervals.constraint[i][2],"satisfied",sat,"error:",error)
        #print("slack",slack)


        if sat == 1:
            sum += 1     #toplam satisfy edilen kısıt sayısını hesaplar
        else:
            error+=error     #toplam error u hesaplar
        satisfaction = np.append(satisfaction,sat)



    if sum != determine_intervals.num_constraints:     #eğer tüm kısıtlar sağlanmıyorsa
        satisfied = "0"
        #print("Result: Unsatisfied")
        s = np.append(s, satisfied)
    else:                               #tüm kısıtlar sağlanmışsa
        satisfied = "1"
        #print("Result:Satisfied")
        s = np.append(s, satisfied)
    #print(satisfied)
    #s=np.append(s,satisfied)


    # print("random:",sets[j],"Total satisfied constraint number",sum,"out of 9")
    satisfied_constraint = np.append(satisfied_constraint,sum)
    total_error = np.append(total_error,error)
    objective = np.append(objective,obj)


myDataTable = pd.DataFrame(data=sets, index=range(1,len(sets)+1),columns=["x1", "x2", "x3", "x4"])
myDataTable.insert(4,"objective value",objective)
myDataTable.insert(5,"satisfied cons",satisfied_constraint)
myDataTable.insert(6,"total error in rhs",total_error)
print(myDataTable)

#print(s)
const = satisfaction.reshape(20,9)
#print(const)
constraint_satisfaction = pd.DataFrame(data=const, index=range(1,len(sets)+1),columns=["Constraint1", "Constraint2", "Constraint3", "Constraint4", "Constraint5", "Constraint6", "Constraint7", "Constraint8", "Constraint9"])
constraint_satisfaction.insert(9,"Satisfy",s)
print(constraint_satisfaction)



