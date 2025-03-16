import cv2

# capture video 
cap=cv2.VideoCapture("test1.mp4")
# iterate through frames 
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    # display window
    cv2.imshow("Video",frame)
    # wait for one millisecond
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# release video from memory
cap.release()
cv2.destroyAllWindows()
