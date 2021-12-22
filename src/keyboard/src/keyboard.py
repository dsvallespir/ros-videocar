#!/usr/bin/python3.8

import rospy
from pynput.keyboard import Key, Listener
from std_msgs.msg import UInt8

msg = list

def on_press(key):
    if not msg.index(key):
        msg.append(key)

def on_release(key):
    msg.index(key)
    if msg.index:
        msg.remove(key)

def publisher():
    pub = rospy.Publisher('status', UInt8, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(5)
    rospy.loginfo("Publisher Node Started, now publishing messages")
    while not rospy.is_shutdown():
        #   msg.append("%s" % rospy.get_time())
        pub.publish(msg)
        rate.sleep()

if __name__ =='__main__':
    
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
