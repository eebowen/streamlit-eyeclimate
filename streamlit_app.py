import streamlit as st
import pandas as pd
import numpy as np
from streamlit_image_comparison import image_comparison
import streamlit as st
from streamlit_juxtapose import juxtapose

from PIL import Image
import requests
import pathlib

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




# STREAMLIT_STATIC_PATH = (
#     pathlib.Path(st.__path__[0]) / "static"
# )  # at venv/lib/python3.9/site-packages/streamlit/static

# IMG1 = "slider2a.png"
# IMG2 = "slider2b.png"

# juxtapose(IMG1, IMG2)