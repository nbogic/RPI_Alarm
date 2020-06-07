# Libraries
import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer = 14
led = 18
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)
TRIG = 23
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)
GPIO.setup(ECHO,GPIO.IN)

sleep(0.1)
has_beeped = False

while True:
    GPIO.output(TRIG,1)
    sleep(0.00001)
    GPIO.output(TRIG,0)
    
    while GPIO.input(ECHO) == 0:
        pass
    start = time.time()
    
    while GPIO.input(ECHO) == 1:
        pass
    stop = time.time()
    result = (stop - start) * 170
    print(result)
    
    if result < 0.09:
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(buzzer,GPIO.LOW)
        sleep(0.5)
        GPIO.output(led,GPIO.HIGH)
        sleep(0.03)
        GPIO.output(led,GPIO.LOW)
        has_beeped = True
        
    else:
        GPIO.output(buzzer,GPIO.LOW)
        GPIO.output(led,GPIO.LOW)
        
        if has_beeped == True:
            sleep(0.01)
            GPIO.output(led,GPIO.HIGH)
            sleep(2)
            GPIO.output(led,GPIO.LOW)

GPIO.output(buzzer,GPIO.LOW)
     
     
     
