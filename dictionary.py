import collections
import math

"""--------------------------------------------BENCHMARK DATABASE------------------------------------------------"""
benchmarks = collections.namedtuple("benchmarks",["num_var","num_bound","lowerlimit","upperlimit","constraints","weights","constraints2"])
"""------------------------CONSTRAINED PROBLEMS---------------------------"""
Pressure = benchmarks(num_var=4,num_bound=8,lowerlimit=[0.0625,0.0625,0,0],upperlimit=[10,10,100,240],constraints=[["-x01+0.0193*x03","<=",0],["-x02+0.00954*x03","<=",0],["3.141592653559*x03**2*x04+(4/3)*3.141592653559*x03**3",">=",1296000]],weights=[2,10,10],constraints2=[["-x01+0.0193*x03","<=",0],["-x02+0.00954*x03","<=",0],["3.141592653559*x03**2*x04+(4/3)*3.141592653559*x03**3",">=",1296000]])
Himmelblau = benchmarks(num_var=5,num_bound=10,lowerlimit=[78,33,27,27,27],upperlimit=[102,45,45,45,45],constraints=[["85.334407+0.0056858*x02*x05+0.00026*x01*x04-0.0022053*x03*x05",">=",0],["80.51249+0.0071317*x02*x05+0.0029955*x01*x02+0.0021813*x03**2",">=",90],["9.300961+0.0047026*x03*x05+0.0012547*x01*x03+0.0019085*x03*x04",">=",20],["85.334407+0.0056858*x02*x05+0.00026*x01*x04-0.0022053*x03*x05","<=",92],["80.51249+0.0071317*x02*x05+0.0029955*x01*x02+0.0021813*x03**2","<=",110],["9.300961+0.0047026*x03*x05+0.0012547*x01*x03+0.0019085*x03*x04","<=",25]],weights=[2,10,10],constraints2=[["85.334407+0.0056858*x02*x05+0.00026*x01*x04-0.0022053*x03*x05",">=",0],["80.51249+0.0071317*x02*x05+0.0029955*x01*x02+0.0021813*x03**2",">=",90],["9.300961+0.0047026*x03*x05+0.0012547*x01*x03+0.0019085*x03*x04",">=",20],["85.334407+0.0056858*x02*x05+0.00026*x01*x04-0.0022053*x03*x05","<=",92],["80.51249+0.0071317*x02*x05+0.0029955*x01*x02+0.0021813*x03**2","<=",110],["9.300961+0.0047026*x03*x05+0.0012547*x01*x03+0.0019085*x03*x04","<=",25]])
WeldedBeam = benchmarks(num_var=4,num_bound=8,lowerlimit=[0.125,0.1,0.1,0.1],upperlimit=[5,10,10,5], constraints=[["(18000000*8*((x02**2)/12+((x01+x03)/2)**2)**2*((x02**2)/4+((x01+x03)/2)**2)**0.5+1500*x02*(84000+3000*x02)*((x02**2)/4+((x01+x03)/2)**2)**0.5*8*((x02**2)/12+((x01+x03)/2)**2)+(84000+3000*x02)**2*((x02**2)/4+((x01+x03)/2)**2)*(((x02**2)/4+((x01+x03)/2)**2))**0.5)-(184960000*(8*x01**2*x02**2*((x02**2)/12+((x01+x03)/2)**2)**2*((x02**2)/4+((x01+x03)/2)**2)**0.5))","<=",0],["x04*(x03**2)",">=",16.8],["x01-x04","<=",0],["102372.449*x03*(x04**3)*(1-0.028234621*x03)",">=",6000],["(x03**3)*x04",">=",8.7808],["1.10471*(x01**2)+0.67354*x03*x04+0.04811*x02*x03*x04","<=",5]], weights=[2,10,10],constraints2=[["((6000/(2**0.5*x01*x02))**2+2*(6000/(2**0.5*x01*x02))*((6000*(14+x02/2))*((x02**2/4+((x01+x03)/2)**2)**0.5)/(2*(2**0.5*x01*x02*(x02**2/12+((x01+x03)/2)**2))))*x02/(2*(x02**2/4+((x01+x03)/2)**2)**0.5)+((6000*(14+x02/2))*((x02**2/4+((x01+x03)/2)**2)**0.5)/(2*(2**0.5*x01*x02*(x02**2/12+((x01+x03)/2)**2))))**2)**0.5","<=",13600],["6*6000*14/(x04*x03**2)","<=",30000],["x01-x04","<=",0],["1.1047*x01**2+0.04811*x03*x04*(14.0+x02)","<=",5],["4*6000*14**3/(30*10**6*x03**3*x04)","<=",0.25],["4.013*30*10**6*(x03**2*x04**6/36)**0.5/14**2*(1-x03/(2*14)*(30*10**6/(4*12*10**6))**0.5)",">=",6000]])
Tension = benchmarks(num_var=3,num_bound=6,lowerlimit=[0.05,0.25,2],upperlimit=[1,1.3,15],constraints=[["71785*x01**4-x02**3*x03","<=",0],["5108*x01**2*(4*x02**2-x01*x02)+12566*(x02*x01**3-x01**4)-5108*x01**2*12566*(x02*x01**3-x01**4)","<=",0],["x02**2*x03-140.45*x01","<=",0],["x01+x02","<=",1.5]],weights=[2,10,10],constraints2=[["1-((x02**3*x03)/(71785*x01**4))","<=",0],["(4*x02**2-x01*x02)/(12566*(x02*x01**3-x01**4))+1/(5108*x01**2)","<=",1],["1-((140.45*x01)/(x02**2*x03))","<=",0],["(x01+x02)/1.5","<=",1]]) #0.000001,0.5,0.52,10,101e-6,0.5,0.8
Dispatch = benchmarks(num_var=6,num_bound=12,lowerlimit=[0,81,40,0,0,0],upperlimit=[150,274,125.8,180,135.6,2695.2],constraints=[["x01+x02+x03","<=",200],["x04+x05+x06","<=",115],["x01+x02+x03",">=",200],["x04+x05+x06",">=",115],["1.781914894*x04-x02","<=",105.74468],["0.177778*x04+x02","<=",247],["1.1584*x05-x03","<=",46.8812],["0.151163*x05+x03","<=",130.6977],["0.16985*x04+x02",">=",98.8],["0.067682*x05+x03",">=",45.076142]],weights=[2,6,1.5],constraints2=[["x01+x02+x03","<=",200],["x04+x05+x06","<=",115],["x01+x02+x03",">=",200],["x04+x05+x06",">=",115],["1.781915*x04-x02","<=",105.74468],["0.177778*x04+x02","<=",247],["1.1584*x05-x03","<=",46.8812],["0.151163*x05+x03","<=",130.6977],["0.16985*x04+x02",">=",98.8],["0.067682*x05+x03",">=",45.076142]])
"""-----------------------UNCONSTRAINED PROBLEMS-------------------------"""
Mccormick = benchmarks(num_var=2,num_bound=4,lowerlimit=[-1.5,-3],upperlimit=[4,3],constraints=[],weights=[2,10,10],constraints2=[])
Bird = benchmarks(num_var=2,num_bound=4,lowerlimit=[-2*math.pi]*2,upperlimit=[2*math.pi]*2,constraints=[],weights=[2,10,10],constraints2=[])
Beale = benchmarks(num_var=2,num_bound=4,lowerlimit=[-4.5]*2,upperlimit=[4.5]*2,constraints=[],weights=[2,10,10],constraints2=[])
Branin = benchmarks(num_var=2,num_bound=4,lowerlimit=[-5,0],upperlimit=[10,15],constraints=[],weights=[2,10,10],constraints2=[])
Adjiman = benchmarks(num_var=2,num_bound=4,lowerlimit=[-1,-1],upperlimit=[2,1],constraints=[],weights=[2,10,10],constraints2=[])
Guinta = benchmarks(num_var=2,num_bound=4,lowerlimit=[-1]*2,upperlimit=[1]*2,constraints=[],weights=[2,10,10],constraints2=[])
Himmel = benchmarks(num_var=2,num_bound=4,lowerlimit=[-5]*2,upperlimit=[5]*2,constraints=[],weights=[2,10,10],constraints2=[])
Price2 = benchmarks(num_var=2,num_bound=4,lowerlimit=[-10]*2,upperlimit=[10]*2,constraints=[],weights=[2,10,10],constraints2=[])
Paraboloid = benchmarks(num_var=3,num_bound=6,lowerlimit=[-10]*3,upperlimit=[10]*3,constraints=[],weights=[2,10,10],constraints2=[])
DeJoungF1 = benchmarks(num_var=10,num_bound=20,lowerlimit=[-100]*10,upperlimit=[100]*10,constraints=[],weights=[2,10,10],constraints2=[])
Xinsheyang = benchmarks(num_var=2,num_bound=4,lowerlimit=[-2*math.pi]*2,upperlimit=[2*math.pi]*2,constraints=[],weights=[2,10,10],constraints2=[])
Schaffer1 = benchmarks(num_var=2,num_bound=4,lowerlimit=[-100]*2,upperlimit=[100]*2,constraints=[],weights=[2,10,10],constraints2=[])
Bohachevsky2 = benchmarks(num_var=2,num_bound=4,lowerlimit=[-50]*2,upperlimit=[50]*2,constraints=[],weights=[2,10,10],constraints2=[])
Cb3 = benchmarks(num_var=2,num_bound=4,lowerlimit=[-5]*2,upperlimit=[5]*2,constraints=[],weights=[2,10,10],constraints2=[])
Exponential = benchmarks(num_var=10,num_bound=20,lowerlimit=[-1]*10,upperlimit=[1]*10,constraints=[],weights=[2,10,10],constraints2=[])
Cosine = benchmarks(num_var=10,num_bound=20,lowerlimit=[-1]*10,upperlimit=[1]*10,constraints=[],weights=[2,10,10],constraints2=[])
Rastrigin = benchmarks(num_var=10,num_bound=20,lowerlimit=[-5.12]*10,upperlimit=[5.12]*10,constraints=[],weights=[2,10,10],constraints2=[])
Griewank = benchmarks(num_var=10,num_bound=20,lowerlimit=[-100]*10,upperlimit=[100]*10,constraints=[],weights=[2,10,10],constraints2=[])
Schwefel12 = benchmarks(num_var=2,num_bound=4,lowerlimit=[-100]*2,upperlimit=[100]*2,constraints=[],weights=[2,10,10],constraints2=[])
Ackley = benchmarks(num_var=2,num_bound=4,lowerlimit=[-32]*2,upperlimit=[32]*2,constraints=[],weights=[2,10,10],constraints2=[])
Egg = benchmarks(num_var=2,num_bound=4,lowerlimit=[-5]*2,upperlimit=[5]*2,constraints=[],weights=[2,10,10],constraints2=[])
Alpine = benchmarks(num_var=2,num_bound=4,lowerlimit=[-10]*2,upperlimit=[10]*2,constraints=[],weights=[2,10,10],constraints2=[])
