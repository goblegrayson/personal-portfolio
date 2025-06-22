"""
page.py
A streamlit page
"""
from pathlib import Path
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
import black_scholes.model as model


# Utils
def load_markdown(file_name):
    file_path = Path(__file__).parent.joinpath('markdown', file_name + '.md')
    with open(file_path, 'r') as file:
        return file.read()


# Page Setup
st.title(':green[Dirty Trend in Crypto Markets]')
st.markdown(load_markdown('intro'), unsafe_allow_html=True)
st.image(Path(__file__).parent.joinpath('markdown', 'Performance1.png').__str__())
st.markdown(load_markdown('prelim-perf'), unsafe_allow_html=True)

