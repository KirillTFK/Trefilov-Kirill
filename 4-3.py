import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)

n = 10
p = GPIO.PWM(22, 1000)
p.start (0)

try:
    while True:
        f = int(input("enter duty cycle "))
        p.ChangeDutyCycle(f)
        print(3.3*f/100)

finally:
    GPIO.output(p,0)
    GPIO.cleanup()