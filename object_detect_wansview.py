import cv2
import os
import cvlib as cv
from cvlib.object_detection import draw_bbox


conn_str = "rtsp://{0}:{1}@{2}/live/ch0".format(os.environ["CAM_USER"],
                                                os.environ["CAM_PW"],
                                                os.environ["CAM_IP_OUTDOOR"])

print(conn_str)

cap = cv2.VideoCapture(conn_str)

while(1):
    success, img = cap.read()

    bbox, label, conf = cv.detect_common_objects(img)

    output_image = draw_bbox(img, bbox, label, conf)

    cv2.imshow('Object Detection', output_image)

    k = cv2.waitKey(30) & 0xff
    if k == 27:        # Press Escape to stop the loop
        break

cap.release()
cv2.destroyAllWindows()

