#!/usr/bin/python3.8

import rospy
from rospy.client import init_node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def publish_message():

    pub = rospy.Publisher('video_frames', Image, queue_size=10)
    
    rospy.init_node('cam_pub_py', anonymous=True)

    rate = rospy.Rate(4)

    cap = cv2.VideoCapture(0)

    br = CvBridge()

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        frame_resized = cv2.resize(frame, (320, 240))

        if ret == True:
            rospy.loginfo("publishing video frame")

            pub.publish(br.cv2_to_imgmsg(frame_resized))

        rate.sleep()

if __name__=='__main__':
    try:
        publish_message()
    except rospy.ROSInterruptException:
        pass