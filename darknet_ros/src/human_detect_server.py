#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray  
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
from darknet_ros_msgs.msg import BoundingBoxes
import rospkg
from darknet_ros_msgs.srv import Speak, SpeakResponse
import os

# hi
# class fileRoot(object):
#     pkg_path=rospkg.RosPack()
#     path=pkg_path.get_path('darknet_ros')

class detect_server():
    def __init__(self):
        # self.sound_path=fileRoot.path + '/speak'
        self.cnt=0
        rospy.Service('play_voice', Speak, self.play_sound)

    def play_sound(self, req):
        if req.str=='detect':
            rospy.loginfo("success")
            # rospy.loginfo("voice: %s"%req.req)
            # os.system('play_voice' + self.sound_path +'/%s.mp3'%req.req)
            return SpeakResponse('success')
    
if __name__ == '__main__':
    rospy.init_node('speaker_server', anonymous=True)
    cls_=detect_server()
    rospy.spin()