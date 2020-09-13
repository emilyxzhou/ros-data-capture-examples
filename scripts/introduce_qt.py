#!/usr/bin/env python


import rospy
from std_msgs.msg import String


rospy.init_node('introduce_qt', anonymous=True)
say_publisher = rospy.Publisher("cordial/say", String, queue_size=1)


if __name__ == '__main__':

    text_to_say = "Hi, my name is QT! Nice to meet you!"

    rospy.sleep(5)
    for _ in range(3):

        rospy.loginfo("Publishing message '{}'".format(text_to_say))
        say_publisher.publish(text_to_say)
        rospy.sleep(5)
