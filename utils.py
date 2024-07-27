"""
utils.py
A module containing a few project utils
"""
from pathlib import Path


def load_markdown(file_name):
    file_path = Path(__file__).parent.joinpath('markdown', file_name + '.md')
    with open(file_path, 'r') as file:
        return file.read()

