#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math
from tkinter import *
import tkinter as tk
from turtlesim.srv import Spawn


taille = "0"

#Séquence corespondant à un carré
def command(angle, taille):
    #défini le type de message
    commande = Twist()

    commande.linear.x = taille
    commande.angular.z = angle

    return commande

#Séquence corespondant à un carré
def command2(angle, taille):
    #défini le type de message
    commande = Twist()

    commande.linear.x = taille
    commande.angular.z = angle

    return commande

#Crée le publisher et publie les messages au topic
def squareturtle(taille):
    #création du publisher
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.init_node('warturtle', anonymous=True)

    pub2 = rospy.Publisher("/turtle2/cmd_vel", Twist, queue_size=10)
    rospy.init_node('warturtle', anonymous=True)

    rate = rospy.Rate(0.9)

    #taille entrée au début mise en entier
    print(taille)
    tailleint = int(taille)
    angle = math.pi/2
    #jeu en continu
    while not rospy.is_shutdown():
        i = 0
        while i < 2:
            if i == 0:
                j=1
            else:
                j=-1
            i = i + 1
            commande = command(j*angle,tailleint)
            commande2 = command(j*-angle,tailleint)
            rospy.loginfo(commande)
            pub.publish(commande)
            pub2.publish(commande2)
            rate.sleep()
            commande = command(j*-angle, tailleint)
            commande2 = command(j*angle, tailleint)
            pub.publish(commande)
            pub2.publish(commande2)
            rate.sleep()
            commande = command(j*-angle, tailleint)
            commande2 = command(j*angle, tailleint)
            rospy.loginfo(commande)
            pub.publish(commande)
            pub2.publish(commande2)
            rate.sleep()
            commande = command(j*-angle, tailleint)
            commande2 = command(j*angle, tailleint)
            pub.publish(commande)
            pub2.publish(commande2)
            rate.sleep()


def chekbox():
    window = tk.Tk()
    window.title('Sélection de la taille du rond')
    window.geometry('300x100')


    def getEntry():
        global taille
        taille = myEntry.get()
        window.destroy()


    myEntry = tk.Entry(window, width=40)
    myEntry.pack(pady=20)
    btn = tk.Button(window, height=1, width=10, text="Valider", command=getEntry)
    btn.pack()
    window.mainloop()

if __name__ == '__main__':
    try:
        chekbox()
        spawn_turtle = rospy.ServiceProxy('spawn', Spawn)
        spawn_turtle(4, 4, 0.2, "turtle2")
        squareturtle(taille)
    except rospy.ROSInterruptException:
        pass