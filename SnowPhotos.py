from phue import Bridge
import cv2
from time import sleep

#Turn on the light
b = Bridge('192.168.86.21')
b.connect()

#Take a picture each hour

name = 0
while True:
    b.set_light(3,'on', True)
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    name +=1
    final_name = 'C:/geomsb/' + str(name) + '.jpg'
    cv2.imwrite(final_name, frame)
    cap.release()
    b.set_light(3,'on', False)
    sleep(30)
      
