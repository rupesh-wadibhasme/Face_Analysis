import numpy as np
import cv2,math
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10

img1 = cv2.imread('image.jpg',0)          # queryImage
img2 = cv2.imread('image1.jpg',0) # trainImage

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)


bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)

good = sorted(matches, key = lambda x:x.distance)

if len(good)>MIN_MATCH_COUNT:
	src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)

if np.shape(M) == ():
	print( "No transformation possible" )
        #return None, None

        ## derive rotation angle from homography


theta = - math.atan2(M[0,1], M[0,0]) * 180 / math.pi

total_move= src_pts[0][0]-dst_pts[0][0]

Horizontal=total_move[0]
Vertical=total_move[1]

print "Displacement in X:",Horizontal
print "Displacement in Y:",Vertical
print "Angle detected:",abs(theta)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[1:10],None, flags=2)
cv2.imwrite("output.jpg",img3)





