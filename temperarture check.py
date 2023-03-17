from machine import Pin, SoftI2C
import network
import time
from i2c_lcd import I2cLcd
import socket
import dht

led = Pin(15, Pin.OUT)
led.off()
#########LCD########
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=1000000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
time.sleep(1)

lcd.clear() # clear LCD
text = 'Starting...'
lcd.putstr(text)
###############DHT###############
d = dht.DHT22(Pin(15))
t = 0
h = 0
def check_temp():
    global t
    global h
    print('check temp starting....')
    while True:
        d.measure()
        time.sleep(2)
        t = d.temperature()
        h = d.humidity()
        print('DHT22:',t,h,)
        time.sleep(2)
        
def runserver():
    global led_status
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 80
    s.bind((host,port))
    s.listen(5)

################wifi##############
wifi = 'Prayut'
password = 'yuth2474'
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
time.sleep(2)
wlan.connect(wifi, password)
time.sleep(2)
status = wlan.isconnected()
ip,_,_,_ = (wlan.ifconfig())
#####################wifi############
if status == True:
    lcd.clear()
    text = 'IP:{}'.format(ip)
    lcd.putstr(text)
    time.sleep(2)
    lcd.clear()
    lcd.putstr('Wifi Connected')
    time.sleep(2)
   
else:
    lcd.clear
    lcd.putstr('Wifi disconnected')

html = 'Hello world'

######### server##################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#
host = ''
port = 80 # defult of web browser
s.bind((host,port))
s.listen(5)

while True:
    client, addr = s.accept()
    print('connection from;', addr)
    data = client.recv(1024).decode('utf-8')
    print([data])
#########server########################   
    client.send(html)
    client.close()


_thread.start_new_thread(runserver,())
_thread.start_new_thread(checktemp,())
