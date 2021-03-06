#!/usr/bin/env python

import rospy #importar ros para python
from sensor_msgs.msg import Image
import cv2
import numpy as np
from cv_bridge import CvBridge
fx=167.856
fy=169.605
cx=152.939
cy=111.756
Dpx=3.5
Dpy=3

class buscadores(object):
	def __init__(self,args):
         	#def publicar(self):
		self.args = args
		super(buscadores,self).__init__()		
		self.publisher = rospy.Publisher("/geometry_msg/Point",Image, queue_size=10)		
		self.publisher = rospy.Publisher("/godduck",Image, queue_size=10)
                self.subscriber = rospy.Subscriber("/duckiebot/camera_node/image/rect",Image,self.callback)
		self.bridge = CvBridge()
		self.image = Image()

	def callback(self,msg):
		#deteccion de patos:
		change = self.bridge.imgmsg_to_cv2(msg,"bgr8")
		imageinHSV = cv2.cvtColor(change, cv2.COLOR_BGR2HSV) #cambiar entre espacios de colores
		mask= cv2.inRange(imageinHSV,(20, 100, 150), (35, 255, 255))
		kernel = np.ones((3,3),np.uint8)       # Matriz de 1 s de 3x3 ocupada en las transfo
		img_out = cv2.erode(mask, kernel, iterations = 1)
		img_out = cv2.dilate(mask, kernel, iterations = 1)
		image_out = cv2.bitwise_and(change,change,mask = img_out)
		hola, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #buscar contornos de blobs
		
		for contorno in contours:
			area=cv2.contourArea(contorno)
			if (area>400):
				x,y,w,h = cv2.boundingRect(contorno)
				cv2.rectangle(change, (x,y), (x+w,y+h), (0,0,0), 2)
				#medidor de distancia		
				z=(fx/(x+w))*Dpx
				u=x+w/2 
				v=y+h/2
				x3=(u-cx)*z/fx
				y3=(v-cy)*z/fy
				z3=z
				
		msg = self.bridge.cv2_to_imgmsg(change,"bgr8")
		self.publisher.publish(msg)  
		self.publisher.publish(z3)
		#medidor de diostancia:

		


def main():
	rospy.init_node('test') #creacion y registro del nodo!
	obj = buscadores('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
