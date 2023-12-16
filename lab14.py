"""
@file laplace_demo.py
@brief Sample code showing how to detect edges using the Laplace operator
"""

import sys
import cv2 as cv

def main(argv):
    # Declare the variables we are going to use
    ddepth = cv.CV_16S
    kernel_size = 3
    window_name = "Laplace Demo"

    # load image
    imageName = argv[0] if len(argv) > 0 else 'cat.jpg'
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR) # Load an image

    # Check if image is loaded fine
    if src is None:
        print ('Error opening image')
        print ('Program Arguments: [image_name -- default cat.jpg]')
        return -1

    # [reduce_noise]
    # Remove noise by blurring with a Gaussian filter
    src = cv.GaussianBlur(src, (3, 3), 0)

    # [reduce_noise]
    # Convert the image to grayscale
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # Create Window
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    # Apply Laplace function
    dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)

    # converting back to uint8
    abs_dst = cv.convertScaleAbs(dst)

    # [display]
    cv.imshow(window_name, abs_dst)
    cv.waitKey(0)

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])