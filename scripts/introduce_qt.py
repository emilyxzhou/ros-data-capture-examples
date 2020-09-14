#!/usr/bin/env python


import rospy
from std_msgs.msg import Bool, String


rospy.init_node('introduce_qt')
say_publisher = rospy.Publisher("cordial/say", String, queue_size=1)
is_record_publisher = rospy.Publisher("data_capture/is_record", Bool, queue_size=1)


if __name__ == '__main__':
    while is_record_publisher.get_num_connections() == 0:
        rospy.sleep(0.1)
    is_record_publisher.publish(Bool(data=True))

    text_to_say = "Hi, my name is QT! Nice to meet you!"

    rospy.sleep(3)
    for _ in range(2):

        rospy.loginfo("Publishing message '{}'".format(text_to_say))
        say_publisher.publish(text_to_say)
        rospy.sleep(5)

    is_record_publisher.publish(data=False)
