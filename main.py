import cv2
import numpy as np

img = cv2.imread("Resources/cat_card.jpg")

width,height = 184,275
pts1 = np.float32([[24,68],[206,22],[58,343],[274,290]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOut = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Img",img)
cv2.imshow("cat_card",imgOut)
cv2.waitKey(0)

