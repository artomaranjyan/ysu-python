"""
Open the video vid1.mp4 and display it frame by frame in a window named vid1.
"""

import cv2 as cv

#takes either interger argumenets or a path to a video file (when the file already exists)
#we provide integers when we are using webcam or computer cams

capture = cv.VideoCapture('vid1.mp4')

#using a loop to read the video frame by frame

while True:
    frame_loaded, frame = capture.read() #returns the frames and a boolean indicating if it was successfully read
    
    #we will get an error at the end, cause when the video ends, openCV cannot find the frame
    #same happens when we give a wrong path to an image
    #cv.imshow('Video', frame) 
    
    
    #we use this to not get an error when the video ends
    #if frame is not None:
    if frame_loaded:
        cv.imshow('vid1', frame)
    else:
        print('empty frame')
        exit(1)
    
    #we don't want the video to display forever
    #when the letter 'd' is pressed, break out of the loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows() #distroying all windows since we don't need them anymore
    
cv.waitKey(0)