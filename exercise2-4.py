import sys
import cv2 as cv
import numpy as np

data = []
default_file = 'imagesLab2/coins.png'

def main(argv):    
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    # Convert it to gray
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    # Reduce the noise to avoid false circle detection
    gray = cv.medianBlur(gray, 5)
    
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)
    
    
    # Draw the detected circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            
            center = (i[0], i[1])
            # circle center
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 3)
    
    
    cv.imshow("detected circles", src)
    cv.waitKey(0)
    
    return 0


def main2(argv):    
    img = cv.imread(default_file, 0)
    ret, thresh = cv.threshold(img,127,255,0)
    contours, hierarchy = cv.findContours(thresh, 1, 2)
    # cnt = contours[0]
    
    for idx, cnt in enumerate(contours):
        area = cv.contourArea(cnt)
        x,y,w,h = cv.boundingRect(cnt)
        
        # It is the ratio of width to height of bounding rect of the object.
        aspect_ratio = float(w)/h
        
        # Extent is the ratio of contour area to bounding rectangle area.
        rect_area = w*h
        extent = float(area)/rect_area
        
        # Solidity is the ratio of contour area to its convex hull area.
        hull = cv.convexHull(cnt)
        hull_area = cv.contourArea(hull)
        solidity = 0
        if hull_area != 0:
            solidity = float(area)/hull_area

        # Equivalent Diameter is the diameter of the circle whose area is same as the contour area.
        equi_diameter = np.sqrt(4*area/np.pi)

        # Orientation is the angle at which object is directed. 
        # Following method also gives the Major Axis and Minor Axis lengths.
        # (x,y),(MA,ma),angle = cv.fitEllipse(cnt)

        # average color of an object or the average intensity of the object in grayscale mode
        # mean_val = cv.mean(im, mask = mask)

        print(f"{idx} - {aspect_ratio} - {extent} - {equi_diameter} - {solidity}")


if __name__ == "__main__":
    main(sys.argv[1:])