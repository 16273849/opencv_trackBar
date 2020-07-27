import cv2

maxScaleUp = 100
scaleFactor = 1
scaleType = 0
maxType = 1

windowName = "Resize Image"
trackbarValue = "Scale"
trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"

# load an image
image = cv2.imread("truth.png")

# Create a window to display results
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)


#######################################################################

# Callback functions
def scaleImage(*args):
    global scaleFactor
    global scaleType
    
    # Get the scale factor from the trackbar 
    if (scaleType == 0):
        scaleFactor = 1 + args[0]/100.0
    else:
        scaleFactor = 1 - args[0]/100.0
    
    # Perform check if scaleFactor is zero
    if scaleFactor == 0:
        scaleFactor = 1
    
    # Resize the image
    scaledImage = cv2.resize(image, None, fx=scaleFactor,\
            fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    
    #font = cv2.FONT_HERSHEY_COMPLEX
    #cv2.putText(scaledImage, str(scaleFactor), (50,100), font, 2, (0,200,0) )
    cv2.imshow(windowName, scaledImage)

# Callback functions
def scaleTypeImage(*args):
    global scaleType
    global scaleFactor
    scaleType = args[0]
    scaleIm = 1 + scaleFactor/100.0
    if scaleFactor ==0:
        scaleFactor = 1
    scaledImage = cv2.resize(image, None, fx=scaleFactor,\
            fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)

###########################################################################

cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, scaleImage)
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, scaleTypeImage)



cv2.imshow(windowName, image)
c = cv2.waitKey(0)

cv2.destroyAllWindows()