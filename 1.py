import cv2
img = cv2.imread('ehidna.jpg')
size1 = cv2.resize(img,(600,1000))
cv2.imshow('img',size1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
size = cv2.resize(gray,(600,1000))
cv2.imshow('gray',size)
border = cv2.Canny(size1,50,150,apertureSize=3)
cv2.imshow('canny',border)
rotate = cv2.rotate(border, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('rotate',rotate)
blur = cv2.GaussianBlur(size,(15,15),0)
cv2.imshow('blur',blur)



cv2.waitKey(0)
cv2.destroyAllWindows()
