    # !/usr/bin/python
# -*- coding:utf-8 -*-

# import sys
# sys.path.append("C:/Users/sabdi/Documents/GitHub/gForceSDKPython") # CDCL Desktop

from gforce import GForceProfile, NotifDataType, DataNotifFlags
import time
import struct
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Float64MultiArray


class OyMotionData:

    _GF = GForceProfile()

    _packet_cnt = 0
    _start_time = 0

    _EMG     = []
    _EMG_pub = []
    _EMG_gesture     = []
    _EMG_gesture_pub = []
    _orientation     = []
    _orientation_pub = []

    _subscribers = []

    def __init__(self):
        # GF = GForceProfile()

        rospy.init_node('Oymotion_Cuff', anonymous=True)

        cuff_EMG_pub  = rospy.Publisher('/oymotion_emg', Float64MultiArray, latch=True, queue_size=10)
        self._EMG_pub.append(cuff_EMG_pub)

        msg = Float64MultiArray()
        msg.data = [128]*129
        self._EMG_pub[0].publish(msg)

        cuff_quat_pub = rospy.Publisher('/oymotion_quat', Float64MultiArray, queue_size=10)
        self._orientation_pub.append(cuff_quat_pub)

        cuff_gest_pub = rospy.Publisher('/oymotion_gest', Int16, latch=True,queue_size=10)
        self._EMG_gesture_pub.append(cuff_gest_pub)
        
        msg = Int16()
        msg.data = 0
        self._EMG_gesture_pub[0].publish(msg)

    def set_cmd_cb(self,resp):
        print('Command result: {}'.format(resp))

    def ondata(self,data):

        if len(data) > 0:
            print('data.length = {0} \ncontent = {1}'.format(len(data), data))

            if data[0] == NotifDataType['NTF_QUAT_FLOAT_DATA'] and len(data) == 17:
                quat_iter = struct.iter_unpack('f', data[1:])
                quaternion = []
                for i in quat_iter:
                    quaternion.append(i[0])

                # print('quaternion:', quaternion)

                # Publishing datat to ROS topic /oymotion_quat
                msg = Float64MultiArray()
                msg.data = quaternion
                self._orientation_pub[0].publish(msg)

            elif data[0] == NotifDataType['NTF_EMG_ADC_DATA'] and len(data) == 129:
                # Data for EMG CH0~CHn repeatly.
                # Resolution set in setEmgRawDataConfig:
                #   8: one byte for one channel
                #   12: two bytes in LSB for one channel.
                # eg. 8bpp mode, data[1] = channel[0], data[2] = channel[1], ... data[8] = channel[7]
                #                data[9] = channel[0] and so on
                # eg. 12bpp mode, {data[2], data[1]} = channel[0], {data[4], data[3]} = channel[1] and so on
                
                # for i in range(1, 129):
                #     print(data[i])

                if self._start_time == 0:
                    self._start_time = time.time()
                
                self._packet_cnt += 1
                
                if self._packet_cnt % 100 == 0:
                    period = time.time() - self._start_time
                    sample_rate = 100 * 16 / period     # 16 means repeat times in one packet
                    byte_rate = 100 * len(data) / period
                    print('----- sample_rate:{0}, byte_rate:{1}'.format(sample_rate, byte_rate))

                    self._start_time = time.time()

                # Publishing datat to ROS topic /oymotion_emg
                msg = Float64MultiArray()
                msg.data = data
                self._EMG_pub[0].publish(msg)

            elif data[0] == NotifDataType['NTF_EMG_GEST_DATA'] and len(data) == 2:

                msg = Int16()
                msg.data = data[1]
                self._EMG_gesture_pub[0].publish(msg)

if __name__ == '__main__':


    cuff_data = OyMotionData()
    time.sleep(1)

    run = True

    while run:
        print("Scanning devices...")

        # Scan all gforces,return [[num,dev_name,dev_addr,dev_Rssi,dev_connectable],...]
        scan_results = cuff_data._GF.scan(5)

        print(" scan_results length : ", len(scan_results))

        if scan_results == []:
            print('No bracelet was found')
        else:
            for d in scan_results:
                print('{0:<1}: {1:^16} {2:<18} Rssi={3:<3}, connectable:{4:<6}'.format(*d))

        # Hardcoding button select for Oymotion Cuff and address to connect to
        button = 1
        addr = scan_results[button-1][2]
        cuff_data._GF.connect(addr)

        # Setting up EMG Data Output
        sampRate    = 650
        channelMask = 0xFF 
        dataLen     = 128
        resolution  = 8
        cuff_data._GF.setEmgRawDataConfig(sampRate, channelMask, dataLen, resolution, cb=cuff_data.set_cmd_cb, timeout=1000)
        time.sleep(1)

        # While loop that retrieves data from cuff and publishes to rostopics
        while run:

            # cuff_data._GF.setDataNotifSwitch(DataNotifFlags['DNF_QUATERNION'] | DataNotifFlags['DNF_EMG_RAW'], cuff_data.set_cmd_cb, 1000)
            cuff_data._GF.setDataNotifSwitch(DataNotifFlags['DNF_EMG_GESTURE'] | DataNotifFlags['DNF_QUATERNION'], cuff_data.set_cmd_cb, 1000)
            cuff_data._GF.startDataNotification(cuff_data.ondata)
            time.sleep(1)

            while True:
                button = input()

                print("button = '",button,"'" )
                if len(button) != 0:
                    cuff_data._GF.stopDataNotification()
                    cuff_data._GF.setDataNotifSwitch(DataNotifFlags['DNF_OFF'], cuff_data.set_cmd_cb, 1000)
                    run = False
                    break
                time.sleep(1)

        while True:
            button = input()

            print("button = '",button,"'" )
            if len(button) != 0:
                run = False
                break