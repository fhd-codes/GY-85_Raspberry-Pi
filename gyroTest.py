import sys
sys.path.insert(1,'/home/pi/i2clibraries')
from i2c_itg3205 import *
from time import *

itg3205 = i2c_itg3205(1)

while True:
    (itgready, dataready) = itg3205.getInterruptStatus ()
    if dataready:
        temp = itg3205.getDieTemperature ()
        (x, y, z) = itg3205.getDegPerSecAxes ()
        print ("Temp:" + str (temp ))
        print ("X:" + str (x ))
        print ("Y:" + str (y ))
        print ("Z:" + str (z ))
        print ("")

    sleep (1)
    