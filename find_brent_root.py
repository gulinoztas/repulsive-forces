
from pyroots import Brentq
f=lambda x : x+0.0193-5
brent = Brentq(epsilon=0.0001)
tempResult = brent(f,1,10)
print(tempResult)
