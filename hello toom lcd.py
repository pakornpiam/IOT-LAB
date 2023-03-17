from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=1000000)
#print(i2c.scan()) ### check i2c adress 
print('Adress',hex(i2c.scan()[0]))
lcd =I2cLcd(i2c,0x27,2,16)  ## hex nuber of i2c adress ,2 row 16 alphabet
lcd.putstr('Hello toom\nby PKroaming')




