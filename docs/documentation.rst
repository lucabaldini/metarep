.. _documentation:

Documentation
=============

Imagine for a second if somebody handed you the |numpy| package with no documentation 😢.
Pretty daunting, eh? Bottomline: you should do a favor to your users (and to the
future version of yourself, six months from now) and ship good documentation with
your package. When it comes to tooling, nowadays this is simply a no brainer: all
Python projects out there use |Sphinx| to generate the documentation, Python itself
uses |Sphinx|, and so should you!

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
a series of ``.rst`` markup files, while the second is extracted from the docstrings
in the Python code. What you need is a Python configuration file such as the one
generating this page

.. literalinclude:: conf.py
   :language: python

and at least a master markup file ``index.rst``

.. literalinclude:: index.rst

.. note::

   Wow, did you see that? We just included an entire file from the repository
   `verbatim` into the documentation. This is what the
   `literalinclude <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude>`_ directive is for.


The most straightforward way to begin a new project is to use the quickstart
facility provided by Sphinx itself, which will generate a basic set of files

.. code-block:: shell

    cd docs
    sphinx-quickstart

and then proceed from there.


Compiling the documentation
---------------------------

All right, now I have a fully fledged ``docs`` folder with all the ingredients
for great documentation---what should I do with it?

Well, for one thing, if you did use ``sphinx-quickstart`` you will find in the
``docs`` folder a fully fledged ``Makefile`` (on Linux/Mac) or a ``make.bat`` (on Windows)
and the magic is simply

.. code-block:: shell

   cd docs
   make html

or

.. code-block:: shell

   cd docs
   make.bat html

depending on your platform. This will trigger the Sphinx build process and
generate the HTML documentation in the ``_build/html`` directory.

This is equivalent to running the following command

.. code-block:: shell

   cd docs
   sphinx-build -b html docs _build/html

and, in fact, you might want to wrap just that into a session of your
``noxfile.py`` if you happen (as you should) to use ``nox``, as described in
the section about :ref:`tasks`.

.. seealso::
   :ref:`tasks`.


Markup files and docstrings
---------------------------

As noted before, there are two main parts to software documentation: general, descriptive
text and technical descriptions of the interfaces.

For the first, you just create a bunch of .rst files in markdown format, include
them into the ``index.rst`` file, and you're good to go. Start from
`here <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`__
if you want to become proficient in reStructuredText (reST), the default plaintext
markup language used by |Sphinx|.

The interfaces, one the other hand, are customarily described in the code
source files in the form of doctrings. Having code and documentation living side by
side in the same file makes it easier for the developer to update the second when
the first is changed! In the context of |Sphinx|, docstrings get automatically
parsed and formatted via the
`autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc>`_
directive.

.. note::
   ``autodoc`` is part of the |Sphinx|, but it comes in the form of an `extensions`,
   and you do have to explicitly opt-in to use it. This typically entails to adding
   (at least) a line to your ``conf.py`` file

   .. code-block:: python

      extensions = [
         "sphinx.ext.autodoc",
      ]

Let's see how this plays out in practice. Take the only |Python| module we are
actually shipping with this repository

.. literalinclude:: ../src/metarep/utils.py
   :language: python

along with the markup file

.. literalinclude:: api.rst
   :language: rst

And look at the resulting API documentation in the :ref:`api` section. Cool,
isn't it?



Sphinx themes
-------------

With no offense to anybody, the default theme that |Sphinx| uses to generate HTML
documentation is not particularly inspiring. The website
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

Publishing the documentation
----------------------------

At this point you might be wondering: all right I have all this great stuff on
my laptop, and I managed to compile it, but where do I put the static html
output so that people can actually `see` it? Very good question.

This is one area where `GitHub Actions` come into play. To make a long story short,
go ahead and drop into the ``.github/workflows`` a file containing something along
the lines of

.. literalinclude:: ../.github/workflows/docs.yml
   :language: yaml

and you will get your glorious documentation recompiled and deployed on GitHub Pages
every time you push changes to the main branch, be that via a pull request or
directly (which, remember, you should not).

.. warning::
   In order for this to work as advertised you will have to enable GitHub Pages
   for your repository. That is: go to your repository "Settings" -> "Pages" and
   set the "Source" combo box to "GitHub Actions". That should do it.

.. seealso::
   :ref:`actions`.