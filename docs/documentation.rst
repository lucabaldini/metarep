.. _documentation:

Writing documentation
=====================

Nowadays this is a no brainer: all Python projects out there use
`Sphinx <https://www.sphinx-doc.org/en/master/>`_ to generate the documentation,
Python itself uses Sphinx, and so should you!

When you think about documenting a software project, there are actually to equally
important parts to it, namely:

* descriptive text explaining the purpose and usage of the project (this might
  include, among other things, a user guide, examples, tutorials and so on and
  so forth);
* technical documentation (sometimes referred to as Advanced Programming Interfaces,
  or APIs), describing, e.g., the inner workings of the classes and functions that
  your package makes available (this might include, among other things, function
  signatures and return values).

Just to put things in context, the reference page for the
`optimize <https://docs.scipy.org/doc/scipy/reference/optimize.html>`_ module in
SciPy (or this very page that you are reading right now, for what it's worth) is
a good example of the first, while the documentation of the
`curve_fit <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html>`_
function belongs to the second category.

Sphinx handles both things equally well---the first is expressed in the form of
a series of ``.rst`` markup files, while the second can be easily extracted from
the docstrings in the Python code. What you need is a Python configuration
file such as the one generating this page

.. literalinclude:: conf.py
   :language: python

.. note::

   Wow, did you see that? We just included an entire file from the repository
   `verbatim` into the documentation. This is what the
   `literalinclude <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude>`_ directive is for.

Sphinx themes
-------------

`sphinx-themes.org <https://sphinx-themes.org/>`_ provides an extensive collection
of themes for Sphinx documentation. I have no doubt that there are useful places
out there, but I recommend starting from there.

.. warning::

   Using a custom theme is done by setting the ``html_theme`` variable in your
   Sphinx configuration file (``conf.py``), e.g.,

   .. code-block:: Python

      html_theme = 'sphinxawesome_theme'

   `and` making sure that you have the theme installed in your environment
   (usually via ``pip``). The most robust way to achieve the latter is to list
   the proper Python package among the optional dependencies in your
   ``pyproject.toml`` file

   .. code-block::

      [project.optional-dependencies]
      docs = [
         "sphinx",
         "sphinxawesome-theme",
        ]


    If you change theme, you will have to tweak both files!

github pages
------------

Settings -> Pages

Source: GitHub Actions