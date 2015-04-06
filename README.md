# PiTimeLapse

This is an attempt to create a handy and cheap device that could create timelapse videos and much more. The Pi clicks a series of images which is then encoded using ffmpeg. 

For now, you will need to execute both the commands separetly, but in the next step, both of these will be automated.

ffmpeg -f image2 -i image_stream%d.jpg -vcodec mpeg4 -b 2000k outvideo2.avi

image_stream001.jpg is the typical input image name
2000k refers to the bit rate for compression (higher this number, better the output resolution)
