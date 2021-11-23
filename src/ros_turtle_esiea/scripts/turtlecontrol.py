#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from getkey import getkey, keys

#menu qui permet de voir quel touche est appuyer et de réagir en conséquence
def command():
    #défini le type de message
    commande = Twist()

    #détection de la touche pressee
    rospy.loginfo("Direction zqsd :")
    direction = getkey()

    #gestion de la direction
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

#Crée le publisher et publie les messages au topic
def directionturtle():
    #création du publisher
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.init_node('directionturtle', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    #jeu en continu
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
