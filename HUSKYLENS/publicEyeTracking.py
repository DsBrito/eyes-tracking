


# #!/usr/bin/env python
# #mudanças aqui
# import rospy
# import time

# from std_msgs.msg import String
# from geometry_msgs.msg import Point
# from std_msgs.msg import Bool
# from std_msgs.msg import Float32

# import Adafruit_PCA9685

# import random
# import time
# import subprocess
# import json
# from huskylib import HuskyLensLibrary

# huskylens = HuskyLensLibrary("I2C","", address=0x32)




# def eye_tracking(object):
#     def _init_(self, name, Channel, ZeroOffset):
#         self.name = name
#         rospy.init_node(self.name)
#         self.rate = rospy.Rate(10) # 10hz
#         self.initPublishers()
#         self.initVariables()
            
#         self.Channel = Channel
#         self.ZeroOffset = ZeroOffset

#     def initPublishers(self):
#         while True:
#             try:
#                 block = huskylens.blocks()
#                 x, y = block.x, block.y
#                 print(x, y)
#                 self.pubMoveEyes = rospy.Publisher("/moveEyes", Point, queue_size = 10)
#                 self.eyesPosition.x = x
#                 self.eyesPosition.y = y
#                 self.eyesPosition.z = 0
#                 self.pubMoveEyes.publish(self.eyesPosition)
#                 time.sleep(0.1)                
#             except Exception as e:
#                         continue
#             except KeyboardInterrupt:
#                         print("\nQUITING")
#                         quit()

# eye_tracking()


#!/usr/bin/env python
# mudanças aqui
import rospy
import time

from std_msgs.msg import String
from geometry_msgs.msg import Point
from std_msgs.msg import Bool
from std_msgs.msg import Float32

import Adafruit_PCA9685

import random
import subprocess
import json
from huskylib import HuskyLensLibrary

huskylens = HuskyLensLibrary("I2C", "", address=0x32)

class EyeTracking:
    def __init__(self, name, Channel, ZeroOffset):
        self.name = name
        self.Channel = Channel
        self.ZeroOffset = ZeroOffset
        rospy.init_node(self.name)
        self.rate = rospy.Rate(10)  # 10hz
        
        self.eyesPosition = Point() #MUDEI AQUI
        
        self.initPublishers() #mudei aqui

    def initPublishers(self):
        self.pubMoveEyes = rospy.Publisher("/moveEyes", Point, queue_size=10)

    def track_object(self):
        while not rospy.is_shutdown():
            try:
                block = huskylens.blocks()[0]  
                x, y = block.x, block.y
                print(x, y)

                self.eyesPosition.x = x
                self.eyesPosition.y = y
                self.eyesPosition.z = 0
                self.pubMoveEyes.publish(self.eyesPosition)

                self.rate.sleep()
            except IndexError:
                # Nenhum bloco detectado
                continue
            except Exception as e:
                rospy.logerr("Erro: {}".format(e))
            except KeyboardInterrupt:
                print("\nSAINDO")
                break

if __name__ == "__main__":
    try:
        eye_tracker = EyeTracking("eye_tracker_node", channel=1, zero_offset=0)
        eye_tracker.track_object()
    except rospy.ROSInterruptException:
        pass
