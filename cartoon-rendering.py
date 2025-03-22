import cv2

img = cv2.imread("test10.jpg")  
img = cv2.resize(img, (600, 600))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray= cv2.medianBlur(gray, 3)
edges = cv2.adaptiveThreshold(gray, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, blockSize=9, C=9)
color = cv2.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=300)


cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Cartoon Image", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
