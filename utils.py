"""
utils.py
A module containing a few project utils
"""
from pathlib import Path


def load_markdown(file_name):
    file_path = get_relative_path(f'markdown/{file_name}.md')
    with open(file_path, 'r') as file:
        return file.read()


def get_relative_path(file_name):
    return Path(__file__).parent.joinpath(*file_name.split('/'))
