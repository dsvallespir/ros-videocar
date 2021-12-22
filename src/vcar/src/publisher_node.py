#!/usr/bin/python3.8
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('status', String, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("Publisher Node Started, now publishing messages")
    while not rospy.is_shutdown():
        msg = "Hello.. I am videoCar - %s" % rospy.get_time()
        pub.publish(msg)
        rate.sleep()

if __name__ =='__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
