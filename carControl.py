import RPi.GPIO as GPIO
import pigpio
import time


STEER_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(STEER_PIN, GPIO.OUT)
# GPIO.setwarnings(False)

pwmSteering = GPIO.PWM(STEER_PIN, 50)  # 50 Hz frequency
pwmSteering.start(2.5)  # 0 degree

# time where the last steer was set

""" 
moving: True, False
steer: 0-180
gear: reverse, normal, fast
 """
gears = ["reverse", "normal", "fast"]

carStatus = {
    "moving": False,
    "steer": 2.5,
    "gear": "normal"
}
# deg : 180 == x : 12
def degreeToPwm(degree):
    return (degree * 12) / 180


def setSteer(angle):
    if (type(angle) != int or angle > 180 or angle < 0):
        return False
    pwmSteering.ChangeDutyCycle(degreeToPwm(angle))
    print("Stee pwm: ", angle)
    carStatus["steer"] = angle
    return True


def setMoving(moving):
    carStatus["moving"] = moving
    if (type(moving) != bool):
        return False
    return True


def setGear(gear):
    carStatus["gear"] = gear
    if (gear not in gears):
        return False
    return True


def getCarStatus():
    return carStatus


# 0-180
""" ranges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90,
          100, 110, 120, 130, 140, 150, 160, 170, 180]

for i in ranges:
    
    print("Steer: ", i)
    setSteer(i)
    print ("Sleeping: ", i)
    time.sleep(0.5)



setSteer(80) """

""" pwmSteering.stop()
GPIO.cleanup() """
