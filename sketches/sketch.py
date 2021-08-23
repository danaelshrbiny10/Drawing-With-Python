import cv2

image = cv2.imread("sketches/img/Messi-PSG.jpg")
image1 = cv2.imread("sketches/img/mbappe.jpg")
image2 = cv2.imread("sketches/img/salah.jpg")
image3 = cv2.imread("sketches/img/msn.jpg")
image4 = cv2.imread("sketches/img/suarez.jpg")



grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
grey_img1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
grey_img2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
grey_img3 = cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY)
grey_img4 = cv2.cvtColor(image4,cv2.COLOR_BGR2GRAY)



invert = cv2.bitwise_not(grey_img)
invert1 = cv2.bitwise_not(grey_img1)
invert2 = cv2.bitwise_not(grey_img2)
invert3 = cv2.bitwise_not(grey_img3)
invert4 = cv2.bitwise_not(grey_img4)




blur = cv2.GaussianBlur(invert,(21,21),0)
blur1 = cv2.GaussianBlur(invert1,(21,21),0)
blur2 = cv2.GaussianBlur(invert2,(21,21),0)
blur3 = cv2.GaussianBlur(invert3,(21,21),0)
blur4 = cv2.GaussianBlur(invert4,(21,21),0)




invertdblur = cv2.bitwise_not(blur)
invertdblur1 = cv2.bitwise_not(blur1)
invertdblur2 = cv2.bitwise_not(blur2)
invertdblur3 = cv2.bitwise_not(blur3)
invertdblur4 = cv2.bitwise_not(blur4)




sketch = cv2.divide(grey_img, invertdblur, scale=256.0)
sketch1 = cv2.divide(grey_img1, invertdblur1, scale=256.0)
sketch2 = cv2.divide(grey_img2, invertdblur2, scale=256.0)
sketch3 = cv2.divide(grey_img3, invertdblur3, scale=256.0)
sketch4 = cv2.divide(grey_img4, invertdblur4, scale=256.0)




cv2.imwrite("sketches/sketch_result/Messi.png", sketch)
cv2.imwrite("sketches/sketch_result/mbappe.png", sketch1)
cv2.imwrite("sketches/sketch_result/salah.png", sketch2)
cv2.imwrite("sketches/sketch_result/msn.png", sketch3)
cv2.imwrite("sketches/sketch_result/suarez.png", sketch4)
