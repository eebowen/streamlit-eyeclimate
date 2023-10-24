import streamlit as st
import pandas as pd
import numpy as np
from streamlit_image_comparison import image_comparison

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
    # width=width
)


# st.markdown("# Galaxy Cluster SMACS 0723")

# # render image-comparison
# image_comparison(
#     img1="https://www.webbcompare.com/img/hubble/deep_field_700.jpg",
#     img2="https://www.webbcompare.com/img/webb/deep_field_700.jpg",
#     label1="Hubble",
#     label2="Webb"
# )
