.. _layout:

Repository layout
=================

While in principle there is an infinite number of ways you can structure the
repository for a Python package, if you look around you will find that most repos
look remarkably similar to each other, the minimal structure resembling something
like

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

flat vs. src layout and the Python package authority.