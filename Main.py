import cv2
import numpy as np
 
def canny(img):
   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   blur=cv2.GaussianBlur(gray, (5.5), 0)
   canny=cv2.Canny(blur,50,150)
   return canny 

def region_of_interest(canny):
    height,width=canny.shape
    mask=np.zeros_like(canny)
    triangle = np.array([
        [(200, height), (800, 350), (1200, height)]
    ], np.int32)
    cv2.fillPoly(mask, [triangle], 255)  # Fill the triangular area with white
    masked_image = cv2.bitwise_and(canny, mask)  # Keep only edges in the ROI
    return masked_image

def houghLines(cropped_canny):
    return cv2.HoughLinesP(cropped_canny, 2, np.pi/180, 100, 
                           np.array([]), minLineLength=40, maxLineGap=5)

def display_lines(img, lines):
    line_image = np.zeros_like(img)

    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 10)  

    return line_image



# capture video 
cap=cv2.VideoCapture("test1.mp4")
# iterate through frames 
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    canny_image = canny(frame)  
    cropped_canny = region_of_interest(canny_image)  

    lines = houghLines(cropped_canny)  
    line_image = display_lines(frame, lines)  
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)  

    cv2.imshow("Lane Detection", combo_image)
# release video from memory
cap.release()
cv2.destroyAllWindows()
