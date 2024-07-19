from pathlib import Path
import streamlit as st

# Read file
file_name = 'aboutme.md'
file_path = Path('markdown', file_name)
with open(file_path, 'r') as file:
    text = file.read()

# Now print it
st.markdown(body=text)