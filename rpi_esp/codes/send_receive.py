import serial
import time
import sys

esp_serial = serial.Serial(port="/dev/ttyS0", baudrate=9600)
esp_serial.flush()

while 1:
    a = int(input("Enter a number: "))
    esp_serial.write(a.to_bytes(1,byteorder=sys.byteorder))
    print("sent =", a)
    print("received = ",esp_serial.readline().decode('utf-8').rstrip())
    time.sleep(1)

