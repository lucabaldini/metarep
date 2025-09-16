.. metarep documentation master file, created by
   sphinx-quickstart on Mon Sep  1 14:14:13 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

metarep documentation
=====================

This is an unusual repo. From the pure code standpoint it provides a single Python module
exposing exactly one function (calculating the square of a given number, by the way).

.. literalinclude:: ../src/metarep/utils.py

In the process, though, it touches upon many different points related to the
development and maintainance of a simple Python package, and can be taken as a
rough template and a starting point for new projects.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   layout
   license
   install
   versioning
   documentation
   linting
   testing
   actions
   tasks
   badges
   release_notes
