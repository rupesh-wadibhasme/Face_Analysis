import os,sys
from image_emotion_gender import *
arg= (sys.argv)
try:
	inp_path=sys.argv[1]
	out_path=sys.argv[2]


	inp_path=(arg[1].strip('[]').split(','))

	out_path=(arg[2].strip('[]').split(','))
	for inpt,output in zip(inp_path,out_path):
		race_emotion(inpt,output)
except:
	print ('Incorrect Input ')
	print ('check for valid input path !!! Allowed extentions are jpg, png, jpeg')
	


        

