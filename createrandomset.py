import numpy as np
from random import random
from random import seed
from random import gauss
from random import uniform
import determine_intervals

#def createrandomset():
rand_set_size = 20
set= np.array(())
for j in range(0,rand_set_size):

    for i in range(0,determine_intervals.num_var):
        rand_set = uniform(determine_intervals.lowerlimit[i],determine_intervals.upperlimit[i])   #determine intervals ile hesaplanan aralıklarda random sayı üretir her değişken için
        set = np.append(set,rand_set)    #
#return set.reshape(j + 1, determine_intervals.num_var)
values = set.reshape(j + 1, determine_intervals.num_var)    #değerleri şekillendirir.
#print(set.reshape(j + 1, determine_intervals.num_var))
#print(values)

