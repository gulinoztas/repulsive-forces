def find_coefficient(num_var, st, strVars, k, constraint, j):
    sign = constraint[j][1]
    for i in range(0, num_var):
        if i == k:
            st = st.replace(strVars[i], "1")  # xtodouble??? x str olduğundan find_coeff bulmuyor
            #print("kısıt:", st)
        else:
            if sign == ">=":
                st = st.replace(strVars[i], "0")  # her koşul aynı şeyi söylüyor! evala uyuyor ancak x işi bozuyor.
                #print("kısıt", st)
            elif st[1] == "<=":
                st = st.replace(strVars[i], "0")
                #print("kısıt", st)
            else:
                st = st.replace(strVars[i], "0")
                #print("kısıt:", st)
    find_coeff = eval(st)
    return find_coeff
    #print("kısıt:", st)
    #print("coefficient:", find_coeff)