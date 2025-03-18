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

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Step 2: Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Step 3: Apply Canny Edge Detection to find edges in the frame
    edges = cv2.Canny(blurred, 50, 150)
    
    # Step 4: Display the edge-detected frame
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# release video from memory
cap.release()
cv2.destroyAllWindows()
