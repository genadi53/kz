import cv2 as cv
import sys

img = cv.imread("cat.jpg")
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)

key = cv.waitKey(0)
if key == ord("s"):
    cv.imwrite("cat.png", img)