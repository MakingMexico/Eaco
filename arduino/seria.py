import sys
import urllib3
import serial
import datetime
ser = serial.Serial('COM4')  # open serial port
while True:
    x = ser.read()     # write a string
    x = x.decode("utf-8")
    if x == "1":
        http = urllib3.PoolManager()
        fec = str(datetime.datetime.now())
        r = http.request('POST', 'http://127.0.0.1:8000/home/', fields={'fecha': fec})
ser.close()