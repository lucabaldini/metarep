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

from enum import Enum

from metarep import METAREP_SRC

_VERSION_FILE_PATH = METAREP_SRC / "_version.py"
_ENCODING = "utf-8"


class BumpMode(str, Enum):

    """Small enum class describing the bump mode.
    """

    MAJOR = "major"
    MINOR = "minor"
    MICRO = "micro"


def read_version() -> str:
    """Read the version string from the version file.
    """
    print(f"Reading version string from {_VERSION_FILE_PATH}...")
    with open(_VERSION_FILE_PATH, "r", encoding=_ENCODING) as input_file:
        _, version = input_file.readline().split("=")
    version = version.strip().strip('"').strip("'")
    print(f"Done, version {version} found.")
    return version


def bump_version(version: str, mode: BumpMode) -> str:
    """Bump the version string.
    """
    major, minor, micro = [int(item) for item in version.split(".")]
    if mode == BumpMode.MAJOR:
        return f"{major + 1}.0.0"
    elif mode == BumpMode.MINOR:
        return f"{major}.{minor + 1}.0"
    elif mode == BumpMode.MICRO:
        return f"{major}.{minor}.{micro + 1}"
    else:
        raise ValueError(f"Invalid bump mode {mode}")


def write_version(version: str) -> None:
    """Write a given version string to the version file.
    """
    print(f"Writing version string {version} to {_VERSION_FILE_PATH}...")
    with open(_VERSION_FILE_PATH, "w", encoding=_ENCODING) as output_file:
        output_file.write(f'__version__ = "{version}"\n')
    print('Done.')


if __name__ == "__main__":
    version = read_version()
    print(version)
    print(bump_version(version, BumpMode.MAJOR))
    print(bump_version(version, BumpMode.MINOR))
    print(bump_version(version, BumpMode.MICRO))
    write_version("0.1.0")