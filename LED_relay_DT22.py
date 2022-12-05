from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
from lcd_api import LcdApi
import time
import dht


###relay#######
relay = Pin(15,Pin.OUT)
def relay_off():
    relay.value(0)
    print('relay:off')
def relay_on():
    relay.value(1)
    print('relay:on')
#### temp and humid ######    
d = dht.DHT22(Pin(16))
time.sleep(2)

def get_temp_humid():
    d.measure()
    time.sleep(2)
    temp = d.temperature()
    humid = d.humidity()
    text_temp = 'TEMP: {:.2f} C'.format(temp)
    text_humid = 'HUMID: {:.2f} %'.format(humid)
    return (text_temp, text_humid, temp, humid)   ### sent data out

tp, th, t, h = get_temp_humid()
#print(tp)
#print(th)

### define LCD
i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=1000000)
lcd = I2cLcd(i2c, 0x27, 2, 16)


def show_lcd(line1, line2):
    lcd.clear()
    lcd.putstr(line1)
    lcd.move_to(0,1)# lcd.move_to(colum, Row)
    lcd.putstr(line2)
             
for i in range(10):
    tp, th, t, h = get_temp_humid()
    show_lcd(tp,th)
    if t >30:
        relay_on()
    else:
        relay_off()
    time.sleep(2)


    
    

#i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=1000000)
#print(i2c.scan()) ### check i2c adress 
#print('Adress',hex(i2c.scan()[0]))
#lcd =I2cLcd(i2c,0x27,2,16)  ## hex nuber of i2c adress ,2 row 16 alphabet
### lcd.putstr('Hello toom\nby PKroaming')
#lcd.putchar(chr(244)) ## show special charector as table ,need convert binary to int 




