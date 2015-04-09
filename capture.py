''' The code has been written by Rishi Gaurav Bhatnagar and Rahul Thota to capture a time lapse video by merging various images over a period of time. '''
import picamera
import time
import RPi.GPIO as GPIO
'''Initialize camera '''
camera = picamera.PiCamera()
camera.resolution =(640,480)

#Initialize the GPIOs
GPIO.setmode(GPIO.BCM) #This is to name GPIOS
GPIO.setwarning(False) 
p1 = GPIO17 #RedLED
p2 = GPIO27 #GreenLED
p3 = #StartButton
p4 = #Stopbutton
#Initialize the pins to their INPUT/OUPUT nature
#GPIO.setup(pinNumber,GPIO.IN/OUT)
GPIO.setup(p1,GPIO.OUT) 
GPIO.setup(p2,GPIO.OUT)
GPIO.setup(p3,GPIO.IN)
GPIO.setup(p4,GPIO.IN)

####################################Capturing Image ##########################################################
def captureImage(initialName,timeInterval):
        camera.capture(initialName+'.jpg')
        #filePost(initialName+'.jpg',finalName) #This function is going to add the extension to finalName
        time.sleep(timeInterval)
'''The image being capturd here will be stored in the same folder as the code '''
def convVideo():
	#Basically the subprocess needs to be called here.
	command = "/usr/bin/sudo " #command is not right yet, need to be worked on.
    	import subprocess
    	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    	output = process.communicate()[0]
    	print output
def initialBlink():
	GPIO.output(p1,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(p1,GPIO.LOW)	
def finalBlink():
	GPIO.output(p2,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(p2,GPIO.LOW)
def startButton():
	return GPIO.input(p3)
def stopCapture():
	return GPIO.input(p4)
count = 0
while True:
	#Write the condition for starting image capture
        captureImage("image_stream"+str(count),0.25)
	print count
	count = count +1
	if count > 4000:
		break

''' Once the images have been captured, we can encode them using ffmpeg '''
