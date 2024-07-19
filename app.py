from pathlib import Path
import sys
import streamlit as st

# App Config
st.set_page_config(page_title='Grayson Goble')
app_dir = str(Path(__file__).parent)
logo_path = str(Path(app_dir, 'media', 'logo.svg'))

# Sidebar
file_path = Path('markdown', 'sidebar.md')
with open(file_path, 'r') as file:
    text = file.read()
st.sidebar.markdown(text)

# Navigation text to white
st.markdown("""
<style>
    [data-testid=stSidebarNav] * {
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
pages = {
    'Who am I?': [
        st.Page(title='About Me', page='about.py'),
    ],
    'Black Scholes': [
        st.Page(title='Visualization', page=str(Path('black_scholes', 'page.py')))
    ]
}
pg = st.navigation(pages)
pg.run()


