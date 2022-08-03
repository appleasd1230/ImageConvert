# Copyright (c) 2022 Josh Hung. All Rights Reserved.
#
# You can use the all methods I offer for free.
# You also can leave your options about my code,
# we can have a discussion.
# If the methods I provide can help you,
# you can also take a look at other portfolios I made.
# Visit https://github.com/appleasd1230.

import cv2
import numpy as np

def read_bytes_image(image: bytes) -> numpy.ndarray:
  """Read image as byte type, most use in webAPI.
  
     if byte from request
     image = request.files['file'].read()

     if byte from parameter like below
     image = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00...........'
  """
  
  # read bytes by using openCV
  img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
  ## if you also want to conver it to gray
  # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  return img


