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


A dead-simple workflow
----------------------

As you might imagine, keeping track of the version of your software boils down to
having a `version string` hard-coded somewhere in your codebase. This can actually get
trickier than it might seem at a first glance, as the version number is needed in several
different places for slightly different reasons (tags are managed by git in the first
place, but presumably you need ``__version__`` to be defined in some Python file, while
your ``pyproject.toml`` needs to be version-aware, and you might want to spell out which
version the online documentation refers to---perhaps in the release notes).

Now: whatever strategy you resort to, you need to make sure that the information you
disseminate in the wild is self-consistent. As is often the case, this is a well-known
problem that has been fixed for you. If you use `hatch <https://github.com/pypa/hatch>`_
(with fellow ``hatchling`` build manager) to manage your Python project (if you have
no idea, then there is no reason for you not to do it) `hatch-vcs <https://github.com/ofek/hatch-vcs>`_
is a plugin designed to seamlessly use git to determine the project version. Really.
You don't have to do anything, except for setting up your ``pyproject.toml`` file properly,
e.g.

.. code-block::

    [build-system]
    requires = ["hatchling>=1.24", "hatch-vcs>=0.3"]
    build-backend = "hatchling.build"

    [tool.hatch.version]
    source = "vcs"

    [tool.hatch.build.hooks.vcs]
    version-file = "src/package-name/_version.py"

In a nutshell: the first block specifies that you need ``hatchling`` and ``hatch-vsc``
(don't worry: ``pip`` will install as needed when you pip-install your package) and you
are using the former as your build system. This is all pretty standard these days.
The second block implies that the version of your package is automatically fetched from
git by the ``hatch-vsc`` plugin. At build time this will create a small Python module
(you name it in the third block) with all the information that you need. The latter might
look like

.. literalinclude:: ../src/metarep/_version.py

.. note::

    As the comment at the top of the file clearly states, the ``hatch-vcs`` version
    file is automatically generated---you should not edit it by hand, nor track it
    in version control (i.e., it should be listed in your ``.gitignore`` file).

That's it. In your top-level ``__init__.py`` file put

.. code-block:: Python

    from ._version import __version__

and you have for free the ergonomics of the best Python packages on the market.


Semantic versioning
-------------------