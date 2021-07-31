#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import requests
import shutil
import random

CAPTCHA_DIR = "captcha/"
num = 1000

url = "https://1922.gov.tw/vas/"
sess = requests.session()
result = sess.get(url)


# In[ ]:


captcha_url = "https://1922.gov.tw/vas/validateCodeService.do?"

i = 1

#ignore existing image
while True:
    i += 1
    filename = CAPTCHA_DIR + str(i) + '.jpg'
    if not os.path.isfile(filename):
        break

while i <= num:
    r = sess.get(captcha_url + str(random.random()), stream=True)
    path = CAPTCHA_DIR + str(i) + ".jpg"
    with open(path, 'wb') as handler:
        handler.write(r.content)
    print(i)
    i += 1

print("completed")


# In[ ]:




