#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, random, cv2
import matplotlib.pyplot as plt
import numpy as np

CAPTCHA_FOLDER = "captcha/"
PROCESSED_FOLDER = "processed/"


# In[ ]:


def preprocessing(from_filename, to_filename):
    if not os.path.isfile(from_filename):
        return
    img = cv2.imread(from_filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    crop = img[5:img.shape[0]-5, 5:img.shape[1]-5]
    dst = cv2.adaptiveThreshold(crop, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(to_filename, opening)
    return


# In[ ]:


i = 0

# ignore existing image
while True:
    i += 1
    filename = PROCESSED_FOLDER + str(i) + '.jpg'
    if not os.path.isfile(filename):
        i -= 1
        break

print("start to process image from index: " + str(i + 1))

while True:
    i += 1
    filename = CAPTCHA_FOLDER + str(i) + '.jpg'
    if not os.path.isfile(filename):
        break
    preprocessing(filename, PROCESSED_FOLDER + str(i) + '.jpg')
    print("i: ", i)

print("completed")


# In[ ]:




