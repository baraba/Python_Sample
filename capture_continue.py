import cv2
import numpy as np


cap = cv2.VideoCapture(0)
while(1):
    #
    ret,frame = cap.read(0)
    #
    cv2.imshow("capture",frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
