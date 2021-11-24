#!/usr/bin/env python
import os

import rospy
from geometry_msgs.msg import Twist
import math
from tkinter import *
import tkinter as tk
from turtlesim.srv import Spawn

taille = "0"

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
def squareturtle():
    #création du publisher
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.init_node('warturtle', anonymous=True)

    #pub2 = rospy.Publisher("/turtle2/cmd_vel", Twist, queue_size=10)
    #rospy.init_node('warturtle', anonymous=True)
    rate = rospy.Rate(0.9)

    #taille entrée au début mise en entier
    print(taille)
    tailleint = int(taille)
    j = 1

    #jeu en continu
    while not rospy.is_shutdown():

        i = 0

        while i < 8:
            i = i+1
            commande = command(i, tailleint)

            rospy.loginfo("turtle1")
            rospy.loginfo(commande)
            pub.publish(commande)
            rate.sleep()

        if j == 1:
            j = 2
            tailleint = tailleint*2
        elif j ==2 :
            j = 1
            tailleint = tailleint/2


def chekbox():
    window = tk.Tk()
    window.title('Sélection de la taille du carré')
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
        #spawn_turtle = rospy.ServiceProxy('spawn', Spawn)
        #spawn_turtle(5.5, 5.5, 0.2, "turtle2")
        squareturtle()
    except rospy.ROSInterruptException:
        pass