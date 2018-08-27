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
		self.ser= serial.Serial('/dev/ttyusb0',9600)
	

	def callback(self,msg):
		OY=msg.axes[1]
		acelerador = msg.buttons[0]
		OX=msg.axes[0]	
		Freno=msg.buttons[1]
		delanteras=mdg.buttons[3]
		intizquierda=msg.buttons[4]
		intderecha=msg.buttons[5]
		if delanteras ==1
			self.ser.write('1')
		if intizquierda==1
			self.ser.write('4')
		if intderecha == 1 
			self.ser.write('3')
		if Freno == 0:		
			self.twist.v = OY
			self.twist.omega = OX  
			self.publisher.publish(self.twist)		#que gire para la izq
		if Freno==1:
			self.twist.v=0
			self.twist.omega=0
			self.publisher.publish(self.twist)
			self.ser.write('2')	


def main():
	rospy.init_node('test') #creacion y registro del nodo!
	obj = movimientos() # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
