.. _testing:

Unit testing
============

Let's suppose that you are asked to write a conversion function from cartesian
to polar coordinates. Do you picture yourself drafting the function, write a small
``print`` command to verify that ``(1., 1.)`` maps to ``(sqrt(2), pi/4)``, delete
(or comments out) the line with the ``print`` and move on? Well, if that's the case
you need to work on your workflow 🙂.

The basic idea behind unit testing is that you break your program into small pieces,
you create test cases for each piece where you verify that, for some known input
you get the expected output, and by adding more and more tests as you develop
your code, you build confidence that the overall program behaves in fact as
expected. From a purely operational standpoint, you run the tests every time
you modify the code to verify that you haven't broken anything; and whenever
you find a bug, you create a unit test that would trigger the bug so that,
from that point on, you rule out the possibility that the very same bug is
reintroduced. (Ok, this is a fairly rough introduction to unit testing, but you
get the idea.)

.. note::

  If you program long enought you will come across the concept of
  `test-driven development`. That is: before you even start coding anything,
  you write down all the specifications that your piece of code (e.g., a function)
  should satisfy in the form of a set of unit tests, and then you write the
  actual implementation and massage it until all the tests are passed.
  Pretty extreme for a physicist, but definitely not crazy, when you
  think about.


pytest
------

The |Python| standard library provides a
`unittest <https://docs.python.org/3/library/unittest.html>`_ module that, frankly
speaking nobody uses anymore, these days. (The documentation page, though, is still
a useful source of information). Since it looks all the hipe is currently on
`pytest <https://docs.pytest.org/en/stable/>`_, this is what we are using as well.

The basic idea is quite simple: for each module in ``src/pkgname`` you create a
corresponding Python file in ``tests`` that implements all the unit tests. In the
``pytest`` language, this is achieved with a series of function whose name
starts with ``test`` (and in which we define the logic of whether the test is
passed or not by using the ``assert`` Python keyword)---something along the lines of:

.. literalinclude:: ../tests/test_utils.py

With this in place, all you have to do is to run

.. code-block::

  pytest

and ``pytest`` will do all the magic: loop over the Python files in the ``test`` folder,
run all the test function, and collect the output. Cool.

Since we are at it, note how testing is largely less obvious of what it might seem
at a first glance. How would you go about testing a function that calculates the square
of a number? Well, for one thing you'd line the square of 3 to be 9. And then you start
wondering: does it make any difference if I pass ``float`` 3. or ``int`` 3, and should it?
And again, since we physicists cruch numbers as our day job and like using |numpy|,
shall we make sure that the function works on arrays? And, by the way, what about
all the discussions about the floating-point arithmetics being inherently non exact and
the push to refrain from comparing floating-point numbers? Oh, and how about strings?

You got the point. We wrote a one-line function and opened up the floor for
infinite testing...


Continuous integration
----------------------

Now that we got all the unit tests lined up for our tiny module and an awesome
framework to run them, there is one more thing. You are welcome to run your unit tests
locally whenever you change your code. Totally. (Actually, you should definitely do so).
But that is not enough---the quality of your code should not be hostage of the fact
that you remember (or not) to run the test manually. All the unit tests should be
run automatically under certain circumstances (e.g., when you modify a branch with an
open pull request, or when you push something on the main) and you should have somebody
knocking at your door (metaphorically) if something goes wrong. This is typically
referred to as `continuous integration`.

It's a good thing that we encounter the same issue of automatically triggering things
when discussing how one goes about publishing the documentation, and the answer is the
same: a GitHub action. Let's take a look at what we are doing for our small package:

.. literalinclude:: ../.github/workflows/ci.yml
   :language: yaml

At this point most of the stuff shoulf be self-explaining. Oh, and note we are running
Ruff before we run pytest. If the thing does not pass the static analysis tests we don't
even bother running the code.

.. seealso::

  :ref:`actions`.