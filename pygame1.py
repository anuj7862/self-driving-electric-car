import pygame
import time
import datetime
import serial
ser = serial.Serial("/dev/ttyUSB0",115200,timeout=0)
pygame.init()
pygame.joystick.init()

done = False

sign_speed = '+'
backward_speed_val = -1
forward_speed_val = -1
start_val = 0
stop_val = 0
break_val = 0
angle_val = 0
speed_val = 0
camera_val = 0
data_val = 0
break_val = 0
previous_time = datetime.datetime.now()

while not done:
	joystick = pygame.joystick.Joystick(0)
	joystick.init()
	for event in pygame.event.get():
		if event.type == pygame.JOYAXISMOTION:
			#print(event)
			if(event.axis == 0):
				prev_angle_val = angle_val
				angle_val = event.value
				angle_val = int(float(angle_val)*255.)
				if((prev_angle_val > 5 and angle_val < -5) or (prev_angle_val < -5 and angle_val > 5)):
					angle_val = 0
				print(angle_val)
			elif(event.axis == 5):
				forward_speed_val = event.value*(1.)
			elif(event.axis == 2):
				backward_speed_val = event.value
		elif event.type == pygame.JOYBUTTONDOWN:
			#print(event.button)
			if(event.button == 7):
				print("START THE CAR")
				start_val = 1
			elif(event.button == 2):
				if sign_speed == '+':
					sign_speed = '-'
					backward_speed_val = -1
				elif sign_speed == '-':
					sign_speed = '+'
					forward_speed_val = -1
			elif(event.button == 8):
				print("STOP THE CAR")
				start_val = 0
			elif(event.button == 6):
				print("Nothing1")
			elif(event.button == 3):
				print("Nothing2")
			elif(event.button == 0):
				print("Nothing3")
				#data_val = 1
			elif(event.button == 1):
				print("Break")
				if break_val == 0:
					break_val = 1 #data_val = 0
				else:
					break_val = 0				
		elif event.type == pygame.JOYHATMOTION:
			if(event.value == (-1, 0)):
				print("DATA_COLLECTION_STOP")
				data_val = 0
			elif(event.value == (1, 0)):
				print("DATA_COLLECTION_Start")
				data_val = 1
			elif(event.value == (0,-1)):
				print("CAMERA_STOP")
				camera_val = 0
			elif(event.value == (0,1)):
				print("CAMERA_START")
				camera_val = 1
		if sign_speed == '+' :
			speed = forward_speed_val
		elif sign_speed == '-':
			speed = backward_speed_val
		
		if int(angle_val) <0:
			sign_angle = '-'
			angle = (angle_val)*(-1)
		else:
			sign_angle = "+"
			angle = angle_val
		angle = format(int(angle),'03d')
		speed = format(int((float(speed)+1)*255/2),'03d')
		send_str = str(start_val) + str(break_val) +sign_angle + str(angle) +sign_speed+ str(speed) + "\n"
		a = datetime.datetime.now()
		c = a - previous_time
		if(c.microseconds > 1000):
			previous_time = a		
			ser.write(send_str.encode())
			print(send_str)
			print("written")
		 
#print(event.value)#elif event.type == pygame.JOYAXISMOTION:
#    self.axis_moving.emit(event.axis, event.value
print("sfls")



