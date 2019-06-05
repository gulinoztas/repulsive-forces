import determine_intervals
def strToformula(st,strVars,myCurrentSolution):
    for j in range(0,determine_intervals.num_var):
        st = st.replace(strVars[j], 0.000000000000001+ myCurrentSolution[j])
    return st