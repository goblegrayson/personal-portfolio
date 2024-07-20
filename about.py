from pathlib import Path
import streamlit as st


def load_markdown(file_name):
    file_path = Path(__file__).parent.joinpath('markdown', file_name)
    with open(file_path, 'r') as file:
        return file.read()


st.markdown(body=load_markdown('aboutme.md'), unsafe_allow_html=True)