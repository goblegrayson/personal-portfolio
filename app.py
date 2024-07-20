from pathlib import Path
import sys
import streamlit as st


# Utils
def load_markdown(file_name):
    file_path = Path(__file__).parent.joinpath('markdown', file_name)
    with open(file_path, 'r') as file:
        return file.read()


# App Config
st.set_page_config(page_title='Grayson Goble')
app_dir = str(Path(__file__).parent)
logo_path = str(Path(app_dir, 'media', 'logo.svg'))

# Sidebar
st.sidebar.markdown(load_markdown('sidebar.md'), unsafe_allow_html=True)

# Navigation text to white
st.markdown(load_markdown('css.md'), unsafe_allow_html=True)

# Navigation
pages = {
    'Who am I?': [
        st.Page(title='About Me', page='about.py'),
    ],
    'Black Scholes': [
        st.Page(title='Intuition', page=str(Path('black_scholes', 'page.py')))
    ]
}
pg = st.navigation(pages)
pg.run()


