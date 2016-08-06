from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

"""
for x in range(0, image.shape[1]):
    for y in range(0, image.shape[0]):
        (blue, green, red) = image[y, x]
        print("Pixel at (" + str(x) + "," + str(y) + ") - " +
              "Red: {}, Green: {}, Blue: {}".format(red, green, blue))
"""

# grab 100 x 100 pixel region of the image
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

# change the colour of this region to green
image[0:100, 0:100] = (0, 255, 0)

# present the updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)