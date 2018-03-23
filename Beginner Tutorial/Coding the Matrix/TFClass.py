import math
import matplotlib.pyplot as plt

## NUMBER 1 ##
def transform(L,a,b): 
    return[a*x+b for x in L]

## 2 Vectors
S = [2+2j,3+2j,1.75+1j,2+1j,2.25+1j,2.5+1j,2.75+1j,3+1j,3.25+1j] # Smile Face
T = [(math.e**(2*math.pi*1j/20))**x for x in range(20)] # Circle

## Transform Vectors
m = transform(S,1/4,-0.62-0.35j)
t = transform(T,1/2,0)

## Adding Vectors
x = [x.real for x in m+t]
y = [y.imag for y in m+t]

# Plotting the Vectors
plt.xlabel("Real")
plt.ylabel("Complex")
plt.scatter(x,y)
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.show()

## NUMBER 2 ##






