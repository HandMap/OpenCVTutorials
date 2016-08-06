from __future__ import print_function
import argparse
import cv2
import pprint

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

for x in range(0, image.shape[0]):
    for y in range(0, image.shape[1]):
        print("x value: " + str(x) +
              " y value: " + str(y) +
              " content: " + pprint.pformat(image[x, y]))