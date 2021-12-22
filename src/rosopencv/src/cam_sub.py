#!/usr/bin/python3.8

import rospy
from rospy.client import init_node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def callback(data):
    br = CvBridge()
    rospy.loginfo("receiving video frame")

    current_frame = br.imgmsg_to_cv2(data)
    resized_frame = cv2.resize(current_frame, (640, 480))
    cv2.imshow("camera", resized_frame)
    cv2.waitKey(1)

def receive_message():

    rospy.init_node('cam_sub_node', anonymous=True)

    rospy.Subscriber('video_frames', Image, callback)

    rospy.spin()

    cv2.DestroyAllWindows()

if __name__=='__main__':
    receive_message()