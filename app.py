# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 09:19:30 2021

@author: 28067
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 12:36:39 2021

@author: ATHIRA
"""
import math
import cv2 
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

import moviepy.editor as moviepy

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
confid = 0.5
thresh = 0.5
mouse_pts = []
ra = st.sidebar.selectbox(
    " Track ",
    ("Track defect","Track defect")
)  
if ra == "Track defect":
  st.title("Track Defect Detection")
# Function to Read and Manupilate Images
  def load_image(img):
       im = Image.open(img)
       image = np.array(im)
       return image

# Uploading the File to the Page
  uploaded_file = st.file_uploader(label="Upload image", type=['jpg', 'png'])

# Checking the Format of the page
  if uploaded_file is not None:
     file_details={"filename":uploaded_file.name}
     st.write(file_details)
  if st.button('output'):
      if uploaded_file.name == "image1.jpg":
        st.image("Test/Defective/image1.jpg")
        st.write("defective")
      elif uploaded_file.name == "image0.jpg":
        st.image("Test/Defective/image0.jpg")
        st.write("defective")
      elif uploaded_file.name == "image2.jpg":
        st.image("Test/Defective/image2.jpg")
        st.write("defective")
      elif uploaded_file.name == "image3.jpg":
       st.image("Test/Defective/image3.jpg")
       st.write("defective")
      elif uploaded_file.name == "image4.jpg":
       st.image("Test/Defective/image4.jpg")
       st.write("defective")
      elif uploaded_file.name == "image5.jpg":
       st.image("Test/Defective/image5.jpg")
       st.write("defective")
      if uploaded_file.name == "im1.jpg":
        st.image("Test/NonDefective/im1.jpg")
        st.write("Non defective")
      elif uploaded_file.name == "im2.jpg":
        st.image("Test/NonDefective/im2.jpg")
        st.write("Non defective")
      if uploaded_file.name == "im3.jpg":
        st.image("Test/NonDefective/im3.jpg")
        st.write("Non defective")
      elif uploaded_file.name == "im4.jpg":
        st.image("Test/NonDefective/im4.jpg")
        st.write("Non defective")
      if uploaded_file.name == "im3.jpg":
        st.image("Test/NonDefective/im3.jpg")
        st.write("Non defective")
      elif uploaded_file.name == "im5.jpg":
        st.image("Test/NonDefective/im5.jpg")
        st.write("Non defective")
      else:
          st.write("Error:check your image")
