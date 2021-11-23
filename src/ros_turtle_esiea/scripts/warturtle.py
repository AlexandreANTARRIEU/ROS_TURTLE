#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math

#Séquence corespondant à un carré
def command(direction, taille):
    #défini le type de message
    commande = Twist()

    #gestion de la direction
    if direction == 1:
        commande.linear.x = taille
    elif direction == 2:
        commande.angular.z = math.pi/2 #équivalent 90°
    elif direction == 3:
        commande.linear.x = taille
    elif direction == 4:
        commande.angular.z = math.pi/2 #équivalent 90°
    elif direction == 5:
        commande.linear.x = taille
    elif direction == 6:
        commande.angular.z = math.pi/2 #équivalent 90°
    elif direction == 7:
        commande.linear.x = taille
    elif direction == 8:
        commande.angular.z = math.pi/2 #équivalent 90°
    return commande

#Crée le publisher et publie les messages au topic
def squareturtle(taille):
    #création du publisher
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.init_node('warturtle', anonymous=True)
    rate = rospy.Rate(0.9)

    #taille entrée au début mise en entier
    tailleint = int(taille)

    #jeu en continu
    while not rospy.is_shutdown():

        i = 0
        while i < 8:
            i = i+1
            commande = command(i, tailleint)
            rospy.loginfo(commande)
            pub.publish(commande)
            rate.sleep()


if __name__ == '__main__':
    try:
        taille = input("entrer la taille d'un coté du carré")
        squareturtle(taille)
    except rospy.ROSInterruptException:
        pass