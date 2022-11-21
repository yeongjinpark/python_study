import cv2

img1=cv2.imread('lena.bmp')

print(img1.shape)

cv2.imshow('image color',img1)

img2=cv2.imread('lena.bmp',0)

p=cv2.waitKey(5000)
print('pressed key: ',p)

cv2.imshow('image gray',img2)

cv2.waitKey(0)
cv2.destroyWindow('image gray')
cv2.waitKey(0)
cv2.destroyyAllWindows()
