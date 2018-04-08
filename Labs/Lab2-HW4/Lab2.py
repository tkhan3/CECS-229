################################## NUMBER 1 ###################################
import math
import matplotlib.pyplot as plt

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

################################## NUMBER 2 ###################################
from image import file2image
from plotting import plot

data=file2image("img01.png")

Y=list(range(0,189,1))
X=list(range(0,166,1))
pts=[x+(189j+y*-1j) for x in X for y in Y if data[y][x][0]<120]
plot(pts, 300)

# translation by 189j and multiplication by -1 was used to make the image 
# reflect the expected result

# Y is the set of numbers from 0-188, as the image is 189 pixels tall

# X is the set of numbers from 0-165, as the image is 166 pixels across


################################## NUMBER 3 ###################################
data=file2image("img01.png")
Y=list(range(0,189,1))
X=list(range(0,166,1))
pts=[x+(189j+y*-1j) for x in X for y in Y if data[y][x][0]<120]
pts2=[x*(math.e**(1j*math.pi/4)) for x in pts]
plot(pts2, 300)











