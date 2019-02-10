from phue import Bridge
b = Bridge('192.168.86.21')
b.connect()
b.set_light(3,'on', True)

