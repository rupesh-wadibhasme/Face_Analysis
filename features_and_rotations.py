import numpy as np
import cv2,math
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10

img1 = cv2.imread('image.jpg',0)          # queryImage
img2 = cv2.imread('image1.jpg',0) # trainImage

# Initiate SIFT detector
#sift = cv2.xfeatures2d.SIFT_create() #cv2.SIFT()

orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
#kp1, des1 = sift.detectAndCompute(img1,None)
#kp2, des2 = sift.detectAndCompute(img2,None)


kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)


bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)
good = sorted(matches, key = lambda x:x.distance)


'''
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1,des2,k=2)

# store all the good matches as per Lowe's ratio test.
good = []


for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

'''

if len(good)>MIN_MATCH_COUNT:
	src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)


if np.shape(M) == ():
	print( "No transformation possible" )
        #return None, None

        ## derive rotation angle from homography
theta = - math.atan2(M[0,1], M[0,0]) * 180 / math.pi


img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
plt.imshow(img3)
plt.imsave("output.jpg",img3)
#plt.show()


print "The detected angle is ==>", theta

