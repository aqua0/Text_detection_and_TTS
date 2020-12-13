# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:25:19 2020

@author: user
"""
#pip install pyteserract
import cv2
import pytesseract
from gtts import gTTS
import os

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
#start your webcam

#cam = cv2.VideoCapture(0)

img = cv2.imread("ocr.png")
#while(True):
#ret,frame = cam.read()#reading frame by frame
color = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(color))
print(pytesseract.image_to_boxes(color))

#character detection
#himg,wimg,_ = color.shape
#boxes = pytesseract.image_to_boxes(color)
#
#for i in boxes.splitlines():
#    i = i.split(' ')
#    print(i)
#    x,y,w,h = int(i[1]),int(i[2]),int(i[3]),int(i[4])
#    cv2.rectangle(color,(x,himg-y),(w,himg-h),(0,0,255),2)
#    cv2.putText(color,i[0],(x,himg-y+100),cv2.FONT_HERSHEY_COMPLEX,1,(50,255,50),2)



#detecting words
    
himg,wimg,_ = color.shape
boxes = pytesseract.image_to_data(color)
#print(boxes)
text=[]
for a,i in enumerate(boxes.splitlines()):
    if a!= 0:
        i = i.split()
        print(i)
        if len(i) == 12:
            x,y,w,h = int(i[6]),int(i[7]),int(i[8]),int(i[9])
            cv2.rectangle(color,(x,y),(w+x,h+y),(0,0,255),2)
            cv2.putText(color,i[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,255,50),2)
            text.append(i[11])

text1 =" ".join(text)
#print(text1)

language = 'en'
output = gTTS(text=text1, lang=language ,slow=False)

output.save("audio.mp3")

os.system("start audio.mp3")

cv2.imshow("Camera",color)
cv2.waitKey(0)






#breaking the loop
#if cv2.waitKey(1) & 0xFF == ord('q'):
#    break
#cam.release()    
#cv2.destroyAllWindows()