# Please hit any key when images pop to close the image dont hit
# the x on window , causes the image to loop forver and never moving to next
# line of code

import cv2
import numpy as np
from mat import Mat
import math

# Task 4.15.1
mat_image = cv2.imread('anaconda.jpg' , cv2.IMREAD_GRAYSCALE)
cv2.imshow('Task 4.15.1',mat_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 4.15.2
mat_A = np.identity(600, dtype=np.uint8) # get 600 x 600 Identity matrix of type uint8(0-254)
mat_B = np.asarray(mat_image)
mat_C = mat_B.dot(mat_A)
cv2.imshow('Task 4.15.2',mat_C)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 4.15.3
def identity(labels = {'x','y','u'}):
    d = {}
    for i in labels:
        d[(i,i)] = 1
    return Mat((labels, labels),d)

def translation(x,y):
    d=identity().f
    d[('x','u')]=x
    d[('y','u')]=y
    return Mat((identity().D),d)
print("---Task 4.15.3---" + str(translation(3,3)))

# Task 4.15.4
def scale(a, b):
    return Mat(({'x','y','u'},{'x','y','u'}),{('x','x'):a,('y','y'):b,('u','u'):1})
print("---Task 4.15.4---" + str(scale(3,3)))    

# Task 4.15.5
def rotation(angle):
    d=identity().f
    d[('x','x')]=math.cos(angle)
    d[('y','x')]=math.sin(angle)
    d[('x','y')]=-math.sin(angle)
    d[('y','y')]=math.cos(angle)
    return Mat((identity().D),d)    
print("---Task 4.15.5---" + str(rotation(30)))
    
    
# Task 4.15.6
def rotate_about(x,y,angle):
    return translation(x,y) * rotation(angle) * translation(-x,-y)
print("---Task 4.15.6---")
A = rotate_about(30,3,3)   
    
    
    
    