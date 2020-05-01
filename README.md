# GY-85_Raspberry-Pi
Interfacing GY-85 (IMU module) with Raspberry Pi 3b+


# Step 1: Updating python version

- Open terminal and write:

      $ sudo apt-get install python3-dev libffi-dev libssl-dev -y
      $ wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
      $ tar xJf Python-3.6.3.tar.xz
      $ cd Python-3.6.3
      $ ./configure
      $ make
      $ sudo make install
      $ sudo pip3 install --upgrade pip
      $ sudo nano ~/.bashrc
      $ alias python3=python3.6
      $ source ~/.bashrc
- To check if python has successfully upgraded, write the following lines in terminal

      $ python3
      $ print("fhd-codes")
        
  (if the message is printed on the terminal, you have python3 installed now.)
- Close the terminal

The reference is taken from the following [website](http://www.knight-of-pi.org/installing-python3-6-on-a-raspberry-pi/)

# Step 2: Enabling i2c on Raspberry Pi
- Goto the following directory  /etc/modules-load.d/
- Open "modules.conf" file and write **i2c-dev** in the end and save the file
*********
- After that, open the following file  /etc/modprobe.d/raspi-blacklist.conf
- Comment the line (by adding # in the start) that says **blacklist i2c-bcm2708** and save the file
- Open terminal and enter this line  

      $ sudo apt-get update && sudo apt-get install i2c-tools    
      $ sudo adduser USER i2c       

  (write username in place of USER which is 'pi' by default)
        
- Update the boot file by:

      $ sudo nano /boot/config.txt
  write the following lines in the end

      dtparam=i2c_arm=on
      dtparam=i2c1=on
  Press **Ctrl+X**. Then press **Y** and hit **Enter** 

# Step 3: Installing quick2wire library
- Install git by writing following lines in terminal

      $  sudo apt-get install git
      
- Download quick2wire API by:

      $ git clone https://github.com/quick2wire/quick2wire-python-api.git

- Now, we need to enable Python to access this APi. 
  Open **~/.profile** and add the following lines in the end
    
    **export PYTHONPATH=$PYTHONPATH:$HOME/quick2wire-python-api**
    
    replace $PYTHONPATH with the path where the python is installed; and $HOME with the path where your downloaded API is stored.
    
  For example, in my case, it is: **export PYTHONPATH=/home/pi/Python-3.6.3:/home/pi/quick2wire-python-api**
    
  NOTE: **~/** is the slang for directory **/home/pi/**. The **.profile** file will be hidden, so make the hidden files visible first.
  
  Save and close the file
  
- Reboot your Raspberry Pi

      $ sudo reboot

# Step 4: Connecting GY-85 and checking the connection

- Connect GY-85 with Raspberry Pi.
- Open terminal and write:

      $ sudo i2cdetect -y 1
   
   where **1** is the port number for newer version of Raspberry Pi. If you're using older model of Raspberry Pi, write **0** instead
   
   This will show the address of connected devices.
   
   Accelerometer(ADXL): **53**
   
   Gyroscope(ITG): **68**
   
   Compass(HMC): **0d**
   
   
# Step 5: Downloading the code files

- Open the terminal and download the code files
      $ 
 
Main reference source:
https://topic.alibabacloud.com/a/raspberry-pi-connects-9-axis-imu-sensor-gy-85-module_8_8_32153608.html
