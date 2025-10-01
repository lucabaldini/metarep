# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import importlib.metadata

from metarep import __version__, __name__ as __package_name__


# Get package metadata.
_meta = importlib.metadata.metadata(__package_name__)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = __package_name__
author = _meta['Author-email']
copyright = f'2025-%Y, {author}'
version = __version__
release = version

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
html_logo = '_static/logo_small.png'
html_favicon = '_static/favicon.ico'