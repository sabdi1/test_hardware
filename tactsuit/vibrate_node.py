import sys
sys.path.append("C:/Users/cdcl_/Desktop/Github/tact-python")

from time import sleep
from bhaptics import haptic_player
import keyboard
import msvcrt


def run():

    player = haptic_player.HapticPlayer()
    sleep(0.4)


    interval = 0.5
    durationMillis = 100

    node = 0
    side = "front"

    print("Press Q to quit")
    while True:


        if msvcrt.kbhit():          

            key = keyboard.read_key()
            print('Key: ', key)


            if key == "q" or key == "Q":
                break
            elif key == "up":
                node = node - 4
            elif key == "down":
                node = node + 4
            elif key == "left":
                node = node - 1
            elif key == "right":
                node = node + 1
            elif key == "f":
                side = "front"
            elif key == "b":
                side = "back"

            if node < 0:
                node = 0
            elif node > 19:
                node = 19
        else:
            if side == "front":
                player.submit_dot("frontFrame", "VestFront", [{"index": node, "intensity": 100}], durationMillis)
                sleep(interval)
            else:
                player.submit_dot("backFrame", "VestBack", [{"index": node, "intensity": 100}], durationMillis)
                sleep(interval)

        print('node:', node)





        # print('=================================================')
        # print('is_playing', player.is_playing())
        # print('is_playing_key(CenterX)', player.is_playing_key('CenterX'))
        # print('is_device_connected(Vest)', player.is_device_connected('Vest'))
        # print('is_device_connected(ForearmL)', player.is_device_connected('ForearmL'))
        # print('=================================================')


if __name__ == "__main__":
    run()