import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("lane detection test images/frame.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('red', gray)
cv2.waitKey(3000)
cv2.imwrite('a/gray.jpg',gray)
border, binary = cv2.threshold(gray, 30,110,cv2.THRESH_BINARY)
cv2.imshow('red', binary)
cv2.waitKey(3000)
