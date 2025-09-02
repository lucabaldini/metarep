.. _versioning:

Versioning
==========

Whenever a problem occurs---whether you ara filing a bug  report on a third-party
software or processing a report on your own program---the first thing that you need
to know is `which version` of the softare we are talking about.

It is a widely used convention for Python modules to export a ``__version__`` attribute
to specify the version of a given package. You can try it for yourself on any
third-party Python libray you happen to have installed on your machine, e.g.

.. code-block::

    lbaldini@nblbaldini:~$ python
    Python 3.13.7 (main, Aug 14 2025, 00:00:00) ...
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import numpy as np
    >>> np.__version__
    '2.3.2'
    >>>

Cool. I have ``numpy`` 2.3.2 installed.


A simple workflow
-----------------

As you might imagine, keeping track of the version of your software boils down to
having a `version string` hard-coded somewhere in your codebase. This can actually
get trickier than it might seem at a first glance, as the version number is needed
in several different places for slightly different reasons (tags are managed by
git in the first place, but presumably you need ``__version__`` to be defined in
some Python module so that you can expose it; your ``pyproject.toml`` needs to
be version-aware; and you might want to spell out which version the online
documentation refers to---perhaps in the release notes).

Now: whatever strategy you resort to, you need to make sure that the information you
disseminate in the wild is self-consistent. One dead-simple line of action might
be:

* keep the ``__version__`` attribute into a ``_version.py`` file;
* have a (Python) script tagging your package `and` updating ``_version.py``
  whenever you want to make a release;
* have ``pyproject.toml`` read the version from ``_version.py``;
* expose the ``__version__`` attribute in your package's ``__init__.py`` file.

The  ``pyproject.toml`` magic is easily done via something along the lines of

.. code-block::

    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"

    [project]
    dynamic = ["version"]

    [tool.hatch.version]
    path = "src/metarep/_version.py"

And in the top-level ``__init__.py`` file of your package you might be tempted
to simply write

.. code-block:: Python

    from ._version import __version__

Sure enough, when you install the package (e.g., via pip) you will get the same
ergonomics as any other third-party library. One slight problem with this simplistic
approach is that if you are actively developing a project in a working copy of a
git repo, the version string will not generally capture local modifications---you
will keep getting the same version until you make a new tag. You might care or not
about this, but this is something that can be easily fixed with a slightly
more complicated ``__init__.py`` file, e.g.,

.. literalinclude:: ../src/metarep/__init__.py
