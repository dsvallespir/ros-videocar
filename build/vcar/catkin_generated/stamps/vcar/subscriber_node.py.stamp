#!/usr/bin/python3.8
import rospy
from std_msgs.msg import String

pub = None

def callback(data):
    rospy.loginfo("RECEIVED DATA: %s", data.data)
    pub.publish(data.data)

def listener():
    rospy.init_node("subscriber_node", anonymous=True)

    # Create a suscriber object: 3 arguments:
    # -- Topic to suscribe
    # -- Type of message to recibe
    # -- callback function

    rospy.Subscriber('keyboard_control', String, callback)

    # Run de node continuosly

    rospy.spin()

if __name__ =='__main__':
    
    pub = rospy.Publisher('cmd_serial', String, queue_size=20)

    try:
        listener()
    except rospy.ROSInterruptException:
        pass
