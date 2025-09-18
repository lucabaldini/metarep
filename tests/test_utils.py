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

"""Unit tests for the utils module.
"""

import numpy as np
import pytest

from metarep.utils import square


def test_numbers():
    """Test the square function with numbers.

    Note in principle we have to test integers and floating points separately.
    As documented in the underlying function, the output is always expected to
    be a floating point.
    """
    assert square(3) == 9.
    assert square(3.) == 9.
    assert square(-3) == 9.
    assert square(-3.) == 9.


def test_array():
    """Test the square function with numpy arrays.

    This is similar, in spirit, to the previous test. Note the use of the
    np.allclose() method.
    """
    assert np.allclose(square(np.full(100, 3)), np.full(100, 9.))
    assert np.allclose(square(np.full(100, 3.)), np.full(100, 9.))


def test_string():
    """Calling square() with a string as the argument should raise TypeError.
    """
    with pytest.raises(TypeError) as exception:
        square('hello')
    print(f'Caught exception {exception}')
