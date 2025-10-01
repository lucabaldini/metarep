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

import pathlib
import subprocess

from ._version import __version__ as __base_version__


def _git_suffix() -> str:
    """If we are in a git repo, we want to add the necessary information to the
    version string.

    This will return something along the lines of ``+gf0f18e6.dirty``.
    """
    # pylint: disable=broad-except
    kwargs = dict(cwd=pathlib.Path(__file__).parent, stderr=subprocess.DEVNULL)
    try:
        # Retrieve the git short sha to be appended to the base version string.
        args = ["git", "rev-parse", "--short", "HEAD"]
        sha = subprocess.check_output(args, **kwargs).decode().strip()
        suffix = f"+g{sha}"
        # If we have uncommitted changes, append a `.dirty` to the version suffix.
        args = ["git", "diff", "--quiet"]
        if subprocess.call(args, stdout=subprocess.DEVNULL, **kwargs) != 0:
            suffix = f"{suffix}.dirty"
        return suffix
    except Exception:
        return ""


__version__ = f"{__base_version__}{_git_suffix()}"
