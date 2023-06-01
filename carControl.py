
""" 
moving: True, False
steer: 0-180
gear: reverse, normal, fast
 """
gears = ["reverse", "normal", "fast"]

carStatus = {
    "moving": False,
    "steer": 90,
    "gear": "normal"
}

def setSteer(angle):
    carStatus["steer"] = angle
    if (type(angle) != int or angle > 180 or angle < 0):
        return False
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




