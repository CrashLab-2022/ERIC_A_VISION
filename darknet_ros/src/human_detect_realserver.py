#!/usr/bin/env python

import rospy
import rospkg
from darknet_ros_msgs.srv import Speak, SpeakResponse
import os

class fileRoot(object):
    pkg_path = rospkg.RosPack()
    path = pkg_path.get_path('darknet_ros')
    # web = pkg_path.get_path('hongdo_ros_web')


# class SoundStart:
#     # voice_path=None
#     sound_path=None

#     def __init__(self, sound_path = None):
#         # self._voice_path=vocie_path
#         self._sound_path=sound_path

#     # def play_voice(self, req):
#     #     rospy.loginfo("voice :  %s"%req.sequence)
#     #     os.system('play ' + self._voice_path +'/%s.mp3'%req.sequence)
#     #     return SpeakResponse('finish')

#     def play_sound(self,req):
#         rospy.loginfo("background sound :  %s"%req.sequence)
#         os.system('play ' + self._sound_path +'/%s.mp3'%req.sequence)
#         return SpeakResponse('finish')

#     def __del__(self):
#         self._voice_path=None
#         self._sound_path=None

class EricAspeakNode:
    def __init__(self):
        #sound
        # voice_path = fileRoot.webconnect + '/sound'
        # sound_path = fileRoot.speak_path + '/sound'

        # self.sound_start=SoundStart(sound_path)

        ##service
        rospy.Service('/play_song', Speak, self.play_sound)
        # rospy.Service('/play_voice', Speak, self.sound_start.play_voice)
        
        # self.opencvStart()
        rospy.loginfo('Ready to eric_a_speak Node')
        rospy.on_shutdown(self.__del__)

    def main(self):
        rospy.spin()

    def play_sound(self,req):
        # rospy.loginfo(req.sequence)
        rospy.loginfo("background sound :  %s"%req.sequence)
        os.system('play ' + fileRoot.path +'/sound/%s.mp3'%req.sequence)
        return SpeakResponse('finish')

    def __del__(self):
        print("[info]terminating eric_a_speak_node")



if __name__ == '__main__':
    rospy.init_node('eirc_a_speak_node', anonymous=True)
    node= EricAspeakNode()
    node.main()