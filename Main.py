import cv2


cap=cv2.VideoCapture("test1.mp4")

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break

    cv2.imshow("Video",frame)
    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blurred=cv2.GaussianBlur(gray, (5, 5), 0)
    
    edges=cv2.Canny(blurred,50,150)
    cv2.imshow("edges", edges)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):     
        break

cap.release()
cv2.destroyAllWindows()
