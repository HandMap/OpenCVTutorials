import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    fast = cv2.FastFeatureDetector_create()
    kp = fast.detect(frame, None)

    img2 = cv2.drawKeypoints(frame, kp, frame, color=(255,0,0))

    # Display the resulting frame
    cv2.imshow('frame',img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()