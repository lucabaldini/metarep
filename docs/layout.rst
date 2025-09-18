.. _layout:

Repository layout
=================

While in principle there is an infinite number of ways you can structure the
repository for a Python package, if you look around you will find that most repos
look remarkably similar to each other, the minimal structure resembling something
like (mileage may vary):

.. code-block:: text

   pkgname/
   ├── .github/
   │  └── workflows/
   │     ├── ci.yml
   |     └── docs.yml
   ├── docs/
   │  └── conf.py
   │  └── index.rst
   ├── src/
   │  └── pkgname/
   │     ├── __init__.py
   │     ├── _version.py
   │     └── pkgmodule.py
   └── tests/
      └── test_pkgmodule.py
   ├── LICENSE
   ├── README.md
   ├── noxfile.py
   └── pyproject.toml

Now, this is a lot of files---so may that the thing might look daunting at a first
glance---but in fact it's not too bad. In this section we shall quickly go through
the organization of the files and clarify the rationale beyond this standard organizations.


Source code
-----------

It goes without saying, the source code (i.e., the actual Python modules) is
typically the most important part of your repository. (Ironically, this is not the case
for this repo.) At the very minimum the source code includes

* a ``__init__.py``, a special Python file that is used to mark a directory as a
  Python package (in the simplest case the the file can be empty, but it can serve
  several useful purposes, see
  `here <https://docs.python.org/3/tutorial/modules.html#packages>`__
  for more details);
* all the Python modules that your package ships---this should be self-explaining and,
  quite possibly, is the only thing you ever cared about before reading this;
* depending on how exactly you do versioning, you might have a ``_version.py`` file
  (the precise name might differ)---more on this at the page about :ref:`versioning`.

In terms of `where` the source code actually lives, the basic answer is: isolated in a
single folder with the same name as the package. This folder can live at the top level
in the repository structure, or further embedded in a ``src`` folder, which is sometimes
referred as `flat vs. src layout`. To make a long story short, the Python package authority
recommends the latter (src layout) and this is what we use here. You find (a lot of)
additional information
`here <https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/>`__.

.. seealso::
   :ref:`versioning`.


Documentation
-------------

All the stuff related to documentation lives in the ``docs`` folder. We shall look in
details into how you go about documenting a Python package in the :ref:`documentation`
section, but we anticipate the ``docs`` folder will contain at the very least a
|Sphinx| configuration file called ``conf.py``, a master markup file ``index.rst`` and,
very possibly, more .rst files.

.. seealso::
   :ref:`documentation`.


Unit tests
----------

Not surprisingly, the ``tests`` folder contains all the unit tests. We shell cover this in
the section about :ref:`testing`, but we anticipate that, ideally, you will have one test
file for each |Python| module in the package.

.. seealso::
   :ref:`testing`.


Miscellanea
-----------

You will notice that, past ``src``, ``docs`` and ``tests``, there's plenty of stuff
left; let's quickly go through them:

* the ``pyproject.toml`` file is by far the most important---it has to do primarily
  (but not only) with packaging, and we shall see this is all the excruciating details
  in the section about :ref:`install`;
* the ``noxfile.py`` file is used for automating recurrent development tasks while
  operating on a working copy of the repository, which we shall get back to in the
  section about :ref:`tasks`;
* the ``README.md`` file is what appears in the default landing page on github, and
  it is in many senses the face of your project---the very first thing that people
  will see;
* the ``LICENSE`` file should be self-explanatory, but you should not underestimate
  its importance---more on this in :ref:`license` section;
* finally the ``.github/workflows`` folder contains the GitHub Actions workflows for
  automating tasks such as testing and deployment---see :ref:`actions`.

It goes without saying, there's plenty of additional files and folders that you
might see in real-life project (e.g., ``CODE_OF_CONDUCT.md``, ``CONTRIBUTING.md``,
``CITATION.cff``) but let's start from the simplest possible thing and move from
there.

  .. seealso::
   :ref:`install`, :ref:`tasks`, :ref:`license`, :ref:`actions`.
