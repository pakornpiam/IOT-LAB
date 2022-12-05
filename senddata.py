import socket
import network
import time
from machine import Pin
import dht

################################
serverip = '192.168.1.8'
port = 9000
################################

def send_data(data):
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((serverip,port))
	server.send(data.encode('utf-8'))
	data_server = server.recv(1024).decode('utf-8')
	print('Server:' , data_server)
	server.close()
	
################wifi##############
wifi = 'Prayut'
password = 'yuth2474'
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
time.sleep(2)
wlan.connect(wifi, password)
time.sleep(2)
print(wlan.isconnected())
#####################wifi############ 

"""print('temperature checking...')
d = dht.DHT22(Pin(16))
d.measure()
time.sleep(1)

for i in range(20):
    d.measure()
    time.sleep(1)
    temp = d.temperature()
    humid = d.humidity()
    print(temp)
    print(humid)
    time.sleep(3)
    print('-------------------------------') """

"""while True:
    send_data('LED1:ON')
    time.sleep(2)"""

led = Pin(14,Pin.OUT)
for i in range(10):
    led.on()
    send_data('LED1:ON')
    time.sleep(1)
    led.off()
    send_data('LED1:OFF')
    time.sleep(1)
    


