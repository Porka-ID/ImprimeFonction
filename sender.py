# Importing Libraries
import serial
import time
grbl = serial.Serial(port='ttyUSB0', baudrate=115200, timeout=.1)
