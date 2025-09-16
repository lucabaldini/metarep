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

import argparse
import ast
from enum import Enum

from packaging.version import parse, Version

from metarep import METAREP_DOCS, METAREP_SRC

_VERSION_FILE_PATH = METAREP_SRC / "_version.py"
_RELEASE_NOTES_PATH = METAREP_DOCS / "release_notes.rst"
_ENCODING = "utf-8"


class BumpMode(str, Enum):

    """Small enum class describing the bump mode.
    """

    MAJOR = "major"
    MINOR = "minor"
    MICRO = "micro"


def read_version() -> Version:
    """Read the version string from the version file.

    Note the version file is assumed to contain exactly one line of the form
    __version__ = "version_string"
    The version string must be a valid PEP 440 version string, which is
    actively enforced by casting it to a packaging.version.Version object.
    """
    print(f"Reading version from {_VERSION_FILE_PATH}...")
    with open(_VERSION_FILE_PATH, encoding=_ENCODING) as input_file:
        line = input_file.readline().rstrip("\n")
    # If the line does not start with __version__ something went wrong...
    if not line.startswith("__version__"):
        raise ValueError(f"Invalid version file content: {line}")
    # partition() splits the string in exactly three parts around the separator.
    _, _, version_string = line.partition("=")
    # And we still need to strip the whitespaces, and get rid of the quotes.
    return parse(ast.literal_eval(version_string.strip()))


def bump_version(version: Version, mode: BumpMode) -> Version:
    """Bump the version string.
    """
    print(f'Bumping version (mode = {mode})...')
    major, minor, micro = version.release
    if mode == BumpMode.MAJOR:
        version_string = f"{major + 1}.0.0"
    elif mode == BumpMode.MINOR:
        version_string = f"{major}.{minor + 1}.0"
    elif mode == BumpMode.MICRO:
        version_string = f"{major}.{minor}.{micro + 1}"
    else:
        raise ValueError(f"Invalid bump mode {mode}")
    return Version(version_string)


def write_version(version: Version) -> None:
    """Write a given version string to the version file.
    """
    print(f"Writing version {version} to {_VERSION_FILE_PATH}...")
    with open(_VERSION_FILE_PATH, "w", encoding=_ENCODING) as output_file:
        output_file.write(f'__version__ = "{version}"\n')


def release(mode: BumpMode) -> None:
    """Release a new version of the package.
    """
    old_version = read_version()
    new_version = bump_version(old_version, mode)
    write_version(new_version)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Release a new version of the package.")
    parser.add_argument("mode", choices=[mode.value for mode in BumpMode],
                        help="The version bump mode.")
    args = parser.parse_args()
    release(BumpMode(args.mode))
