import determine_intervals
from random import random
def myRandomVal(CurrentVar):
    rndCategoryLow = float(determine_intervals.VarInterval[CurrentVar,0])
    rndCategoryUp = float(determine_intervals.VarInterval[CurrentVar,1])
    k = int(4*random()+1)
    IntegerVars = False

    if k ==1:
        myRandomVal = ((rndCategoryUp-rndCategoryLow)/4)*random() + rndCategoryLow
    elif k ==2:
        myRandomVal = ((rndCategoryUp - rndCategoryLow) / 4) * random() + (rndCategoryUp - rndCategoryLow)/4 + rndCategoryLow
    elif k ==3:
        myRandomVal = ((rndCategoryUp - rndCategoryLow) / 4) * random() + 2*(rndCategoryUp - rndCategoryLow)/4 + rndCategoryLow
    else:
        myRandomVal = ((rndCategoryUp - rndCategoryLow) / 4) * random() + 3*(rndCategoryUp - rndCategoryLow)/4 + rndCategoryLow
    if IntegerVars==False:
        myRandomVal = myRandomVal   #virgülden sonrasını almıyor.
    return myRandomVal
#print(myRandomVal)
#print(rndCategoryLow)
#print(rndCategoryUp)