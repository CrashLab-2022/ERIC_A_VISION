#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray  
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
from darknet_ros_msgs.msg import BoundingBoxes
import rospkg
from darknet_ros_msgs.srv import Speak, SpeakRequest
import time
class human():
    def __init__(self):
        self.subs=[]
        self.cnt=0
        self.subs.append(rospy.Subscriber('darknet_ros/bounding_boxes', BoundingBoxes, self.callback))
        self.is_callback=True

    def callback(self, data):
        n=len(data.bounding_boxes)
        for i in range(0,n):
            # rospy.loginfo("hi")
            if data.bounding_boxes[i].id==0:
                rospy.loginfo(self.cnt)

                if self.cnt==0:
                    rospy.loginfo(self.speakclient())
                    # if self.speakclient() == 'finish':
                    #     self.cnt=-2

                self.cnt+=1

                if self.cnt==30:
                    self.cnt=0

        
    
    def speakclient(self):
        # rospy.wait_for_service('play_song')
        try:
            play=rospy.ServiceProxy('play_song', Speak)
            rospy.loginfo("detect")
            return play(1)

        except rospy.ServiceException as e:
            rospy.loginfo("Service call failed: ")

if __name__ == '__main__':
    rospy.init_node('human_detect', anonymous=True)
    cls_=human()
    rospy.spin()