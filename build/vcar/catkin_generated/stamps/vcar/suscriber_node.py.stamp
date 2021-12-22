#!/usr/bin/python3.8
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("RECEIVED DATA: %s", data.data)

def listener():
    rospy.init_node("Suscriber_node", anonymous=True)

    # Create a suscriber object: 3 arguments:
    # -- Topic to suscribe
    # -- Type of message to recibe
    # -- callback function

    rospy.Suscriber('status', String, callback)

    # Run de node continuosly

    rospy.spin()

if __name__ =='__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
