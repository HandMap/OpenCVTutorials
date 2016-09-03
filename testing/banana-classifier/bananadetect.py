import numpy as np
import cv2

banana_cascade = cv2.CascadeClassifier('banana_classifier.xml')

img = cv2.imread('bananas-main.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bananas = banana_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w ,h) in bananas:
    cv2.rectangle(img, (x, y), (x+w, y+h),(255,0,0),2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()