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
are large overlaps in terms of how these tools operate.

.. warning::
   Using static code analysis is like using moderation with food and alcohol.
   There is always a good reason to start a diet next Monday, but if you do
   gain too much weight, it's gonna be more and more difficult to go back!



ruff
----


pylint
------



mypy
----