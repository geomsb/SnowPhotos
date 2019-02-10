from phue import Bridge
import cv2
from time import sleep

#Turn on the light
b = Bridge('192.168.86.21')
b.connect()
b.set_light(3,'on', True)

#Take a picture

cap = cv2.VideoCapture(0)

name = 0
while True:
    ret, frame = cap.read()
    name +=1
    final_name = 'C:/geomsb/' + str(name) + '.jpg'
    cv2.imwrite(final_name, frame)
    sleep(30)  
