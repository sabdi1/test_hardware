#
#      ____   ____  ___    ____   __________       __   ________   _______    ________   ___  
#     /   /  /   / /   \  /    \ \   _____  \     /  / /  _____/  /  ___  \  /  _____/  /  /  
#    /   /  /   / /     \/  /\  \ \  \    |  |   /  / /  /       /  /  /  / /  /       /  /   
#   /   /__/   / /   /\____/  \  \ \  \___/  |  /  / /  /_____  /  /__/  / /  /_____  /  /____
#  /__________/ /___/          \__\ \_______/  /__/  \_______/ /________/  \_______/ /_______/ 
#

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



if __name__ == "__main__":
    run()