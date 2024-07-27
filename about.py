"""
about.py
A streamlit page
"""
from pathlib import Path
import streamlit as st
from utils import load_markdown

# Content
st.markdown(body=load_markdown('aboutme'), unsafe_allow_html=True)