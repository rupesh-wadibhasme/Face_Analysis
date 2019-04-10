import cv2
import numpy as np

img = cv2.imread('image.jpg')
num_rows, num_cols = img.shape[:2]

translation_matrix = np.float32([ [1,0,70], [0,1,0] ])
img_translation = cv2.warpAffine(img, translation_matrix, (num_cols , num_rows))

#img_translation=img_translation[:,70:]
#img_translation=cv2.resize(img_translation, (num_cols, num_rows)) 


cv2.imwrite('Translation.jpg', img_translation)
#cv2.waitKey()
