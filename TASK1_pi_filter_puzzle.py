import cv2
import math
img = cv2.imread("/Users/apple/Desktop/pi_image.png",0)
# for i in range (img.shape[0]): 
#     for j in range (img.shape[1]): 
#         print (img[i][j], end=" ")
#     print ("\n")
# print(img.shape[0],img.shape[1])
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j]==255:
            print ("(",i+1,",",j+1,")",end=" ")
print("\n")
a=[[251,219],[94,0]]
collage = cv2.imread("/Users/apple/Desktop/collage.png",0)
temp = cv2.imread("/Users/apple/Desktop/artwork_picasso.png",0)
# cv2.imshow("temp",temp)
for i in range(0,temp.shape[0],2):
    for j in range(0,temp.shape[1],2):
        temp[i][j]=temp[i][j]^a[0][0]
        temp[i][j+1]=temp[i][j+1]^a[0][1]
        temp[i+1][j]=temp[i+1][j]^a[1][0]
        temp[i+1][j+1]=temp[i+1][j+1]^a[1][1]
# cv2.imshow("template",temp)
resize = cv2.resize(temp,(100,100),interpolation=cv2.INTER_CUBIC)
# print(collage.shape[0],collage.shape[1],resize.shape[0],resize.shape[1])
cv2.imshow("resize",resize)
cv2.imshow('collage',collage)
for i in range(0,collage.shape[0],100):
    for j in range(0,collage.shape[1],100):
        t=1
        for k in range(i,i+100):
            for l in range(j,j+100):
                if collage[k][l]!=resize[k%100][l%100]: t=0
        if t==1:
            print("Required coordinates : ",i,j);break
        elif t==0: continue
print("\nHence, password of the file is ",math.floor(3.141596*(100+100)))

cv2.waitKey(0)


    

