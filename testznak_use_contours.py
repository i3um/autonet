import cv2 as cv


cap = cv.VideoCapture(0)
stop = cv.imread("stop.png")
stop = cv.inRange(stop, (104, 83, 85), (255,255,255))
stop = cv.resize(stop, (64,64))
straight = cv.imread('straight1.png')
straight = cv.resize(straight,(64,64))
straight = cv.inRange(straight,(104, 83, 85), (255,255,255))


while (True):
    ret, frame = cap.read()
    #cv.imshow("Frame", frame)
    framecopy = frame.copy()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv = cv.blur(hsv,(5,5))
    mask = cv.inRange(hsv,(104, 83, 85),(255,255,255))
    #cv.imshow("Mask", mask)
    #борьба с шумами
    mask = cv.erode(mask,None,iterations = 2)
    mask = cv.dilate(mask,None,iterations = 4)
    cv.imshow("Mask2", mask)
    
    
    contours, _ = cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    if contours:
        contours = sorted(contours, key = cv.contourArea, reverse = True) 
        cv.drawContours(frame, contours, -1,(255,0,255),3)
    
        (x,y,w,h) = cv.boundingRect(contours[0])
        cv.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        cv.imshow("Contours", frame)
        roImg = framecopy[y:y+h, x:x+w]
        cv.imshow("Detect", roImg)
        roImg = cv.resize(roImg, (64,64))
        roImg = cv.inRange(hsv,(104, 83, 85),(255,255,255))
        cv.imshow("resized", roImg)
        
        stopv = 0
        straightv = 0
        for i in range(64):
            for t in range(64):
                if roImg[i][t] == stop[i][t]:
                    stopv += 1
                if roImg[i][t] == straight[i][t]:
                    straightv += 1
                
        
        print(stopv, straightv)
        
        
        
        
    
    
    #cv.drawContours(frame,[contours],-1,(255,0,255),3)
       # cv.imshow("Contours", frame)
       # (x,y,w,h) = cv.boundingRect(contours[0])
        #cv.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        #cv.imshow("Rect", frame)
    
    
    #roImg = frame[y:y+h, x:x+w]
    #cv.imshow("utt", roImg)
    
    
    
        if cv.waitKey(1) == ord("q"):
            break
    
cv.destroyAllWindows()
cap.release()
