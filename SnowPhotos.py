from phue import Bridge
b = Bridge('192.168.86.21')
b.connect()
b.set_light(3,'on', True)

import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imwrite('C:/geomsb/Test_1.jpg', frame) 
cap.release()