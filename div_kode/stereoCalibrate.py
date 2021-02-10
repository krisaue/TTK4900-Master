import cv2 as cv
import numpy as np


imgPtsL = np.loadtxt("files/cornersLeftStereoCalib.txt")
imgPtsR = np.loadtxt("files/cornersRightStereoCalib.txt")
K_l = np.loadtxt('files/K_l.txt')
K_r = np.loadtxt('files/K_r.txt')

D_l = np.loadtxt('files/D_l.txt')
D_r = np.loadtxt('files/D_r.txt')

#objp = np.zeros((4*6,3), np.float32)
#objp[:,:2] = np.mgrid[0:6,0:4].T.reshape(-1,2)

#ObjPts = np.array([[145,750,0],[145,895,0],[0,895,0],[0,750,0],[145,0,0],[145,145,0],[0,145,0],[0,0,0]],dtype= np.float32)
ObjPts = np.array([[750,145,0],[895,145,0],[895,0,0],[750,0,0],[0,145,0],[145,145,0],[145,0,0],[0,0,0]],dtype= np.float32)
ObjPts[:,:2] = ObjPts[:,:2].T.reshape(-1,2)

#object_points = np.empty((0,3),dtype = np.float32)
image_points_l = np.empty((0,2),dtype = np.float32)
image_points_r = np.empty((0,2),dtype = np.float32)
object_points = []
image_points_l_2 = []
image_points_r_2 = []


temp = int(len(imgPtsL)/8)
#for j in range(temp):
#    image_points_l =np.append(image_points_l,imgPtsL[j*8:(j*8)+8,:]),axis=0)
#    image_points_r =np.append(image_points_r,imgPtsR[j*8:(j*8)+8,:]),axis=0)


for i in range(temp):
    object_points.append(ObjPts)
    image_points_l_2.append(np.array(imgPtsL[i*8:(i*8)+8,:].reshape((8,1,2)),dtype=np.float32))
    image_points_r_2.append(np.array(imgPtsR[i*8:(i*8)+8,:].reshape((8,1,2)),dtype=np.float32))
    #object_points = np.append(object_points,ObjPts,axis=0)
    #image_points_l =np.append(image_points_l,imgPtsL[i*8:(i*8)+8,:],axis=0)
    #image_points_r =np.append(image_points_r,imgPtsR[i*8:(i*8)+8,:],axis=0)


#print(image_points_l_2)
R_init = np.eye(3)
T_init = np.array([[25.0,0.0,0.0]])

retval, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, E, F = cv.stereoCalibrate(object_points,image_points_l_2,image_points_r_2,K_l,D_l,K_r,D_r,(1224,1024),R_init,T_init,flags=cv.CALIB_USE_EXTRINSIC_GUESS)

print(T)
print(R)