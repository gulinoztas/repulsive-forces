
def find_upper_limit(num_var, st, strVars, constraint , VarInterval, j, k):
    sign=constraint[j][1]
    i=0
    print(i == k)
    for i in range(0, num_var):

        if i == k:
            st = st.replace(strVars[i], "x")
            #print("x konulduğunda", st)
        elif sign == ">=":
            st = st.replace(strVars[i], min((str(0.000000000000001 + (VarInterval[i, 0]))), str(abs(float(constraint[j][2])))))
            #print("upper kısıt", st)
        else:
            st = st.replace(strVars[i], min((str(0.000000000000001 + (VarInterval[i, 0]))), str(constraint[j][2])))
            #print("upper2 kısıt", st)
    st = st + "-" + str(abs(float(constraint[j][2])))
    #print(st)
    return st

