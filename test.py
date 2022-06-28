import torch
import cv2
import numpy as np
import Jetson.GPIO as GPIO
import time

# INFERENCE SETUP
model = torch.hub.load('./yolov5', 'custom', path='./best.pt', source='local')
cam = cv2.VideoCapture(1)

# HARDWARE SETUP
# Pin Definition
led_pin = 7

# Set up the GPIO channel
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

while True:
	success, video = cam.read()
	results = model(video, size=640)
	index = results.pandas().xyxy[0]

	# returns a Pandas.Series array containing names if objects are detected
	name = index["name"].array

	# if objects are detected turn on LED; else, turn off LED
	if len(name) == 0:
		GPIO.output(led_pin, GPIO.LOW)
	else:
		GPIO.output(led_pin, GPIO.HIGH)
	
	
	cv2.imshow('video', np.squeeze(results.render()))
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# clean up code
cam.release()
cv2.destroyAllWindows()
GPIO.cleanup()
