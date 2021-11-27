import cv2
import os


conn_str = "rtsp://{0}:{1}@{2}/live/ch0".format(os.environ["CAM_USER"],
                                                os.environ["CAM_PW"],
                                                os.environ["CAM_IP_OUTDOOR"])

print(conn_str)

cap = cv2.VideoCapture(conn_str)

while(1):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:     # Press escape to stop the loop
        break

cap.release()
cv2.destroyAllWindows()

