import variables
from statistics import *
from rsab_v3 import *
import pandas as pd
from opfunu.cec.cec2014.function import *
def interval_table(trials,table): #creates interval table
    for j in range(0, variables.num_var):
        variables.z.append(variables.CurrentInterval[j][1])
        variables.z.append(variables.CurrentInterval[j][2])
    table[trials,:] = variables.z
    variables.z = []
    return table
def result_table(trials,table): #creates result table
    table[trials,0] = variables.loop
    table[trials,1] = variables.hitObj
    table[trials,2:variables.num_var+2] = variables.bestpos[variables.gbest]
    table[trials,variables.num_var+2] = rsab(variables.num_var,variables.num_const,variables.lowerlimit,variables.upperlimit,variables.set_size,variables.textboxiterations).call_function(variables.function,variables.bestpos[variables.gbest])
    table[trials, variables.num_var + 3] = variables.bestfit[variables.gbest]
    return table
def average(table): #creates averages
    for i in range(0,variables.num_var+4):
        variables.ave_table[:,i] = mean(table[:,i])
    return variables.ave_table

