import sys
# sys.path.append("C:/Users/cdcl_/Desktop/Github/tact-python") # CDCL Laptop
sys.path.append("C:/Users/sabdi/Documents/GitHub/tact-python") # CDCL Desktop

from time import sleep
from bhaptics import haptic_player
import keyboard
import msvcrt
from keyboard_io import read_key

def run():

    player = haptic_player.HapticPlayer()
    sleep(0.4)


    durationMillis = 100
    delay = durationMillis/1000

    node = 0
    side = "front"

    print("Press Q to quit")
    done = False
    while not done:

        if msvcrt.kbhit():
            key = msvcrt.getwch()

            if key == "Q":
                done = True

            # if key != "":
            #     print("You pressed << ",key," >>")

            if key == "Q":
                break
            elif key == "w":
                node = node - 4
            elif key == "s":
                node = node + 4
            elif key == "a":
                node = node - 1
            elif key == "d":
                node = node + 1
            elif key == "f":
                side = "front"
            elif key == "b":
                side = "back"

            if node < 0:
                node = 0
            elif node > 19:
                node = 19

     
        if side == "front":
            player.submit_dot("frontFrame", "VestFront", [{"index": node, "intensity": 100}], durationMillis)
            sleep(delay)
        else:
            player.submit_dot("backFrame", "VestBack", [{"index": node, "intensity": 100}], durationMillis)
            sleep(delay)

        print('node:', node)





        # print('=================================================')
        # print('is_playing', player.is_playing())
        # print('is_playing_key(CenterX)', player.is_playing_key('CenterX'))
        # print('is_device_connected(Vest)', player.is_device_connected('Vest'))
        # print('is_device_connected(ForearmL)', player.is_device_connected('ForearmL'))
        # print('=================================================')


if __name__ == "__main__":
    run()