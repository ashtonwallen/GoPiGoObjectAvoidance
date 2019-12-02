import time
import easygopigo3 as easy

gpg = easy.EasyGoPiGo3()
dist_sensor = gpg.init_distance_sensor()
TURN_DISTANCE = 20
TURN_DEGREES = 25

while True:
    print("Distance From Object (mm): " + str(my_distance_sensor.read_mm()))
    dist = my_distance_sensor.read_mm()
    if dist <= TURN_DISTANCE:
        gpg.turn_degrees(TURN_DEGREES)
    time.sleep(.1)

