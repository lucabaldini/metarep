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
    """
    assert square(3) == 9.
    assert square(3.) == 9.


def test_array():
    """Test the square function with numpy arrays.
    """
    val = np.full(100, 3.)
    assert np.allclose(square(val), np.full(100, 9.))


def test_string():
    """Calling square() with a string as the argument should raise TypeError.
    """
    with pytest.raises(TypeError) as exception:
        square('hello')
    print(exception.info)
