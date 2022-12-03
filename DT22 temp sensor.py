from machine import Pin
import time
import network
import dht
d = dht.DHT22(Pin(16))
d.measure()
print (d.temperature())
print (d.humidity())


for i in range (100):
    d.measure()
    time.sleep(1)
    print(d.temperature())
    print(d.humidity())
    print('----')
    time.sleep(1)
    

