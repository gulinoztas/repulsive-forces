from atomvb import *
from UpdateBests import UpdateBests
from ReLocate import ReLocate
def ForceIt(item1,item2,item3,myPosition,myfitness,k1,GravityMult,alpha,k2=-1,catalyst=False):

    distance = atom(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).calculateDistance(variables.bestpos[k1],myPosition) # Euclidean distance
    myGravityConst = variables.GravitationCorrection *10 **(int(variables.TrackBarForceIt)+GravityMult+math.floor(math.log10(distance+0.00000000000001)/math.log10(10))) #C constant
    Force = myGravityConst*(1/variables.bestfit[k1])*(1/myfitness)/(distance**2+0.00000000000001) if variables.objective == "Min" else variables.bestfit[k1]*myfitness/(distance+0.00000000000001)**2 #repulsive force

    variables.deltaXns = np.zeros((variables.num_var))

    for i in range(0,variables.dimension):  #the location difference is calculated as Delta for each variable
        variables.deltaXs = np.zeros((variables.num_var))
        SQRdifference = (variables.bestpos[k1,i]-myPosition[i])**2 / 1.0E+200 if distance ==0 else (variables.bestpos[k1,i]-myPosition[i])**2 /(distance**2+0.00000000000001)
        Force0 = Force * SQRdifference
        if variables.objective =="Min":
            DeltaX = Force0*1.0E+100 if variables.bestfit[k1]==0 else Force0*variables.bestfit[k1]
        else:
            DeltaX = Force0 / 1.0E+100 if variables.bestfit[k1] == 0 else Force0 / variables.bestfit[k1]
        if math.isnan(DeltaX) or math.isinf(DeltaX):
            print("dur12")

        if int(k2)!=variables.gbest or catalyst:
            DeltaX = -abs(DeltaX) if (variables.bestpos[k1,i]-myPosition[i])<0 else abs(DeltaX)
        else:
            DeltaX = abs(DeltaX) if (variables.bestpos[k1,i]-myPosition[i])<0 else -abs(DeltaX)
        variables.deltaXs[i]+= DeltaX

        if math.isinf(variables.deltaXs[i]):
            print("stopppp")

        variables.deltaXX[i] = variables.deltaXs[i]
        variables.deltaXns[i] = DeltaX

    ReLocate(k1, variables.deltaXns, 0, alpha,item1,item2,item3) #DISPLACEMENT (net force is calculated)
    UpdateBests(k1, 0) #updates best positions of particles

    if variables.boolImprovement: #continue updating until no improvement
        while variables.boolImprovement:
            ReLocate(k1,variables.deltaXns,0,alpha,item1,item2,item3)
            UpdateBests(k1,0)
            variables.deltaXns[:]+=[variables.deltaXns[i]*variables.incremental for i in range(0,variables.dimension)]

    return


