# import cv2
# import matplotlib.pyplot as plt
#
# img = cv2.imread("panda.jpg")
#
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# _, binary = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
#
# # plt.imshow(binary, cmap="gray")
# # plt.show()
#
# contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(hierarchy)
# img = cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
# plt.imshow(img)
# plt.show()


import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

segmenator = SelfiSegmentation()


while True:
    success, img = cap.read()

    imgOut = segmenator.removeBG(img, (255, 0, 0), threshold=0.95)

    cv2.imshow("Im", img)
    cv2.imshow("Im Out", imgOut)
    cv2.waitKey(1)



