import sys
sys.path.insert(1,'/home/pi/GY-85_Raspberry-Pi/i2clibraries')
from i2c_adxl345 import *
from time import *

adxl345 = i2c_adxl345(1)

while True:
    print (adxl345)
    sleep (1)