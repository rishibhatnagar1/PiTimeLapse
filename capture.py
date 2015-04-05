''' pip install picamera requests time '''
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
count = 0
while True:
        captureImage("image_stream"+str(count),0.25)
	print count
	count = count +1
	if count > 4000:
		break

