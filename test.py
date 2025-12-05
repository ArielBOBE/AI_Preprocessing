import cv2
import os 
import matplotlib.pyplot as plt

image = cv2.imread('./image/fundus_0001.png', 0)
cv2.imshow("",image)
cv2.waitKey(0)
cv2.destroyAllWindows()