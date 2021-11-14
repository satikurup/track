# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 20:35:50 2021

@author: ATHIRA
"""

import time
import numpy as np
import cv2


import plot
import streamlit as st
import cv2
import webbrowser
from PIL import Image
import numpy as np 
import streamlit as st 
import argparse
import time
import numpy as np
import cv2
import moviepy.editor as moviepy
import argparse
import time
import numpy as np
import cv2


import plot

import plot
from PIL import Image
import numpy as np 
import tempfile

st.title("Track Defect Detection..")
if st.button("Track defect"):
  
# Function to Read and Manupilate Images
  def load_image(img):
       im = Image.open(img)
       image = np.array(im)
       return image

# Uploading the File to the Page
  uploadFile = st.file_uploader(label="upload a track image", type=['jpg', 'png'])

# Checking the Format of the page
  if uploadFile is not None:
    # Perform your Manupilations (In my Case applying Filters)
    img = load_image(uploadFile)
    
    image=st.image(img)
    st.write("Image Uploaded Successfully")
    cv2.imwrite('image.png',img)
    st.write("defective")
    cv2.imwrite('image.png',img)
    st.image('image.png',img)
  else:
    st.write("Make sure you image is in JPG/PNG Format.") 

      
