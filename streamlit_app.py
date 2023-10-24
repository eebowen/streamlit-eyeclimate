import streamlit as st
import pandas as pd
import numpy as np
from streamlit_image_comparison import image_comparison
import streamlit as st
from streamlit_juxtapose import juxtapose

from PIL import Image
import requests
import pathlib
'''
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# st.title("James Webb vs Hubble Telescope Pictures")

# st.markdown("# Southern Nebula")
# width = st.screen.width

# render image-comparison
image_comparison(
    img1="no_mask.png",
    img2="with_mask.png",
    label1="",
    label2="",
    starting_position=35
    # width=width
)

image_comparison(
    img1="slider2a.png",
    img2="slider2b.png",
    label1="",
    label2="",
    # starting_position=35
    # width=width
)
'''



STREAMLIT_STATIC_PATH = (
    pathlib.Path(st.__path__[0]) / "static"
)  # at venv/lib/python3.9/site-packages/streamlit/static

IMG1 = "img1.png"
IMG2 = "img2.png"

DEFAULT_IMG1_URL = (
    "https://juxtapose.knightlab.com/static/img/Sochi_11April2005.jpg"
)
DEFAULT_IMG2_URL = (
    "https://juxtapose.knightlab.com/static/img/Sochi_22Nov2013.jpg"
)

def fetch_img_from_url(url: str) -> Image:
    img = Image.open(requests.get(url, stream=True).raw)
    return img

form = st.form(key="Image comparison")
img1_url = DEFAULT_IMG1_URL
img2_url = DEFAULT_IMG2_URL
# img1_url = form.text_input("Image one url", value=DEFAULT_IMG1_URL)
img1 = fetch_img_from_url(img1_url)
img1.save(STREAMLIT_STATIC_PATH / IMG1)

# img2_url = form.text_input("Image two url", value=DEFAULT_IMG2_URL)
img2 = fetch_img_from_url(img2_url)
img2.save(STREAMLIT_STATIC_PATH / IMG2)
juxtapose(IMG1, IMG2)