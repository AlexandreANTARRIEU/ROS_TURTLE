#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    print("je parle")
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
