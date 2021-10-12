#!/usr/bin/python3.8

import rospy
import sys
import pygame
from pynput import keyboard
from std_msgs.msg import String


def publisher():
    pub = rospy.Publisher('keyboard_control', String, queue_size=10)
    rospy.init_node('keyboard_node', anonymous=True)
    rate = rospy.Rate(10)
    rospy.loginfo("Keyboard Node Started, now publishing messages")
    while not rospy.is_shutdown():    
        msg ="null"    
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    msg = "left down"
                if event.key == pygame.K_RIGHT:
                    msg = "right down"
                if event.key == pygame.K_w:
                    msg = "w down"
                if event.key == pygame.K_s:
                    msg = "s down"
                if event.key == pygame.K_i:
                    msg = "i down"
                if event.key == pygame.K_k:
                    msg = "k down"
                if event.key == pygame.K_l:
                    msg = "l down"
                if event.key == pygame.K_j:
                    msg = "j down"
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    msg = "left up"
                if event.key == pygame.K_RIGHT:
                    msg = "right up"
                if event.key == pygame.K_w:
                    msg = "w up"
                if event.key == pygame.K_s:
                    msg = "s up"
                if event.key == pygame.K_i:
                    msg = "i up"
                if event.key == pygame.K_k:
                    msg = "k up"
                if event.key == pygame.K_l:
                    msg = "l up"
                if event.key == pygame.K_j:
                    msg = "j up"
        if not msg == "null":
            # pub.publish(msg + " - t: %s" % rospy.get_time())
            pub.publish(msg)
        rate.sleep()
    pygame.quit()

if __name__ =='__main__':

    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass