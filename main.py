
import cv2 as cv
import cv2
from time import sleep
from tkinter import *
from PIL import ImageTk, Image, ImageColor
import os
import numpy as np

cap = cv.VideoCapture(0)

ret, frame = cap.read()

image = cv.imwrite("v1.jpg", frame)
imgg = Image.open("v1.jpg")
img1 = imgg.copy()
img2 = imgg.copy()
size = imgg.size

im = imgg.convert("L").load()
imm = imgg.load()
# print(im[50, 50])

for i in range(size[0]):
    for j in range(size[1]):
        if im[i, j] <= 12:
            imm[i, j] = (255, 255, 255)
            # pass



imgg.show()
img2.convert("L").show()
img1.show()

os.remove("v1.jpg")
cap.release()



# cap = cv.VideoCapture(0)
# ret, frame = cap.read()
# image = cv.imwrite("v1.jpg", frame)
# root = Tk()
# img = ImageTk.PhotoImage(Image.open("v1.jpg"))
# panel = Label(root, image=img)
# panel.pack(side="bottom", fill="both", expand="yes")
# root.mainloop()
# os.remove("v1.jpg")
# cap.release()





# import cv2
# import numpy as np
# cap = cv2.VideoCapture(0)
#
# ret, frame = cap.read()
# cv2.imwrite("v1.jpg", frame)
# #
# image = cv2.imread('v1.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Set threshold level
# threshold_level = 20
#
# # Find coordinates of all pixels below threshold
# coords = np.column_stack(np.where(gray < threshold_level))
#
# print(coords)
#
# # Create mask of all pixels lower than threshold level
# mask = gray < threshold_level
#
# # Color the pixels in the mask
# image[mask] = (255, 255, 255)
#
# cv2.imshow('image', image)
# cv2.waitKey()