"""
app.py
A streamlit app containing my personal portfolio
"""

from pathlib import Path
import streamlit as st
from utils import load_markdown

# App Config
app_dir = str(Path(__file__).parent)
logo_path = str(Path(app_dir, 'media', 'logo.svg'))

# Sidebar
# st.sidebar.markdown(load_markdown('sidebar'), unsafe_allow_html=True)
st.sidebar.markdown(load_markdown('aboutme'), unsafe_allow_html=True)

# Navigation text to white
st.markdown(load_markdown('css'), unsafe_allow_html=True)

# Navigation
pages = {
    'Who am I?': [
        st.Page(title='About Me', page='about.py'),
    ],
    'Aerospace Modeling, Simulation, and Control': [
        st.Page(title='SLAM: A 6-DOF Simulation', url_path='slam', page=str(Path('SLAM', 'page.py')))
    ],
    'Quantitative Finance': [
        st.Page(title='Black-Scholes Option Pricing Model', url_path='black-scholes', page=str(Path('black_scholes', 'page.py'))),
        st.Page(title='Black-Derman-Toy Interest Rate Model', url_path='bdt', page=str(Path('bdt', 'page.py'))),
        st.Page(title='Dirty Crypto Trend', url_path='dirty-crypto-trend', page=str(Path('dirty-crypto-trend', 'page.py')))
    ],

}
pg = st.navigation(pages)
pg.run()


