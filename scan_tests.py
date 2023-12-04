import cv2

img = cv2.imread('Foto_2023-12-01_141717.jpg')
original = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
thresh = cv2.threshold(blurred, 230, 255, cv2.THRESH_BINARY_INV)[1]

contours = cv2. findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours [1]

img_number = 0
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 2)
    ROI = original[y:y+h, x: x+w]
    cv2.imwrite("ROI_{}.jpg". format(img_number), ROI)
    img_number += 1

cv2.imshow('thresh', thresh)
cv2.imshow('image', img)
cv2.waitKey(0)