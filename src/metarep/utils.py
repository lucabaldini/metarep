# Copyright (C) 2025 Luca Baldini (luca.baldini@pi.infn.it)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


def square(x):
    """Return the square of a single number or a numpy array.

    Note by virtue of the ``2.`` (vs. ``2``) at the exponent, the output value
    is always a float, or an array of floats, even if the input is an integer
    (or an array of integers).

    Example
    -------

    >>> square(2)
    4.0
    >>> square(np.array([1, 2, 3]))
    array([1., 4., 9.])

    Arguments
    ---------
    x : array_like
        Input value(s) to be squared. This can be either a number (int or float)
        or a numpy array.

    Returns
    -------
    array_like
        The squared value(s) of the input.
    """
    return x**2.
