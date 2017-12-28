import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.cv.FOURCC(*'MP4V')
out = cv2.VideoWriter('video11.mp4', fourcc, 20, (640, 480))
x = 0
while(x <= 200):
    x = x + 1
    # get a frame
    ret, frame = cap.read()
    # save a frame
    out.write(frame)
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows() 
