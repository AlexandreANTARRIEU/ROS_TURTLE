#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math
from tkinter import *
import tkinter as tk

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
def squareturtle(taille):
    #création du publisher
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.init_node('warturtle', anonymous=True)
    rate = rospy.Rate(0.9)

    #taille entrée au début mise en entier
    print(taille)
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
        squareturtle(taille)
    except rospy.ROSInterruptException:
        pass