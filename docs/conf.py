# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

# Import the version string
from metarep._version import __version__

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'metarep'
copyright = '2025, Luca Baldini'
author = 'Luca Baldini'
version = __version__

# This will be included at the beginning of each .rst file.
rst_prolog = f"""
.. |Python| replace:: `Python <https://www.python.org/>`__
.. |Sphinx| replace:: `Sphinx <https://www.sphinx-doc.org/en/master/>`__
.. |numpy| replace:: `NumPy <https://numpy.org/>`__
.. |GitHub| replace:: `GitHub <https://github.com/>`__
"""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

todo_include_todos = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'undoc-members': True,
    'private-members': True
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_permalinks_icon = '<span>#</span>'
pygments_style = 'default'
pygments_dark_style = 'default'
html_theme_options = {
    'awesome_external_links': True,
}
html_static_path = ['_static']
