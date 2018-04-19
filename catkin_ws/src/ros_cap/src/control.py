#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from sensor_msgs.msg import Joy
from duckietown_msgs.msg import Twist2DStamped

class movimientos(object):
	def __init__(self):
         	#def publicar(self):
		super(movimientos, self).__init__()
		self.publisher = rospy.Publisher("/duckiebot/wheels_driver_node/car_cmd",Twist2DStamped, queue_size=10)
                self.subscriber = rospy.Subscriber("/duckiebot/joy",Joy,self.callback)
		self.twist = Twist2DStamped()
	

	def callback(self,msg):
		OY=msg.axes[1]
		OX=msg.axes[0]	
		Freno=msg.buttons[1]
		if Freno == 0:		
			self.twist.v = OY
			self.twist.omega = OX  
			self.publisher.publish(self.twist)		#que gire para la izq	


def main():
	rospy.init_node('test') #creacion y registro del nodo!
	obj = movimientos() # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
