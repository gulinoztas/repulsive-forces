from rsab_v3 import *
import numpy as np
import pandas as pd
import variables

def determine():
    VarInterval = np.zeros((variables.num_var, 2))
    myDataTableIntervals = np.array(())
    lowerlimitt = np.zeros((variables.num_var))
    upperlimitt = np.zeros((variables.num_var))
    ref = rsab(variables.num_var, variables.num_const, variables.lowerlimit, variables.upperlimit, variables.set_size,variables.textboxiterations)

    VarInterval[:,:] = [(variables.lowerlimit[k],variables.upperlimit[k]) for k in range(0,variables.num_var)]

    for k in range(0, variables.num_var):
        for j in range(variables.num_bound, variables.num_const):
            st = ref.const()[j][0]
            splitVar = ref.const()[j][0].split("-x", -1)  # eksi işaretli değişkenleri ayrıştırır.
            sign = ref.const()[j][1]
            rhs = ref.const()[j][2]
            variables.chg = False
            if variables.num_var < 10:
                test = True if "x0{}".format(k + 1) in st else False  # or "x{}".format(v)
            else:
                test = True if "x{}".format(k + 1) in st else False
            if test == True:  # gereksiz yere girmesin diye..
                if sign == "<=":
                    if float(rhs) >= 0:
                        if splitVar[0] == st:  # all the variables in the selected constraint are positive signed
                            st = ref.find_upper_limit(sign, st, VarInterval, j, k)
                            result = ref.brentroot(st, VarInterval, k)
                            if result > 0:  # 0a eşitse ne yapacak
                                if result > VarInterval[k, 0] and result < VarInterval[k, 1]:  # or idi 9/11/2020
                                    VarInterval[k, 1] = result
                            result = 0
                        else:  # variables in the selected constraint are negative or positive signed
                            find_coeff = ref.find_coefficient(st, k, sign)
                            if find_coeff < 0:  # working variable is negative signed
                                VarInterval[k, 0] = VarInterval[k, 0]
                            else:
                                variables.chg = True   #eksi işaret varsa, üst limit bulunurken üst limiti yerine koy 7/12/2020
                                st = ref.find_upper_limit(sign, st, VarInterval, j, k)
                                result = ref.brentroot(st, VarInterval, k)
                                if result > 0:  # 0a eşitse ne yapacak
                                    if result > VarInterval[k, 0] and result < VarInterval[k, 1]:  # or idi 16/11/2020
                                        VarInterval[k, 1] = result
                                result = 0

                    else:  # rhs is negative
                        if splitVar[0] == st:  # all the variables in the selected constraint are positive signed
                            VarInterval[k, 1] = VarInterval[k, 1]
                        else:
                            find_coeff = ref.find_coefficient(st, k, sign)
                            if find_coeff < 0:
                                st = ref.find_lower_limit(sign, st, VarInterval, j, k)
                                result = ref.brentroot(st, VarInterval, k)
                                if result > 0:
                                    # if result <= VarInterval[k, 0] or result < VarInterval[k, 1]:  #16/11/2020
                                    if result > VarInterval[k, 0] and result < VarInterval[k, 1]:
                                        VarInterval[k, 0] = result
                                result = 0
                            else:
                                VarInterval[k, 1] = VarInterval[k, 1]
                elif sign == ">=":
                    if float(rhs) >= 0:
                        if splitVar[0] == st:
                            st = ref.find_lower_limit(sign, st, VarInterval, j, k)
                            #if eval(st.replace("x", str(0)))>= 0:#rhs:   #st'de -rhs olduğundan sağ yan değer 0 kaldı. 11/11/2020
                            result = ref.brentroot(st, VarInterval, k)
                            if result > 0:
                                if result > VarInterval[k, 0] and result < VarInterval[k, 1]:  # <=LL idi.
                                    VarInterval[k, 0] = result
                            result = 0
                        else:
                            find_coeff = ref.find_coefficient(st, k, sign)
                            if find_coeff < 0:
                                VarInterval[k, 1] = VarInterval[k, 1]
                                # VarInterval[k, 0] = 0
                            else:
                                st = ref.find_lower_limit(sign, st, VarInterval, j, k)
                                result = ref.brentroot(st, VarInterval, k)
                                if result > 0:
                                    # if result <= VarInterval[k, 0] or result < VarInterval[k, 1]: 16/11/2020
                                    if result > VarInterval[k, 0] and result < VarInterval[k, 1]:
                                        VarInterval[k, 0] = result
                                result = 0
                    else:
                        if splitVar[0] == st:
                            VarInterval[k, 0] = 0
                        else:
                            find_coeff = ref.find_coefficient(st, k, sign)
                            if find_coeff < 0:
                                if "-" in st:  # buraya da bakmalı
                                    st = st.replace("-","+")  # ilk değişkenin eksisini kaldırır. her - olan değişkeni + yapar. Başına da + koyar.
                                    st = st[1:]
                                st = ref.find_upper_limit(sign, st, VarInterval, j, k)
                                result = ref.brentroot(st, VarInterval, k)
                                if result > 0:
                                    # if result > VarInterval[k, 0] or result < VarInterval[k, 1]:
                                    if result > VarInterval[k, 0] and result < VarInterval[k, 1]:
                                        VarInterval[k, 1] = result
                                result = 0
                            else:
                                VarInterval[k, 0] = VarInterval[k, 0]
                else:
                    print("Hata oluştu!")

        variable = ref.strVars()[k]

        lowerlimitt[k] = VarInterval[k, 0]
        upperlimitt[k] = VarInterval[k, 1]
        myDataTableIntervals = [ref.strVars(), lowerlimitt, upperlimitt, np.zeros(variables.num_var)]
    myDataTableIntervals = np.reshape(myDataTableIntervals, (4, variables.num_var))
    Interval = pd.DataFrame(data=myDataTableIntervals, index=None, columns=None)
    print(Interval)
    return myDataTableIntervals#Interval
