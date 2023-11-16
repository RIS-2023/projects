import cv2
import numpy as np
import matplotlib.pyplot as plt

from canny_func import region_of_interest, make_points, average, display_lines

# Loading image and convert it into gray scale
img = cv2.imread("lane detection test images/frame.jpg")
cv2.imshow('input img', img)
cv2.waitKey(3000)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray img', gray)
cv2.waitKey(3000)

# Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow('Gaussian Blue', blur)
cv2.waitKey(3000)

# Canny edge detector
edges = cv2.Canny(blur, 100, 200)
cv2.imshow('Canny edge', edges)
cv2.waitKey(3000)


roi = region_of_interest(edges)
cv2.imshow('ROI', roi)
cv2.waitKey(3000)


lines = cv2.HoughLinesP(roi, 2, np.pi/180, 100,
                        np.array([]), minLineLength=40, maxLineGap=5)



copy = np.copy(img)
averaged_lines = average(copy, lines)
black_lines = display_lines(copy, averaged_lines)

# combine the line image and the color image (copy*0.8 + black_lines*1 + 1)
lanes = cv2.addWeighted(copy, 0.8, black_lines, 1, 1)
cv2.imshow('Result', lanes)
cv2.waitKey(3000)
