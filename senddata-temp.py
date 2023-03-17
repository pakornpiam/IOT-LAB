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
time.sleep(1)
wlan.connect(wifi, password)
time.sleep(5)
print(wlan.isconnected())
#####################wifi############ 

print('temperature checking...')
d = dht.DHT22(Pin(15))

for i in range(20):
    d.measure()
    time.sleep(2)
    temp = d.temperature()
    humid = d.humidity()
    print(temp)
    print(humid)
    text = 'TEMP-HUMID:{} and {}'.format(temp,humid)
    send_data(text)
    time.sleep(3)
    print('-------------------------------') 




    



