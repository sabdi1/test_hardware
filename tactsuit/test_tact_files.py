import sys
sys.path.append("C:/Users/cdcl_/Desktop/Github/tact-python")

from time import sleep
from bhaptics import haptic_player
import keyboard


def run():

    player = haptic_player.HapticPlayer()
    sleep(0.4)

    player.initialize()

    # tact file can be exported from bhaptics designer
    print("Registering Tact Files:")
    player.register("BackCol1", "back_col_1.tact")
    player.register("BackCol2", "back_col_2.tact")
    player.register("BackCol3", "back_col_3.tact")
    player.register("BackCol4", "back_col_4.tact")
    player.register("BackRow1", "back_row_1.tact")
    player.register("BackRow2", "back_row_2.tact")
    player.register("BackRow3", "back_row_3.tact")
    player.register("BackRow4", "back_row_4.tact")
    player.register("BackRow5", "back_row_5.tact")

    player.register("FrontCol1", "front_col_1.tact")
    player.register("FrontCol2", "front_col_2.tact")
    player.register("FrontCol3", "front_col_3.tact")
    player.register("FrontCol4", "front_col_4.tact")
    player.register("FrontRow1", "front_row_1.tact")
    player.register("FrontRow2", "front_row_2.tact")
    player.register("FrontRow3", "front_row_3.tact")
    player.register("FrontRow4", "front_row_4.tact")
    player.register("FrontRow5", "front_row_5.tact")
    print("Completed Registering Tact Files.")

    interval = 0.5
    durationMillis = 100

    for i in range(20):
        print(i, "back")
        player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": 100}], durationMillis)
        sleep(interval)

        print(i, "front")
        player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": 100}], durationMillis)
        sleep(interval)


    def play(index):
        if index == 1:
            print("submit CenterX")
            player.submit_registered("CenterX")
        elif index == 2:
            print("submit Circle")
            player.submit_registered_with_option("Circle", "alt",
                                                scale_option={"intensity": 1, "duration": 1},
                                                rotation_option={"offsetAngleX": 180, "offsetY": 0})
        elif index == 3:
            print("submit Circle With Diff AltKey")
            player.submit_registered_with_option("Circle", "alt2",
                                                scale_option={"intensity": 1, "duration": 1},
                                                rotation_option={"offsetAngleX": 0, "offsetY": 0})


    print("Press Q to quit")
    while True:
        key = keyboard.read_key()
        if key == "q" or key == "Q":
            break
        elif key == "1":
            play(1)
        elif key == "2":
            play(3)
        elif key == "3":
            play(3)


        print('=================================================')
        print('is_playing', player.is_playing())
        print('is_playing_key(CenterX)', player.is_playing_key('CenterX'))
        print('is_device_connected(Vest)', player.is_device_connected('Vest'))
        print('is_device_connected(ForearmL)', player.is_device_connected('ForearmL'))
        print('=================================================')


if __name__ == "__main__":
    run()