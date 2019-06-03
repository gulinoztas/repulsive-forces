def find_lower_limit(num_var, st, strVars, constraint, VarInterval, j, k):
    for i in range(0, num_var):
        if i == k:
            st = st.replace(strVars[i], "x")

            #print("kısıt", st)
        else:
            st = st.replace(strVars[i], max((str(0.000000000000001 + (VarInterval[i, 0]))), str(abs(float(constraint[j][2])))))
            #print("kısıt", st)
    st = st + "-" + str(abs(float(constraint[j][2])))
    #print(st)
    return st
