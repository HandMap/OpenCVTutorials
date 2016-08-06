# The top import is for Python2.7 support
from __future__ import print_function
import argparse
import cv2

# argparse to handle our command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")

# parse the arguments and store them in a dictionary
args = vars(ap.parse_args())

# load the image off the disk
# the imread function returns a NumPy array representing the image.
image = cv2.imread(args["image"])

# examine the dimensions of the image. The images are represented
# as NumPy arrays, so we can use the shape attribute to examine
# the width, height, and number of channels
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

# handles displaying the actual image on my screen
# the first parameter is a string, the "title" of the window
# the second parameter is a reference to the image we loaded.
cv2.imshow("Image", image)

# the cv2.waitKey paused the execution of the script until
# we press a key on the keyboard.
cv2.waitKey(0)

# lastly we write our image to file in JPG format
cv2.imwrite("new_image.jpg", image)