from machine import Pin, ADC
from utime import sleep, sleep_us
import machine
import time

samplingTime = 280 #original 280
deltaTime = 40
sleepTime = 9680
# Define the ADC pin for the dust sensor
adc = machine.ADC(machine.Pin(13))
LedPower = Pin(27)
while True:
    LedPower.on
    sleep_us(samplingTime)
    time.sleep(2)
    # Read the ADC value from the dust sensor
    dust_sensor_value = adc.read()
    
    #sleep_us(deltaTime)
    LedPower.off
    #sleep_us(sleepTime)
    print(dust_sensor_value)

    # Convert the ADC value to voltage
    voltage = dust_sensor_value * 3.3 / 1095

    # Calculate the dust density (in μg/m³) using the formula from the datasheet
    dust_density = 0.17 * voltage - 0.1

    # Print the dust density value
    print("Dust density: {:.2f} μg/m³".format(dust_density))

    # Wait for 5 seconds before taking another reading
    time.sleep(5)