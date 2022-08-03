# Copyright (c) 2022 Josh Hung. All Rights Reserved.
#
# You can use the all methods I offer for free.
# You also can leave your opinions about my code,
# than we can have a discussion.
# If the methods I provide can help you,
# you can also take a look at other portfolios I made.
# Go visit https://github.com/appleasd1230.

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

def read_whihe_and_black_image(image: bytes) -> numpy.ndarray:
    """Read 1 (1-bit pixels, black and white, stored with one pixel per byte) by openCV.
       using PIL read image first,
       if image mode is '1', conver it to mode 'L',
       than opencv can read the mode 'L' bytes.
       modes :
       · 1 (1-bit pixels, black and white, stored with one pixel per byte)
       · L (8-bit pixels, black and white)
       · P (8-bit pixels, mapped to any other mode using a colour palette)
       · RGB (3x8-bit pixels, true colour)
       · RGBA (4x8-bit pixels, true colour with transparency mask)
       · CMYK (4x8-bit pixels, colour separation)
       · YCbCr (3x8-bit pixels, colour video format)
       · I (32-bit signed integer pixels)
       · F (32-bit floating point pixels)

       if byte from request
       image = request.files['file'].read()

       if byte from parameter like below
       image = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00...........'
    """
    from PIL import Image
    import io
    
    stream = io.BytesIO(image)
    pil_img = Image.open(stream)

    if pil_img.mode == '1':
        pil_img.convert('L')
        buf = io.BytesIO()
        pil_img.save(buf, format='JPEG')
        image = buf.getvalue()

    stream.close()

    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    ## if you also want to conver it to gray
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img
  
def read_image_with_chinese_filename(image_path: str) -> numpy.ndarray:
    """Read image which filename contain chinese."""
    img = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), -1)
    
    return img
  
def auto_convert_best_size(img: bytes, width: str, height: str, inter = cv2.INTER_AREA) -> numpy.ndarray:
    """Auto resize image with the best width and height which not reduce too much DPI.
       Give width or height to auto calculate the best other widht or heigth.
       If give both the width and height, it will return the size you decide.
       if not give any, return the origin image.
    """
    if width == '':
        width = None
    if height == '':
        height = None

    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is not None and height is not None:
        resized = cv2.resize(image, (width, height), interpolation = inter)
        return resized    

    if width is None:
        r = int(height) / float(h)
        dim = (int(w * r), int(height))
    else:
        r = int(width) / float(w)
        dim = (int(width), int(h * r))

    img = cv2.resize(image, dim, interpolation = inter)
    return img
