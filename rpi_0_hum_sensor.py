import RPi.GPIO as GPIO
import time

print("run")
GPIO.setmode(GPIO.BCM)

SENSOR_PIN = 23
GPIO.setup(SENSOR_PIN, GPIO.IN)

try:
    while True:
        print("end msg..", int(time.time()))
        if GPIO.input(SENSOR_PIN):
            print("Gleba sucha")
        else:
            print("Gleba wilgotna")
        time.sleep(0.1)
except Exception as e:
    print("Error")
