#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from getkey import getkey, keys


def command():
    commande = Twist()


    rospy.loginfo("Direction zqsd :")
    direction = getkey()
    if direction == "z":
        print("J'avance")
        commande.linear.x = 1.0
    elif direction == "s":
        print("Je recule")
        commande.linear.x = -1.0
    elif direction == "q":
        print("Je tourne vers la gauche")
        commande.angular.z = 1.0
    elif direction == "d":
        print("Je tourne vers la droite")
        commande.angular.z = -1.0
    return commande

def directionturtle():
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.init_node('directionturtle', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():

        commande = command()
        rospy.loginfo(commande)
        pub.publish(commande)
        rate.sleep()


if __name__ == '__main__':
    try:
        directionturtle()
    except rospy.ROSInterruptException:
        pass
