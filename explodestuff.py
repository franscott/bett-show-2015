import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.output(11, False)
GPIO.output(12, False)
GPIO.output(13, False)
GPIO.output(16, False)

GPIO.setup(7, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN)
GPIO.setup(22, GPIO.IN)

# input 7 is BANANA
# input 18 is spare
# input 22 is TURNIP

# output 11 is YELLOW balloon
# output 12 is ORANGE balloon
# output 13 is GREEN balloon
# output 16 is BOOM

touched = GPIO.LOW

i = 1
while i < 10:
    if GPIO.input(7) == touched: 
        print('Button Pushed')
        sleep(1)

        GPIO.output(11 , True)
        print('3...  ')
        sleep(1)
        GPIO.output(11 , False)
                
        GPIO.output(12 , True)
        print('2...  ')
        sleep(1)
        GPIO.output(12 , False)
                
        GPIO.output(13 , True)
        print('1...  ' )
        sleep(1)
        GPIO.output(13, False)

        GPIO.output(16, True)
        print('BOOM! ')
        sleep(1)
        GPIO.output(16, False)
        i += 1
    else:
        GPIO.output(11, False)   
        GPIO.output(12, False)
        GPIO.output(13, False)
        GPIO.output(16, False)
        print("waiting")

GPIO.cleanup()
