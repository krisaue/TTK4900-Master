import cv2 as cv
import numpy as np


array1 = np.loadtxt("files/cornersLeftStereoCalib.txt")


array2 = array1[:8,:].reshape((8,1,2))
array3 = array1[8:16,:].reshape((8,1,2))

#print(array2)
#print(array3)

array4 = []

array4.append(array2)
array4.append(array3)

print(array4)