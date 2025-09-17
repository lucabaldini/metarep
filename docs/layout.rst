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
  several useful purposes, see `here <https://docs.python.org/3/tutorial/modules.html#packages>`_
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
`here <https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/>`_

.. seealso::
   :ref:`versioning`


Documentation
-------------


.. seealso::
   :ref:`documentation`


Unit tests
----------


.. seealso::
   :ref:`testing`



Miscellanea
-----------