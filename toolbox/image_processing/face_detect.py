""" Experiment with face detection and image filtering using OpenCV """
"""By Annabel Consilvio"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/Users/annabelconsilvio/anaconda/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
kernel = np.ones((41,41),'uint8')  #blurs faceframe

while(True):
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	for (x,y,w,h) in faces:
	    frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
	    #create tophat
	    cv2.rectangle(frame,(x,y),(x+w,y), (0,0,0), thickness=10, lineType=8, shift=0)
	    cv2.rectangle(frame,(x+40,y-180),(x+w-40,y), (0,0,0), thickness=-80, lineType=8, shift=0)
	    #create eyes
	    cv2.circle(frame, (x+60, y+60), 15, (255,0,0), thickness=-51, lineType=8, shift=0)
	    cv2.circle(frame, (x+w-60, y+60), 15, (255,0,0), thickness=-51, lineType=8, shift=0)
	    cv2.circle(frame, (x+60, y+65), 5, (0,0,0), thickness=-51, lineType=8, shift=0)
	    cv2.circle(frame, (x+w-60, y+65), 5, (0,0,0), thickness=-51, lineType=8, shift=0)
	    #create pipe
	    cv2.line(frame,(x/2+((x+w)/2)+20,y+160),(x/2+((x+w)/2)+100,y+230), (0,0,0), thickness=10, lineType=8, shift=0)
	    cv2.circle(frame, (x/2+((x+w)/2)+100,y+230), 20, (0,0,0), thickness=-51, lineType=8, shift=0)


	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

