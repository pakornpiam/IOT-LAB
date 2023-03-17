from machine import Pin, I2C

import ssd1306
from time import sleep

# Set up I2C communication with the OLED display
i2c = I2C(1, scl = Pin(22), sda = Pin(21))
display = ssd1306.SSD1306_I2C(128,64, i2c)

# Clear the display and display some text
display.fill(1)
display.text("Hello, World!", 30, 25,1)
display.show()

# Wait for a few seconds and then clear the display
sleep(5)
display.fill(0)
display.show()
