import pytesseract
pytesseract.pytesseract.tesseract_cmd = (
    r'/usr/bin/tesseract'
)
from PIL import Image
import easyocr
import cv2
import numpy as np
import matplotlib.pyplot as plt
read = easyocr.Reader(['en'])
from google.colab.patches import cv2_imshow
#storing the video in cap
cap = cv2.VideoCapture('/content/Introduction to data structures lecture.mp4')
l = []
while cap.isOpened():
  try:
    _, frame = cap.read()
    im = Image.fromarray(frame)
    im.save('frame.jpg')
    #img = Image.open('/content/frame.jpg')
    img = cv2.imread("/content/frame.jpg")
    #converting BGR image to gray_scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #find contours over the textual data according to the threshold
    img_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    img_contours = sorted(img_contours, key=cv2.contourArea)
    for i in img_contours:
      if cv2.contourArea(i) > 180:
        break
    #draw the contours on the image(frame)
    cv2.drawContours(img, img_contours, -1, (0, 100, 0))

    data=pytesseract.image_to_string(img)
    #rextract the text from the contours and convertto string
    data = data.replace('\n','')
  except:
    break
   
print(data)
cap.release()
cv2.destroyAllWindows()
#displays image
imgplot = plt.imshow(im)
