import sys
sys.path.append("C:/Users/cdcl_/Desktop/Github/tact-python")

from time import sleep
from bhaptics import haptic_player


player = haptic_player.HapticPlayer()
sleep(0.4)

# # tact file can be exported from bhaptics designer
# print("register CenterX")
# player.register("CenterX", "CenterX.tact")
# print("register Circle")
# player.register("Circle", "Circle.tact")

# sleep(0.3)
# print("submit CenterX")
# player.submit_registered("CenterX")
# sleep(4)
# print("submit Circle")
# player.submit_registered_with_option("Circle", "alt",
#                                      scale_option={"intensity": 1, "duration": 1},
#                                      rotation_option={"offsetAngleX": 180, "offsetY": 0})
# print("submit Circle With Diff AltKey")
# player.submit_registered_with_option("Circle", "alt2",
#                                      scale_option={"intensity": 1, "duration": 1},
#                                      rotation_option={"offsetAngleX": 0, "offsetY": 0})
# sleep(3)

interval = 0.5
durationMillis = 100

for i in range(20):
    print(i, "back")
    player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": 100}], durationMillis)
    sleep(interval)

    print(i, "front")
    player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": 100}], durationMillis)
    sleep(interval)

# send individual point for 1 seconds
dotFrame = {
    "Position": "Left",
    "DotPoints": [{
        "Index": 0,
        "Intensity": 100
    }, {
        "Index": 3,
        "Intensity": 50
    }],
    "DurationMillis": 1000
}
player.submit("dotPoint", dotFrame)
sleep(5)

pathFrame = {
    "Position": "VestFront",
    "PathPoints": [{
        "X": "0",
        "Y": "0",
        "Intensity": 100
    }, {
        "X": "0",
        "Y": "0.25",
        "Intensity": 80
    }, {
        "X": "0",
        "Y": "0.5",
        "Intensity": 60
    }, {
        "X": "0",
        "Y": "0.75",
        "Intensity": 40
    },  {
        "X": "0",
        "Y": "1",
        "Intensity": 20
    }],
    "DurationMillis": 1000
}
player.submit("pathPoint", pathFrame)
sleep(2)
