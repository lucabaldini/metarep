.. _tasks:

Common tasks
============

As you start developing a project with even a moderate complexity, you will
realize immediately that there are tasks that you want to perform quite frequently
on the working copy of your repository: compiling the documentation, run the
unit tests, running some static analysis, cleaning up the files generated in the
process, and potenatially a lot of other things.

.. seealso::

  :ref:`documentation`, :ref:`testing`, :ref:`linting`.

Each one is presumably achieved with some more or less complex command in your shell,
and there is nothing fundamental that prevents you from doing just that. The fact is,
there are well-developed utilities out there that assist you in this, and there is
no reason not to use this extra-help.


nox
---

`nox <https://nox.thea.codes/en/stable/>`_ is a command-line tool that automates testing
in multiple Python environments. The thing is dead simple: you create a ``noxfile.py`` file
(ah ah: that was it!) with the definition of your tasks, and nox does the rest.

.. note::

  If you are old enough you can think of nox as a Python-oriented version of make, and
  ``noxfile.py`` as the corresponding ``Makefile``. There is a fundamental difference,
  in that nox is design to perform tasks in a `isolated` environment, where you have
  full control of the version of all the packages you need and of Python itself, but
  this goes beyond our scope. At a more superficial level the good thing is that you
  get the same ergonomics on GNU-Linux, Windows and Mac.

Let's proceed inductively, as usual. Or ``noxfile.py`` looks like

.. literalinclude:: ../noxfile.py
   :language: python

Without going into to much details, which you find in the nox documentation anyway,
you do recognize the typical tasks we have listed before. Want to compile the
documentation?

.. code-block:: shell

  nox -s docs

Want to pass extra arguments to ``sphinx-build``, e.g., the ``--E`` flag to regenerate
everything, reprocessing even the files that have not been changed? You can easily
do so listing all the extra options after a ``--``

.. code-block:: shell

  nox -s docs -- -E
