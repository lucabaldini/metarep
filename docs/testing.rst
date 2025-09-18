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

The |Python| standard library provides a ``unittest`` module that nobody uses
anymore, these days.

.. literalinclude:: ../tests/test_utils.py
