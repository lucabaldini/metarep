.. _install:

Installation and usage
======================

Packaging and distribution are key aspects of any Python project, and two that
underwent a significant evolution over the last few years.

The bottomline is: you should ship a ``pyproject.toml`` file with your project.
For reference, the one we are distributing with this repository looks like

.. literalinclude:: ../pyproject.toml

pyproject files can be arbitrarily complex, and encompass any sort of meta
information that goes along with your project, but, at the very basic level,
they make your project `installable.` This means that including a properly
formatted ``pyproject.toml`` file will allow a user to, e.g., ``pip install`` your
package transprently---directly from PyPI, if you have added your package there,

.. code-block:: shell

    pip install package

or locally at the very minimum

.. code-block:: shell

    pip install .

This is it. All the files get copied into a place where they can be imported from,
and it is the ``pyproject.toml`` file that makes that possible.


.. note::

    Explain pip.


Editable installation
---------------------

When you `develop` (as opposed to `use`) a package, you want to install it
in `editable` mode.

.. code-block:: shell

    pip install -e .

Invoking ``pip`` with the ``-e`` command-line switch will place a special
link in the proper folder pointing back to you local version of the source
files (instead of copying the source tree) so that you will always see the
last version of the code as you modify it, e.g., in the local copy of your
git repository. Needless to say, it is still the ``pyproject.toml`` file that
makes all the magic.

.. note::

    You can achieve the same result by just making sure that the
    ``PYTHONPATH`` environmental variable is pointing to the folder where
    your Python modules live, and in fact you might as well do that. That is
    not necessarily considered a good practice, as it departs completely
    from the installation path of a typical Python package that you use as
    a library, but you should still make sure you understand the basic internals
    of the Python import system.
