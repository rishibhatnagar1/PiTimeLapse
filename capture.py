''' The code has been written by Rishi Gaurav Bhatnagar and Rahul Thota to capture a time lapse video by merging various images over a period of time. '''
import picamera
import time
'''Initialize camera '''
camera = picamera.PiCamera()
camera.resolution =(640,480)

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
def finalBlink():
def startButton():
def stopCapture():
count = 0
while True:
        captureImage("image_stream"+str(count),0.25)
	print count
	count = count +1
	if count > 4000:
		break

''' Once the images have been captured, we can encode them using ffmpeg '''
