.. _linting:

Static code analysis
====================

Compiled languages like C and C++ will check lots of things at compile time and
will not even complete the compilation is something is not quite right. On the
other hand, interpreted languages like |Python| will typically fail at runtime,
which makes it somewhat harder to catch issues at early stages. (Well, we shall
concede that for plain syntax errors |Python| will refuse to assemble the bytecode
and the interpreted won't even start, but that's pretty much it.)

Trying catching issues as early as possible with an interpreted language such
as |Python| is typically done with two basic strategies: static code analysis and
unit testing. We shall examine the former in this section and defer the latter to
:ref:`testing`.

.. seealso::

  :ref:`testing`.

Consider this snippet for a second.

.. code-block:: python

  my_value = 0
  if very_unlikely_condition:
      myvalue = 42

Can you spot the issue with this code? We have a variable naming inconsistency:
`my_value` is defined with an underscore, but `myvalue` is used without one within
the ``if`` statement. Now, suppose that the condition that makes the program enter
the ``if`` block is indeed very unlikely, so much that you have never bumped into
it while developing and testing the code. Here you go: we have a beautiful bug that
your users will sooner or later trigger at runtime. (And, to some extent, this
is unavoidable.)

The fact is: you could imagine writing a small |Python| script that would be able
to parse the code and spot this specific issue `without actually executing any code`.
This is, in a nutshell, what we refer to as `static code analysis`: the process of
examining source code without running it to find potential errors, bugs, or areas
for improvement. The `static` part means the analysis happens on the code at rest,
not at runtime (that would be `dynamic` analysis).

Static analysis is amenable to catch a variety of issues: missing imports,
undefined variables, logical issues, type mismatches, duplicated code, style
violations, and security issues, to name a few. While these are not all equally
important, we shall concentrate on three areas:

* enforcing coding conventions---remember `PEP 8 <https://peps.python.org/pep-0008/>`_
  is your bible, here;
* catching logical problems and improving the overall code quality;
* enforcing type correctness, if you do use
  `type annotations <https://typing.python.org/en/latest/spec/annotations.html>`_.

We shall map these three areas into three specific tools, recognizing that there
are large overlaps in terms of how they operate.

.. warning::

  Using static code analysis is like using moderation with food and alcohol.
  There is always a good reason to start a diet next Monday, but if you do
  gain too much weight, it's gonna be more and more difficult to go back!
  Likewise, if you program intensively in the wild for six months and then
  you throw you repo at pylint, chances are that the output will be so long
  that you will never, ever want to do it again. If you start fresh and consistently
  adopot good practices from day one, instead, you will end up writing better code and
  saving time in the long run.

.. seealso::

  :ref:`tasks`.


Ruff
----

`Ruff <https://docs.astral.sh/ruff/>`_ is `an extremely fast Python linter and
code formatter, written in Rust.` (`Really` fast. You might not care particularly
care about this, but Astral literally did shock the community when Ruff first
came out.)

.. note::

  You will have to intall Ruff by hand (e.g., via ``pip``) if it is not installed
  on your system. If you use it regularly in your development it is also a good
  idea to add it in the proper section of your ``pyproject.toml`` file, e.g.,

  .. code-block:: toml

    [project.optional-dependencies]
    dev = [
       "ruff"
    ]

You can start by just doing

.. code-block:: shell

  ruff check .

and this will go through the Python file(s) in the current directory, but it
goes without saying that Ruff comes with a plethora of options to control the
output (e.g., to enable/disable specific rules or automatically fix problems).
Chances are that, in the long run, you will want to customize the default
behavior of the application. The good news is that you can do it just adding
specific sections to you ``pyproject.toml`` file, e.g.,

.. code-block:: toml

  # ruff configuration, see
  # https://docs.astral.sh/ruff/configuration/
  # for the ultimate reference.
  # Note we target the oldest Python version that we support, which helps
  # in avoiding features that are only available in newer versions.
  [tool.ruff]
  target-version = "py37"
  line-length = 100
  src = ["src"]
  exclude = ["docs"]

  # By default the ruff configuration is fairly minimal, and you might
  # want to specifically enable specific useful rules.
  [tool.ruff.lint]
  select = [
    "E",   # pycodestyle errors
    "F",   # pyflakes
    "I",   # isort (imports)
    "B",   # flake8-bugbear
    "UP",  # pyupgrade (kept safe for py37)
    "SIM", # flake8-simplify
    "C4",  # flake8-comprehensions
    "NPY", # NumPy-specific best practices
    "PERF" # performance gotchas
    ]
  # And, of course, sometimes you want to disable rules that are enabled
  # by default.
  ignore = [
    "C408" # I sometimes like dict() calls better than literal dicts
    ]

(This is just an example. You find all the gory details of the Ruff configuration
`here <https://docs.astral.sh/ruff/configuration/>`__.)


Pylint
------

Ruff is great because it is modern, blazingly fast, and to the point, but it is
mostly stylistic in nature, and not (yet) as insightful as some other tools.
`Pylint <https://pylint.readthedocs.io/en/latest/?badge=latest>`_, on the other hand,
offers a rich variety of semantic checks, which often lead to interesting avenues
for code refactoring. It goes without saying, this comes at the cost of a much
slower (and, quite possibly, noisier) experience.

In addition, being somewhat older in its design with respect to Ruff, Pylint is
not fully configurable via ``pyproject.toml``, although you can definitely tweak
the Pylint experience from there, e.g.,

.. code-block:: toml

  # On the other hand, pylint is fairly noisy by default, and you might
  # want to disable some rules.
  [tool.pylint.'MESSAGES CONTROL']
  disable = [
     "missing-docstring",
     "too-few-public-methods",
     "too-many-arguments",
     "too-many-positional-arguments",
     "too-many-instance-attributes",
     "too-many-locals",
     "use-dict-literal",
  ]

  [tool.pylint.'BASIC']
  good-names = ["i", "j", "k", "x", "y", "z"]

  [tool.pylint.'FORMAT']
  max-line-length = 100

Which one (Ruff and/or Pylint) and `how much` you want to use depends on your
workflow. One sensible strategy might be: use Ruff all the time---ideally before
any commit---and Pylint occasionally---to see whether there is room for deeper improvement
somewhere.

.. seealso::

  :ref:`actions`. (Yes: you can , and you should, have some basic linting in your
  GitHub action taking care of the continuous integration.)


mypy
----

This is something related to a subject that we have not touched at all up to this
point, but is relevant for the purpose of writing modern, idiomatic Python---that is:
`type annotations <https://typing.python.org/en/latest/spec/annotations.html>`_.
You might have stumbled across something like

.. code-block:: python

  def square(x: float) -> float:
      return x**2.

Now wait a minute: we do not declare the type of a variable in Python, do we? And
so what are these ``float`` qualifiers all about? They are examples of `type annotations`,
and are basically ignored by the Python interpreter when the code is executed---by
design they have absolutely no effect on the flow of the program.

What's the deal, then? Well they serve (at least) a twofold purpose:

* annotating the function arguments and return values helps `reasoning` about the
  code; what a function that you just wrote is actually doing might be crystal clear
  to you right now, but in two years type annotations will help you remember;
* they can be used by external static analyzer to find mistakes in the code.

(And, well, annotations are interesting per se in other contexts too, see e.g.,
`dataclasses <https://docs.python.org/3/library/dataclasses.html>`_.)

`mypy <https://mypy-lang.org/>`_ is the de factor standard when it comes to
type checking in Python. We don't have time to go much deeper, here, but if any of this
tickled your curiosity, by any means go out there and find out more!